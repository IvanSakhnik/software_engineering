
global proc_ident
global var_ident
global ident_list
global wrong_ident
global labels
proc_ident = []
var_ident = []
ident_list = []
wrong_ident = []
labels = []


def search_index (list, search_elem):
	index = -1
	for elem in list:
		index+=1
		if elem == search_elem:
			return index
	return -1



def ident_err(node):
	global labels
	global proc_ident
	global var_ident

	for i in range (0, len(node.leaves)):
		if (node.leaves[i].val == "statement"):
			if (node.leaves[i].leaves[0].val == "unsigned-integer" and node.leaves[i].leaves[1].val == ":"):
				if ( not node.leaves[i].leaves[0].leaves[0].val in labels):
					labels.append(node.leaves[i].leaves[0].leaves[0].val)
				else:
					wrong_ident.append(node.leaves[i].leaves[0].leaves[0].val)


	for i in range (0, len(node.leaves)):
		if (node.leaves[i].val == "procedure-identifier"):
			proc_ident.append(node.leaves[i].leaves[0].leaves[0].val)

	for i in range (0, len(node.leaves)):
		if (node.leaves[i].val == "variable-identifier"):
			if (node.leaves[i].leaves[0].leaves[0].val in proc_ident):
				wrong_ident.append(node.leaves[i].leaves[0].leaves[0].val)
			else:
				var_ident.append(node.leaves[i].leaves[0].leaves[0].val)

	for i in range(len(node.leaves)):
		ident_err(node.leaves[i])


def kompile(tree):
	global proc_ident
	global var_ident

	ident_err(tree.root)

	generator(tree.root)


def proc(node):
	global ident_list
	if (node.val == "identifier"):
		if (not(node.leaves[0].val in wrong_ident)):
			ident_list.append(node.leaves[0].val)
		else:
			ident_list.append(search_index(wrong_ident, node.leaves[0].val))
	for i in range(len(node.leaves)):
		proc(node.leaves[i])
	return ident_list


def generator (node):
	global program_identifier
	global ident_list

	if (node.val == "PROGRAM"):
		program_identifier = node.parent_element.leaves[1].leaves[0].leaves[0].val
		line = '; '
		line+= program_identifier
		wrong_ident.append(program_identifier)
		line += "\ncode SEGMENT\n\tASSUME cs:code\nbegin:"
		print(line)

	elif (node.val == "statement"):
		line=''
		if (node.leaves[0].val == "procedure-identifier"):
			ident_list = proc(node.leaves[1])
			for elem in ident_list:
				if type(elem) == str:
					line += '\n\tpush '
					line += elem
				else:
					print(line)
					print("This identifier already exist ", wrong_ident[elem])
					quit()


			line += '\n\tcall '
			if (node.leaves[0].leaves[0].leaves[0].val in wrong_ident):
				print (line)
				print ("\nProcedure name can`t be equal program name", node.leaves[0].leaves[0].leaves[0].val)
				quit()
			else:
				line+= node.leaves[0].leaves[0].leaves[0].val

			print(line)

		elif (node.leaves[0].val == "GOTO"):
			line = '\tjmp '
			if (node.leaves[1].leaves[0].val in labels):
				line+=node.leaves[1].leaves[0].val
				print(line)
			else:
				print ("No such label", node.leaves[1].leaves[0].val)
				quit()

		elif (node.leaves[1].val == ":="):
			line = '\tmov '
			line += node.leaves[0].leaves[0].leaves[0].val
			line += ', '
			line += node.leaves[2].leaves[0].val
			print(line)

		elif (node.leaves[1].val == ":"):
			line=''
			if (node.leaves[0].leaves[0].val in wrong_ident):
				print ("This label already exist", node.leaves[0].leaves[0].val)
				quit()
			line += node.leaves[0].leaves[0].val
			line += ":"
			print(line)

		elif (node.leaves[0].val == "LINK"):
			line ='\t'
			ident = node.leaves[1].leaves[0].leaves[0].val
			if ident in wrong_ident:
				print( "\nThis identifier already exist ", ident)
				quit()
			line += node.leaves[0].val
			line += " "
			line += node.leaves[1].leaves[0].leaves[0].val
			line += ", "
			line += "ebp"
			print(line)

		elif (node.leaves[0].val == "IN"):
			line ='\t'
			line += node.leaves[0].val
			line += " ["
			line += node.leaves[1].leaves[0].val
			line += ", 16*bp]"
			print(line)

		elif (node.leaves[0].val == "OUT"):
			line ='\t'
			line += node.leaves[0].val
			line += " ["
			line += node.leaves[1].leaves[0].val
			line += ", 4*ex]"
			print(line)

		elif (node.leaves[0].val == "($"):
			filename = node.leaves[1].leaves[0].leaves[0].val
			filename += ".asm"
			try:
				file = open(filename)
			except IOError as e:
				print(u'\nNo such file', filename)
				quit()
			else:
				file = open(filename, "r")
				line = file.read()
				print(line)

	elif (node.val == "END"):
		line = "\tret  0\n"
		line += "\n\tmov ax, 4c00h\n\tint 21h\ncode ENDS\n\tend begin"
		print(line)


	for i in range(len(node.leaves)):
		generator(node.leaves[i])
