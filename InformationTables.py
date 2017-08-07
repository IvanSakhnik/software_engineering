#information tables

separetors_dictionary = {	";" : 59, 
							":" : 58, 
							"," : 44, 
							"(" : 40, 
							")" : 41,
							"=" : 42 }

separetors_comp_dictionary = {	":=" : 301, 
								"($" : 302, 
								"$)" : 303 }

key_words_dictionary = {	"PROGRAM" : 401, 
							"BEGIN"   : 402, 
							"END" 	  : 403, 
							"GOTO"    : 404, 
							"LINK"    : 405, 
							"IN"      : 406, 
							"OUT"     : 407, 
							"RETURN"  : 408 }
const_dictionary = {}
identificators_dictionary = {}

def printInformationTables():
	print("-"*167)
	print("separetors_dictionary: ", separetors_dictionary)
	print("separetors_comp_dictionary: ", separetors_comp_dictionary)
	print("key_words_dictionary: ", key_words_dictionary)
	print("const_dictionary: ", const_dictionary)
	print("identificators_dictionary: ", identificators_dictionary)
	print("-"*167)
