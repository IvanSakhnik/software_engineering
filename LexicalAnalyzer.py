#Lexical analyzer 

from InformationTables import *

def runLexicalAnalyzer(file_name):
	white_space=[32, 13, 10, 9, 11, 12]
	digits=[i for i in range(48, 57)]
	chars=[i for i in range(65, 90)]
	separetors=[i for i in separetors_dictionary.keys()]
	separetors_comp=[i for i in separetors_comp_dictionary.keys()]
	key_words=[i for i in key_words_dictionary.keys()]
	tmp=''
	list_out=[]
	ident_counter=1001
	const_counter=501
	file=open(file_name)
	ch=file.read(1)
	numb=1
	while ch:
		if ch=="\n":
			numb+=1

		if ord(ch) in white_space:
			ch=file.read(1)

		elif ch==':':
			tmp+=ch
			ch=file.read(1)
			if ch=='=':
				tmp+=ch
				list_out.append(separetors_comp_dictionary[tmp])
				ch=file.read(1)
			else:
				list_out.append(separetors_dictionary[tmp])
			tmp=''

		elif ch=='(':
			tmp+=ch
			ch=file.read(1)
			if ch=='$':
				tmp+=ch
				list_out.append(separetors_comp_dictionary[tmp])
				ch=file.read(1)
			elif ch=="*":
				ch=file.read(1)
				while ch:
					if ch=="*":
						ch=file.read(1)
						if ch==")":
							ch=file.read(1)
							break
					else:
						ch=file.read(1)				
			else:
				list_out.append(separetors_dictionary[tmp])
			tmp=''	

		elif ch=='$':
			tmp+=ch
			ch=file.read(1)
			if ch==')':
				tmp+=ch
				list_out.append(separetors_comp_dictionary[tmp])
				tmp=''
				ch=file.read(1)
			else:
				print("Expected ')' in line: ", numb)
				quit()

		elif ch in separetors:
			tmp+=ch
			ch=file.read(1)
			list_out.append(separetors_dictionary[tmp])
			tmp=''

		elif ord(ch) in digits:
			tmp+=ch
			ch=file.read(1)
			while ch and ord(ch) in digits:
				tmp+=ch
				ch=file.read(1)
			if tmp in const_dictionary.keys():
				list_out.append(const_dictionary[tmp])
				tmp=''
			else:
				const_dictionary[tmp]=const_counter
				list_out.append(const_counter)
				const_counter+=1
				tmp=''

		elif ord(ch) in chars:
			tmp+=ch
			ch=file.read(1)
			while ch and (ord(ch) in chars or ord(ch) in digits):
				tmp+=ch
				ch=file.read(1)
			if tmp in key_words:
				list_out.append(key_words_dictionary[tmp])
				tmp=''
			else:
				if tmp in identificators_dictionary.keys():
					list_out.append(identificators_dictionary[tmp])
					tmp=''
				else:
					identificators_dictionary[tmp]=ident_counter
					list_out.append(ident_counter)
					ident_counter+=1
					tmp=''

		else:
			print("Invalid symbol in line: ", numb)
			quit()


	file.close()
	return list_out

def printResultLexicalAnalyzer(result):
	print("-"*167)
	print("Result lexical analyzer: ", result)
	print("-"*167)


# if __name__ == '__main__':
# 	runLexicalAnalyzer("MyTestProgram.txt")
# 	printResultLexicalAnalyzer(runLexicalAnalyzer("MyTestProgram.txt"))
# 	printInformationTables()
