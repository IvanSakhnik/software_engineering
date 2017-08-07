from tree import Tree
from lexer import *


def syntax(fname):
    lexems = lexer(fname)
    table=[
		{'num': 0,  'name': 'signal-program',              		'code': [-1],     			'at': 1, 'af': 1},

		{'num': 1,  'name': 'program',                     		'code': [401],    			'at': 0, 'af': 1},
		{'num': 2,  'name': 'program',                     		'code': [-44],      		'at': 0, 'af': 1},
		{'num': 3,  'name': 'program',                     		'code': [59],     			'at': 0, 'af': 1},
		{'num': 4,  'name': 'program',                     		'code': [-6],     			'at': 0, 'af': 1},
		{'num': 5,  'name': 'program',                     		'code': [59],     			'at': 1, 'af': 1},

		{'num': 6,  'name': 'block',                       		'code': [402],    			'at': 0, 'af': 1},
		{'num': 7,  'name': 'block',                       		'code': [-9],     			'at': 0, 'af': 1},
		{'num': 8,  'name': 'block',                       		'code': [403],    			'at': 1, 'af': 1},

		{'num': 9,  'name': 'statements-list',             		'code': [-12],      		'at': 0, 'af': 1},
		{'num': 10, 'name': 'statements-list',             		'code': [-9],     			'at': 1, 'af': 0},
		{'num': 11, 'name': 'statements-list',             		'code': [],    				'at': 1, 'af': 1},

		{'num': 12,  'name': 'statement',             			'code': [-42],      		'at': 0, 'af': 1},
		{'num': 13,  'name': 'statement',             			'code': [58],       		'at': 0, 'af': 1},
		{'num': 14,  'name': 'statement',             			'code': [-12],      		'at': 1, 'af': 0},

		{'num': 15,  'name': 'statement',             			'code': [-43],      		'at': 0, 'af': 1},
		{'num': 16,  'name': 'statement',             			'code': [301],      		'at': 0, 'af': 1},
		{'num': 17,  'name': 'statement',             			'code': [-42],      		'at': 0, 'af': 1},
		{'num': 18,  'name': 'statement',             			'code': [59],       		'at': 1, 'af': 0},

		{'num': 19,  'name': 'statement',             			'code': [-44],      		'at': 0, 'af': 1},
		{'num': 20,  'name': 'statement',             			'code': [46],       		'at': 0, 'af': 1},
		{'num': 21,  'name': 'statement',             			'code': [59],       		'at': 1, 'af': 0},
		{'num': 22,  'name': 'statement',             			'code': [404],      		'at': 0, 'af': 1},
		{'num': 23,  'name': 'statement',             			'code': [-42],      		'at': 0, 'af': 1},
		{'num': 24,  'name': 'statement',             			'code': [59],       		'at': 1, 'af': 0},

		{'num': 25,  'name': 'statement',             			'code': [405],      		'at': 0, 'af': 1},
		{'num': 26,  'name': 'statement',             			'code': [-43],      		'at': 0, 'af': 1},
		{'num': 27,  'name': 'statement',             			'code': [44],       		'at': 0, 'af': 1},
		{'num': 28,  'name': 'statement',             			'code': [-42],      		'at': 0, 'af': 1},
		{'num': 29,  'name': 'statement',             			'code': [59],       		'at': 1, 'af': 0},

		{'num': 30,  'name': 'statement',             			'code': [406],      		'at': 0, 'af': 1},
		{'num': 31,  'name': 'statement',             			'code': [-42],      		'at': 0, 'af': 1},
		{'num': 32,  'name': 'statement',             			'code': [59],       		'at': 1, 'af': 0},

		{'num': 33,  'name': 'statement',             			'code': [407],      		'at': 0, 'af': 1},
		{'num': 34,  'name': 'statement',             			'code': [-42],      		'at': 0, 'af': 1},
		{'num': 35,  'name': 'statement',             			'code': [59],       		'at': 1, 'af': 0},

		{'num': 36,  'name': 'statement',             			'code': [408],       		'at': 0, 'af': 1},
		{'num': 37,  'name': 'statement',             			'code': [59],       		'at': 1, 'af': 0},

		{'num': 38,  'name': 'statement',             			'code': [59],       		'at': 1, 'af': 0},

		{'num': 39,  'name': 'statement',             			'code': [302],       		'at': 0, 'af': 1},
		{'num': 40,  'name': 'statement',             			'code': [54],       		'at': 0, 'af': 1},
		{'num': 41,  'name': 'statement',             			'code': [303],       		'at': 1, 'af': 1},

		{'num': 42,  'name': 'unsigned-integer',      			'code': [range(500,600)],   'at': 1, 'af': 1},
		{'num': 43,  'name': 'variable-identifier',         	'code': [-45],       		'at': 1, 'af': 1},
		{'num': 44,  'name': 'procedure-identifier',     		'code': [-45],       		'at': 1, 'af': 1},
		{'num': 45,  'name': 'identifier',       				'code': [range(1000,2000)], 'at': 1, 'af': 1},


		{'num': 46,  'name': 'actual-arguments',        		'code': [40],       		'at': 0, 'af': 1},
		{'num': 47,  'name': 'actual-arguments',        		'code': [-43],       		'at': 0, 'af': 1},
		{'num': 48,  'name': 'actual-arguments',        		'code': [-51],       		'at': 0, 'af': 1},
		{'num': 49,  'name': 'actual-arguments',        		'code': [41],       		'at': 1, 'af': 0},
		{'num': 50,  'name': 'actual-arguments',        		'code': [],       			'at': 1, 'af': 1},

		{'num': 51,  'name': 'actual-arguments-list',    		'code': [-43],       		'at': 0, 'af': 1},
		{'num': 52,  'name': 'actual-arguments-list',    		'code': [-51],       		'at': 1, 'af': 0},
		{'num': 53,  'name': 'actual-arguments-list',    		'code': [],       			'at': 1, 'af': 1},

		{'num': 54,  'name': 'assembly-insert-file-identifier', 'code': [-45],  			'at': 1, 'af': 0}
	]

    tree = Tree()
    stack = []
    stack.append(table[0])
    lxm_itr = 0
    direction = 1
    stage = {"at": 0, "af": 0}
    while stack:
        if direction == 1:
            if stack[len(stack)-1]['code'][0] < 0:
                stack.append(table[-1*stack[len(stack)-1]['code'][0]])
                tree.add(stack[len(stack)-1]['name'])
                direction = 1
                continue
            if stack[len(stack)-1]['code'][0] > 0:#and stack[len(stack)-1]['num'] < 140:
                if lexems[lxm_itr] in stack[len(stack)-1]['code']:
                    discription = ''
                    for key, word in dic_of_int_const.items():
                        if word == lexems[lxm_itr]:
                            discription = key
                    for key, word in dic_of_idents.items():
                        if word == lexems[lxm_itr]:
                            discription = key
                    for key, word in dic_of_complex_const.items():
                        if word == lexems[lxm_itr]:
                            discription = key
                    for key, word in dic_of_float_const.items():
                        if word == lexems[lxm_itr]:
                            discription = key
                    for key, word in key_words.items():
                        if word == lexems[lxm_itr]:
                            discription = key
                    for key, word in dm_dic.items():
                        if word == lexems[lxm_itr]:
                            discription = key
                    # print(lexems[lxm_itr], '-', discription)
                    tree.add(discription)
                    lxm_itr += 1
                    stage["at"] = 1
                    stage["af"] = 0
                else:
                    tree.add("error")
                    stage["at"] = 0
                    stage["af"] = 1
                direction = 0
                continue
            else:
                if lexems[lxm_itr] not in stack[len(stack)-1]['code']:
                    stage["at"] = 1
                    stage["af"] = 0
                    tree.add("empty")
                else:
                    tree.add("not empty")
                    stage["at"] = 0
                    stage["af"] = 1
                direction = 0
                continue
        else:
            if direction == 0:
                if stack[len(stack)-1]['code'][0] > 0:
                    #     return from stack up, stack pop and stack++
                    if stack[len(stack)-1]['at'] == 1 and stage["at"] == 1 and stack[len(stack)-1]['af'] == 0 and stage["af"] == 0:
                        stack.pop()
                        tree.current_element = tree.current_element.parent_element
                        direction = 0
                        continue
                    #     return from stack up
                    if stack[len(stack)-1]['at'] == 1 and stage["at"] == 1 and stack[len(stack)-1]['af'] == 1 and stage["af"] == 0:
                        stack.pop()
                        tree.current_element = tree.current_element.parent_element
                        direction = 0

                        continue
                    #     return error and stop process
                    if stack[len(stack)-1]['at'] == 1 and stage["at"] == 0 and stack[len(stack)-1]['af'] == 1 and stage["af"] == 1:
                        if len(stack) == 1:
                            print("Error!")
                            exit()
                        else:
                            stack.pop()
                            tree.current_element = tree.current_element.parent_element
                            direction = 0
                            continue
                    #     return error and stop process
                    if stack[len(stack)-1]['at'] == 0 and stage["at"] == 0 and stack[len(stack)-1]['af'] == 1 and stage["af"] == 1:
                        if len(stack) == 1:
                            print("Error!")
                            exit()
                        else:
                            stack.pop()
                            tree.current_element = tree.current_element.parent_element
                            direction = 0
                            continue
                    #     next line(stack++)
                    if stack[len(stack)-1]['at'] == 0 and stage["at"] == 1 and stack[len(stack)-1]['af'] == 1 and stage["af"] == 0:
                        index_table = stack[len(stack)-1]['num'] + 1
                        stack.pop()
                        tree.current_element = tree.current_element.parent_element
                        stack.append(table[index_table])
                        direction = 1
                        continue
                    #     next line(stack++)
                    if stack[len(stack)-1]['at'] == 1 and stage["at"] == 0 and stack[len(stack)-1]['af'] == 0 and stage["af"] == 1:
                        index_table = stack[len(stack)-1]['num'] + 1
                        stack.pop()
                        tmp_elem = tree.current_element
                        tree.current_element = tree.current_element.parent_element
                        tree.current_element.leaves.remove(tmp_elem)
                        stack.append(table[index_table])
                        tree.add(stack[len(stack)-1]['name'])
                        direction = 1
                        continue
                if stack[len(stack)-1]['code'][0] < 0:
                    #     return from stack up, stack pop and stack++
                    if stack[len(stack)-1]['at'] == 1 and stage["at"] == 1 and stack[len(stack)-1]['af'] == 0 and stage["af"] == 0:
                        stack.pop()
                        tree.current_element = tree.current_element.parent_element
                        direction = 0
                        continue
                    #     return from stack up
                    if stack[len(stack)-1]['at'] == 1 and stage["at"] == 1 and stack[len(stack)-1]['af'] == 1 and stage["af"] == 0:
                        stack.pop()
                        tree.current_element = tree.current_element.parent_element
                        direction = 0
                        continue
                    #     return error and stop process
                    if stack[len(stack)-1]['at'] == 1 and stage["at"] == 0 and stack[len(stack)-1]['af'] == 1 and stage["af"] == 1:
                        if len(stack) == 1:
                            print("Error!")
                            exit()
                        else:
                            stack.pop()
                            tree.current_element = tree.current_element.parent_element
                            direction = 0
                            continue
                    #     return error and stop process
                    if stack[len(stack)-1]['at'] == 0 and stage["at"] == 0 and stack[len(stack)-1]['af'] == 1 and stage["af"] == 1:
                        if len(stack) == 1:
                            print("Error!")
                            exit()
                        else:
                            stack.pop()
                            tree.current_element = tree.current_element.parent_element
                            direction = 0
                            continue
                    #     next line(stack++)
                    if stack[len(stack)-1]['at'] == 0 and stage["at"] == 1 and stack[len(stack)-1]['af'] == 1 and stage["af"] == 0:
                        index_table = stack[len(stack)-1]['num'] + 1
                        stack.pop()
                        tree.current_element = tree.current_element.parent_element
                        stack.append(table[index_table])
                        direction = 1
                        continue
                    #     next line(stack++)
                    if stack[len(stack)-1]['at'] == 1 and stage["at"] == 0 and stack[len(stack)-1]['af'] == 0 and stage["af"] == 1:
                        index_table = stack[len(stack)-1]['num'] + 1
                        stack.pop()
                        tmp_elem = tree.current_element
                        tree.current_element = tree.current_element.parent_element
                        tree.current_element.leaves.remove(tmp_elem)
                        stack.append(table[index_table])
                        tree.add(stack[len(stack)-1]['name'])
                        direction = 1
                        continue
    print('=========================================')
    tree.print_tree()
    print('=========================================')
    tree.listing()
    return tree


if __name__ == '__main__':
    syntax("Test.txt")
