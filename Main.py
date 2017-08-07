#main

from InformationTables import *
from LexicalAnalyzer import*
from Parser import *
from Generator import kompile



if __name__ == '__main__':

	string_lexems = runLexicalAnalyzer("MyTestProgram.txt")

	printResultLexicalAnalyzer(string_lexems)
	printInformationTables()

	signal_program()
	tree.print_tree()

	print("*"*167)

	kompile(tree)
