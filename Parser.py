"""
    Parser
    Top-down analysis
    Recursive descent algorithm
"""

from InformationTables import *
from LexicalAnalyzer import*
from Tree import *

error_table = {  "Expected ';'!" 	        :        -1, 
				 "Expected 'PROGRAM'!"      :        -2, 
				 "Wrong ID!"                :        -3, 
				 "Expected 'BEGIN'!"        :        -4,
				 "Expected 'END'!"          :        -5,
                 "Wrong NUMBER"             :        -6, 
                 "Expected '('!"            :        -7,
                 "Expected ')'!"            :        -8,
                 "Expected ','!"            :        -9,
                 "Expected '$)'!"           :        -10,
                 "Expected ':'!"            :        -11,
                 "Statement ERROR"          :        -12  }

string_lexems = runLexicalAnalyzer("MyTestProgram.txt")
tree = Tree()
count = 0	#counter to go to the next token		

#function returns the key if the value is found
def scan(dictionary, value):
    for key, v in dictionary.items():
        if v == value:
            return key

def printError(err_number):														
    tree.add(err_number)												
    tree.current_element = tree.current_element.parent_element
    tree.print_tree()
    print("ERROR", err_number, "!!!", scan(error_table, err_number))
    quit()

def program(count):
    tree.add('program')
    lexem = string_lexems[count]
    if lexem == 401:
        tree.add (scan (key_words_dictionary, lexem) )
        tree.current_element = tree.current_element.parent_element
        count += 1
        lexem = string_lexems[count]
        procedure_identifier(lexem);
        count += 1
        lexem = string_lexems[count]
        if lexem == 59:
             tree.add (scan (separetors_dictionary, lexem) )
             tree.current_element = tree.current_element.parent_element
        else:
            printError(-1)
        count += 1
        count = block(count)
        count += 1
        lexem = string_lexems[count]
        if lexem == 59:
            tree.add (scan (separetors_dictionary, lexem) )
            tree.current_element = tree.current_element.parent_element
        else:
            printError(-1)
        lexem = string_lexems[count]
    else:
        printError(-2)
    tree.current_element = tree.current_element.parent_element

def identifier(lexem):
    tree.add('identifier')
    if lexem >= 1000:
        tree.add (scan (identificators_dictionary, lexem) )
        tree.current_element = tree.current_element.parent_element
    else:
        printError(-3)
    tree.current_element = tree.current_element.parent_element

def procedure_identifier(lexem):
    tree.add('procedure-identifier')
    identifier(lexem)
    tree.current_element = tree.current_element.parent_element

def variable_identifier(lexem):
    tree.add('variable-identifier')
    identifier(lexem)
    tree.current_element = tree.current_element.parent_element

def assembly_insert_file_identifier(lexem):
    tree.add('variable-identifier')
    identifier(lexem)
    tree.current_element = tree.current_element.parent_element

def block(count):
    tree.add('block')
    lexem = string_lexems[count]
    if lexem == 402:
        tree.add (scan (key_words_dictionary, lexem) )
        tree.current_element = tree.current_element.parent_element
    else:
        printError(-4)
    count += 1
    count = statements_list(count)
    lexem = string_lexems[count]
    if lexem == 403:
        tree.add(scan(key_words_dictionary, lexem))
        tree.current_element = tree.current_element.parent_element
    else:
        printError(-5)
    tree.current_element = tree.current_element.parent_element
    return count;

def unsigned_integer(lexem):
    tree.add('unsigned-integer')
    if lexem in range (500, 600):
        tree.add (scan (const_dictionary, lexem) )
        tree.current_element = tree.current_element.parent_element
    else:
        printError(-6)
    tree.current_element = tree.current_element.parent_element

def actual_arguments(count):
    tree.add('actual-arguments')
    lexem = string_lexems[count]
    if lexem == 59:
        tree.add('empty')
        tree.current_element = tree.current_element.parent_element
        tree.current_element = tree.current_element.parent_element
        return count
    else:
        if lexem == 40:
            tree.add (scan (separetors_dictionary, lexem) )
            tree.current_element = tree.current_element.parent_element
        else:
            printError(-7)
        count += 1
        lexem = string_lexems[count]
        variable_identifier(lexem)
        count += 1
        lexem = string_lexems[count]
        if lexem != 41:
            count = actual_arguments_list(count)
            lexem = string_lexems[count]
            if lexem == 41:
                tree.add (scan (separetors_dictionary, lexem) )
                tree.current_element = tree.current_element.parent_element
            else: 
                printError(-8)
        else:
            tree.add (scan (separetors_dictionary, lexem) )
            tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    return count

def actual_arguments_list(count):
    tree.add('actual-arguments-list')
    lexem = string_lexems[count]
    if lexem == 44:
        tree.add (scan (separetors_dictionary, lexem) )
        tree.current_element = tree.current_element.parent_element
    else:
        printError(-9)
    count += 1
    lexem = string_lexems[count]
    variable_identifier(lexem)
    count += 1
    lexem = string_lexems[count]
    if lexem != 41:
        count = actual_arguments_list(count)
    tree.current_element = tree.current_element.parent_element
    return count

def statements_list(count):
    tree.add('statement-list')
    lexem = string_lexems[count]
    if lexem == 403:
        tree.add('empty')
        tree.current_element = tree.current_element.parent_element
        tree.current_element = tree.current_element.parent_element
        return count
    else:
        count = statement(count)
        count += 1
        lexem = string_lexems[count]
        if lexem != 403:
            count = statements_list(count)
    tree.current_element = tree.current_element.parent_element
    return count


def statement(count):
    tree.add('statement')
    lexem = string_lexems[count]
    if lexem == 404:
        tree.add (scan (key_words_dictionary, lexem) )
        tree.current_element = tree.current_element.parent_element
        count += 1
        lexem = string_lexems[count]
        unsigned_integer(lexem)
        count += 1
        lexem = string_lexems[count]
        if lexem == 59:
            tree.add (scan (separetors_dictionary, lexem) )
            tree.current_element = tree.current_element.parent_element
        else:
            printError(-1)


    elif lexem == 405:
        tree.add (scan (key_words_dictionary, lexem) )
        tree.current_element = tree.current_element.parent_element
        count += 1
        lexem = string_lexems[count]
        variable_identifier(lexem)
        count += 1
        lexem = string_lexems[count]
        if lexem == 44:
            tree.add (scan (separetors_dictionary, lexem) )
            tree.current_element = tree.current_element.parent_element
        else:
            printError(-9)
        count += 1
        lexem = string_lexems[count]
        unsigned_integer(lexem)
        count += 1
        lexem = string_lexems[count]
        if lexem == 59:
            tree.add (scan (separetors_dictionary, lexem) )
            tree.current_element = tree.current_element.parent_element
        else:
            printError(-1)

    elif lexem==408:
        tree.add (scan (key_words_dictionary, lexem) )
        tree.current_element = tree.current_element.parent_element
        count += 1
        lexem = string_lexems[count]
        if lexem == 59:
            tree.add (scan (separetors_dictionary, lexem) )
            tree.current_element = tree.current_element.parent_element
        else:
            printError(-1)            


    elif lexem == 406 or lexem == 407:
        tree.add (scan (key_words_dictionary, lexem) )
        tree.current_element = tree.current_element.parent_element
        count += 1
        lexem = string_lexems[count]
        unsigned_integer(lexem)
        count += 1
        lexem = string_lexems[count]
        if lexem == 59:
            tree.add (scan (separetors_dictionary, lexem) )
            tree.current_element = tree.current_element.parent_element
        else:
            printError(-1)

    elif lexem == 59:
        tree.add (scan (separetors_dictionary, lexem) )
        tree.current_element = tree.current_element.parent_element


    elif lexem == 302:
        tree.add (scan (separetors_comp_dictionary, lexem) )
        tree.current_element = tree.current_element.parent_element
        count +=1
        lexem = string_lexems[count]
        assembly_insert_file_identifier(lexem)
        count += 1
        lexem = string_lexems[count]
        if lexem == 303:
            tree.add (scan (separetors_comp_dictionary, lexem) )
            tree.current_element = tree.current_element.parent_element
        else:
            printError(-10)

    elif lexem in range(500,600):
        unsigned_integer(lexem)
        count += 1
        lexem = string_lexems[count]
        if lexem == 58:
            tree.add (scan (separetors_dictionary, lexem) )
            tree.current_element = tree.current_element.parent_element
        else:
            printError(-11)
        count += 1
        count = statement(count)


    elif lexem >= 1000:
        prev_lexem = string_lexems[count]
        count += 1
        lexem = string_lexems[count]
        if lexem == 301:
            variable_identifier(prev_lexem)
            tree.add (scan (separetors_comp_dictionary, lexem) ) 
            tree.current_element = tree.current_element.parent_element
            count += 1
            lexem = string_lexems[count]
            unsigned_integer(lexem)
            count += 1
            lexem = string_lexems[count]
            if lexem == 59:
                tree.add (scan (separetors_dictionary, lexem) )
                tree.current_element = tree.current_element.parent_element
            else:
                printError(-1)
        else:
            procedure_identifier(prev_lexem)
            count = actual_arguments(count)
            count += 1
            lexem = string_lexems[count]
            if lexem == 59:
                tree.add (scan (separetors_dictionary, lexem) )
                tree.current_element = tree.current_element.parent_element
            else:
                printError(-1)
    else:
        printError(-12)
    tree.current_element = tree.current_element.parent_element
    return count

def signal_program():
    program(count)


# if __name__ == '__main__':
#     signal_program()
#     tree.print_tree()