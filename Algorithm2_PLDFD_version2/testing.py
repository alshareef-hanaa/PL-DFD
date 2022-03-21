# typed_dfd_nested_dic =  {'2': {'id': '2', 'value': 'EX1', 'purposes': '', 'style': 'rounded=0', 'source': 'null', 'target': 'null',
#            'type': 'external_entity'},
#      '3': {'id': '3', 'value': 'flow one(add)', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '2',
#            'target': '4',
#            'type': 'in'},
#      '4': {'id': '4', 'value': 'proc1', 'purposes': '', 'style': 'ellipse', 'source': 'null', 'target': 'null',
#            'type': 'process'},
#      '5': {'id': '5', 'value': 'flow two(log,add)', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '2',
#            'target': '4', 'type': 'in'},
#      '6': {'id': '6', 'value': 'flow three(log)', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '4',
#            'target': '7', 'type': 'out'},
#      '7': {'id': '7', 'value': 'EX2', 'purposes': '', 'style': 'rounded=0', 'source': 'null', 'target': 'null',
#            'type': 'external_entity'}}
#
# typed_dfd_dic = []
#
# for index, element in typed_dfd_nested_dic.items():
#     typed_dfd_dic.append(element)
#
# print(typed_dfd_dic)
# def update_func(list, u):
#     hanaa = []
#     for item in list:
#         if item['p'] == '1':
#             newelement = item.copy()
#             newelement['p'] = int(newelement['p']) + u
#             hanaa.append(newelement)
#     return hanaa


# # list1 = [{'1':'1'}, {'2':'2'}, {'':''}]
# u = 2
# orgnail = [{'p': '1'}, {'p': '2'}, {'p': '3'}]
# print(orgnail)
# # j = update_func(orgnail)
# # print(j)
# # print(orgnail)
# result = []
# while True:
#     result = update_func(orgnail, u)
#     if result == orgnail:
#         break
#     else:
#         orgnail = result
#
# print(result)

# u = 2
# i = [1, 2, 3]
# while True:
#     j = update_func(i, u)
#     if i != j:
#         u -= 1
#         i != j:
#     i = j


# list1 = [{'1':'1'}, {'2':'2'}, {'':''}]
# u = 2
# i = [1, 2, 3]
# while True:
#     j = update_func(i, u)
#     if i != j:
#         u -= 1
#         i != j:
#     i = j

# # list1 = [{'1':'1'}, {'2':'2'}, {'':''}]
# list1 = [1, 2, 3]
# a = True
# while :
#     list2 = update_func(list1)
#     if list2 != list1:
#         list1 = list2
#         a = True
#     else:
#         a = False


#
# list = [{'id': '2', 'value': 'EX1', 'purposes': '', 'style': 'rounded=0', 'source': 'null', 'target': 'null',
#          'type': 'external_entity'},
#         {'id': '3', 'value': 'flow one(add)', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '2',
#          'target': '4',
#          'type': 'in'},
#         {'id': '4', 'value': 'proc1', 'purposes': '', 'style': 'ellipse', 'source': 'null', 'target': 'null',
#          'type': 'process'},
#         {'id': '5', 'value': 'flow two(log,add)', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '2',
#          'target': '4',
#          'type': 'in'},
#         {'id': '6', 'value': 'flow three(log)', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '4',
#          'target': '7',
#          'type': 'out'},
#         {'id': '7', 'value': 'EX2', 'purposes': '', 'style': 'rounded=0', 'source': 'null', 'target': 'null',
#          'type': 'external_entity'}]
# a_key = "value"
# value = 'EX1'
# values_of_key = [a_dict['id'] for a_dict in list if a_dict[a_key] == value][0]
#
# print(values_of_key)

list = [{'signature_name': 'sign1', 'signature_inputs': [' '], 'signature_output': 'FLOW1'},
        {'signature_name': 'sign2', 'signature_inputs': [' '], 'signature_output': 'FLOW2'},
        {'signature_name': 'sign3', 'signature_inputs': ['FLOW1', 'FLOW2'], 'signature_output': 'FLOW3'},
        {'signature_name': 'sign4', 'signature_inputs': ['FLOW3'], 'signature_output': 'FLOW4'}]

ppfs_dict = [{'function_name': 'sign1', 'input_number': '1', 'def': 'p'},
             {'function_name': 'sign2', 'input_number': '1', 'def': 'q'},
             {'function_name': 'sign3', 'input_number': '2', 'def': '#1|#2'},
             {'function_name': 'sign4', 'input_number': '1', 'def': ''}]

# list1 = [' ']
# if (list1[0]) == ' ':
#     print(type(list1[0]))
# for i in ppfs_dict:
#     if i['def'] == '':
#         print("empty def")
#
# signs = [{'signature_name': 'sign1', 'signature_inputs': [' '], 'signature_output': {'7': 'F'}},
#          {'signature_name': 'sign2', 'signature_inputs': [' '], 'signature_output': {'8': 'F'}},
#          {'signature_name': 'sign3', 'signature_inputs': [{'7': 'F'}, {'8': 'F'}], 'signature_output': {'9': 'F'}},
#          {'signature_name': 'sign4', 'signature_inputs': [{'9': 'F'}], 'signature_output': {'10': 'F'}}]
# sing = {'signature_name': 'sign3', 'signature_inputs': [{'7': 'F'}, {'8': 'F'}], 'signature_output': {'9': 'F'}}
# signature_inputs =
# values_of_key = [a_dict[signature_inputs] for a_dict in signs]
dfd_elements = [{'id': '2', 'value': 'EX1', 'purposes': '', 'style': 'rounded=0', 'source': 'null', 'target': 'null',
                 'type': 'external_entity'},
                {'id': '3', 'value': 'EX2', 'purposes': '', 'style': 'rounded=0', 'source': 'null', 'target': 'null',
                 'type': 'external_entity'},
                {'id': '4', 'value': 'proc1', 'purposes': '', 'style': 'ellipse', 'source': 'null', 'target': 'null',
                 'type': 'process'},
                {'id': '5', 'value': 'EX3', 'purposes': '', 'style': 'rounded=0', 'source': 'null', 'target': 'null',
                 'type': 'external_entity'},
                {'id': '6', 'value': 'proc2', 'purposes': '', 'style': 'ellipse', 'source': 'null', 'target': 'null',
                 'type': 'process'},
                {'id': '7', 'value': 'FLOW1', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '2',
                 'target': '4',
                 'type': 'in'},
                {'id': '8', 'value': 'FLOW2', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '3',
                 'target': '4',
                 'type': 'in'},
                {'id': '9', 'value': 'FLOW3', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '4',
                 'target': '6',
                 'type': 'comp'},
                {'id': '10', 'value': 'FLOW4', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '6',
                 'target': '5',
                 'type': 'out'}]
result = [{'id': '9', 'value': 'FLOW3', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '4',
           'target': '6',
           'type': 'comp'}]
signs = [{'signature_name': 'sign1', 'signature_inputs': [' '], 'signature_output': '7'},
         {'signature_name': 'sign2', 'signature_inputs': [' '], 'signature_output': '8'},
         {'signature_name': 'sign3', 'signature_inputs': ['7', '8'], 'signature_output': '9'},
         {'signature_name': 'sign4', 'signature_inputs': ['9'], 'signature_output': '10'}]
# assigned_sing = {'signature_name': 'sign4', 'signature_inputs': ['9'], 'signature_output': '10'}
# flow = next((x for x in result if x['id'] == assigned_sing['signature_inputs'][0]), None)
# if flow == None:
#     flow = [x for x in dfd_elements if x['id'] == assigned_sing['signature_inputs'][0]][0]
# print(flow)

# value = 'T'
# result = []
# node_types = ['composite_process', 'process', 'data_base', 'external_entity']
# for element in dfd_elements:
#     if element['type'] not in node_types:
#         flow = element
#         new_purpose = {'process': value}
#         flow.update(new_purpose)
#         result.append(flow)

# result[element['id']]['purposes'].append(value)

# def_input = []
# sing = [x for x in signs if x['signature_output'] == '9'][0]
# for i in range(len(sing['signature_inputs'])):
#     # i_purpose = [x for x in result if x['id'] == sing['signature_inputs'][i]][0]
#     i_purpose = next((x for x in result if x['id'] == sing['signature_inputs'][i]), None)
#     if i_purpose == None:
#         i_purpose = [x for x in dfd_elements if x['id'] == sing['signature_inputs'][i]][0]
#     def_input.append(i_purpose['purposes'])
# print(def_input)


# (next( j for j, x in enumerate(result) if x['id'] == sing['signature_inputs'][i]), None))
# sing = [x for x in signs if x['signature_output'] == '10'][0]
# print(sing)
# element = [{'id': '10', 'value': 'FLOW4', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '6',
#             'target': '5',
#             'type': 'out'}]
# print(element[0]['purposes'])

# lstdict = [
#         { "name": "Klaus", "age": 32 },
#         { "name": "Elijah", "age": 33 },
#         { "name": "Kol", "age": 28 },
#         { "name": "Stefan", "age": 8 }
#        ]
# purpose= next((x for x in lstdict if x["name"] == "hanaa"), None)
# # purpose= [x for x in lstdict if x['name'] == 'hanaa'][0]
# print (type(purpose))

# comparing 2 lists of dicts

list_dict_1 = [{'id': '9', 'value': 'FLOW3', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '4', 'target': '6',
                'type': 'comp'},
               {'id': '10', 'value': 'FLOW4', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '6',
                'target': '5',
                'type': 'out'},
               {'id': '8', 'value': 'FLOW2', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '3', 'target': '4',
                'type': 'in'},
               {'id': '7', 'value': 'FLOW1', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '2', 'target': '4',
                'type': 'in'}]
list_dict_2 = [
    {'id': '9', 'value': 'FLOW3', 'purposes': 'F|F', 'style': 'endArrow=classic', 'source': '4', 'target': '6',
     'type': 'comp'},
    {'id': '10', 'value': 'FLOW4', 'purposes': 'F|F', 'style': 'endArrow=classic', 'source': '6', 'target': '5',
     'type': 'out'},
    {'id': '8', 'value': 'FLOW2', 'purposes': 'add', 'style': 'endArrow=classic', 'source': '3', 'target': '4',
     'type': 'in'},
    {'id': '7', 'value': 'FLOW1', 'purposes': 'log', 'style': 'endArrow=classic', 'source': '2', 'target': '4',
     'type': 'in'}]
list_dict_3 = [
    {'id': '9', 'value': 'FLOW3', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '4', 'target': '6',
     'type': 'comp'},
    {'id': '10', 'value': 'FLOW4', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '6', 'target': '5',
     'type': 'out'},
    {'id': '8', 'value': 'FLOW2', 'purposes': 'add', 'style': 'endArrow=classic', 'source': '3', 'target': '4',
     'type': 'in'},
    {'id': '7', 'value': 'FLOW1', 'purposes': 'log', 'style': 'endArrow=classic', 'source': '2', 'target': '4',
     'type': 'in'}]

list_dict_4 = [
    {'id': '9', 'value': 'FLOW3', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '4', 'target': '6',
     'type': 'comp'},
    {'id': '10', 'value': 'FLOW4', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '6', 'target': '5',
     'type': 'out'},
    {'id': '8', 'value': 'FLOW2', 'purposes': 'add', 'style': 'endArrow=classic', 'source': '3', 'target': '4',
     'type': 'in'},
    {'id': '7', 'value': 'FLOW1', 'purposes': 'log', 'style': 'endArrow=classic', 'source': '2', 'target': '4',
     'type': 'in'}]

# if list_dict_3 == list_dict_4:
#     print('yes')
# else:
#     print('no')
# [i for i in list_1 if i not in list_2] == []


# [{'id': '10', 'value': 'FLOW4', 'purposes': 'F', 'style': 'endArrow=classic', 'source': '6', 'target': '5', 'type': 'out'}, {'id': '9', 'value': 'FLOW3', 'purposes': 'F|F', 'style': 'endArrow=classic', 'source': '4', 'target': '6', 'type': 'comp'}, {'id': '8', 'value': 'FLOW2', 'purposes': 'add', 'style': 'endArrow=classic', 'source': '3', 'target': '4', 'type': 'in'}, {'id': '7', 'value': 'FLOW1', 'purposes': 'log', 'style': 'endArrow=classic', 'source': '2', 'target': '4', 'type': 'in'}]
# [{'id': '10', 'value': 'FLOW4', 'purposes': 'F|F', 'style': 'endArrow=classic', 'source': '6', 'target': '5', 'type': 'out'}, {'id': '9', 'value': 'FLOW3', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '4', 'target': '6', 'type': 'comp'}, {'id': '8', 'value': 'FLOW2', 'purposes': 'add', 'style': 'endArrow=classic', 'source': '3', 'target': '4', 'type': 'in'}, {'id': '7', 'value': 'FLOW1', 'purposes': 'log', 'style': 'endArrow=classic', 'source': '2', 'target': '4', 'type': 'in'}]
# [{'id': '10', 'value': 'FLOW4', 'purposes': 'F|F', 'style': 'endArrow=classic', 'source': '6', 'target': '5', 'type': 'out'}, {'id': '9', 'value': 'FLOW3', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '4', 'target': '6', 'type': 'comp'}, {'id': '8', 'value': 'FLOW2', 'purposes': 'add', 'style': 'endArrow=classic', 'source': '3', 'target': '4', 'type': 'in'}, {'id': '7', 'value': 'FLOW1', 'purposes': 'log', 'style': 'endArrow=classic', 'source': '2', 'target': '4', 'type': 'in'}]
# [{'id': '10', 'value': 'FLOW4', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '6', 'target': '5', 'type': 'out'}, {'id': '9', 'value': 'FLOW3', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '4', 'target': '6', 'type': 'comp'}, {'id': '8', 'value': 'FLOW2', 'purposes': 'add', 'style': 'endArrow=classic', 'source': '3', 'target': '4', 'type': 'in'}, {'id': '7', 'value': 'FLOW1', 'purposes': 'log', 'style': 'endArrow=classic', 'source': '2', 'target': '4', 'type': 'in'}]
# [{'id': '10', 'value': 'FLOW4', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '6', 'target': '5', 'type': 'out'}, {'id': '9', 'value': 'FLOW3', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '4', 'target': '6', 'type': 'comp'}, {'id': '8', 'value': 'FLOW2', 'purposes': 'add', 'style': 'endArrow=classic', 'source': '3', 'target': '4', 'type': 'in'}, {'id': '7', 'value': 'FLOW1', 'purposes': 'log', 'style': 'endArrow=classic', 'source': '2', 'target': '4', 'type': 'in'}]
# [{'id': '10', 'value': 'FLOW4', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '6', 'target': '5', 'type': 'out'}, {'id': '9', 'value': 'FLOW3', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '4', 'target': '6', 'type': 'comp'}, {'id': '8', 'value': 'FLOW2', 'purposes': 'add', 'style': 'endArrow=classic', 'source': '3', 'target': '4', 'type': 'in'}, {'id': '7', 'value': 'FLOW1', 'purposes': 'log', 'style': 'endArrow=classic', 'source': '2', 'target': '4', 'type': 'in'}]
# 4
#
# Process finished with exit code 0


test = [
    {'id': '7', 'value': 'FLOW1', 'purposes': 'log', 'style': 'endArrow=classic', 'source': 'EX1', 'target': 'proc1',
     'type': 'in'},
    {'id': '8', 'value': 'FLOW2', 'purposes': 'add', 'style': 'endArrow=classic', 'source': 'EX2', 'target': 'proc1',
     'type': 'in'},
    {'id': '9', 'value': 'FLOW3', 'purposes': {'log', 'add'}, 'style': 'endArrow=classic', 'source': 'proc1',
     'target': 'proc2', 'type': 'comp'},
    {'id': '10', 'value': 'FLOW4', 'purposes': {'log', 'add'}, 'style': 'endArrow=classic', 'source': 'proc2',
     'target': 'EX3', 'type': 'out'}]

# ------- updating result -------
# how to build env

test_update = [
    {'id': '9', 'value': 'FLOW3', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '4', 'target': '6',
     'type': 'comp', 'sig_name': 'sign3', 'sig_inputs': ['7', '8']},
    {'id': '7', 'value': 'FLOW1', 'purposes': 'log', 'style': 'endArrow=classic', 'source': '2', 'target': '4',
     'type': 'in', 'sig_name': 'sign1', 'sig_inputs': [' ']},
    {'id': '8', 'value': 'FLOW2', 'purposes': 'add', 'style': 'endArrow=classic', 'source': '3', 'target': '4',
     'type': 'in', 'sig_name': 'sign2', 'sig_inputs': [' ']},
    {'id': '10', 'value': 'FLOW4', 'purposes': 'log|add', 'style': 'endArrow=classic', 'source': '6', 'target': '5',
     'type': 'out', 'sig_name': 'sign4', 'sig_inputs': ['9']}]
# {'sign1': log, 'sign2': add, 'sign3': (#1|#2), 'sign4': None}


# def propagate_pur(list_flows, ref_signatures_dict, ppfs_dict):
#     iteration = []
#     for element in list_flows:
#         assigned_sing = [x for x in ref_signatures_dict if x['signature_output'] == element['id']][0]
#         # get def of assigned_sing
#         ppf = corresponding_ppf(assigned_sing['signature_name'], ppfs_dict)
#         # check if def of the assigned_sing of type "sing()(output)"
#         if assigned_sing['signature_inputs'][0] == ' ':
#             flow = element.copy()
#             new_purpose = {'purposes': ppf['def']}
#             flow.update(new_purpose)
#             iteration.append(flow)
#         elif ppf['def'] == '':
#             input_flow_pur = next((x for x in iteration if x['id'] == assigned_sing['signature_inputs'][0]), None)
#             if input_flow_pur == None:
#                 input_flow_pur = [x for x in list_flows if x['id'] == assigned_sing['signature_inputs'][0]][0]
#             flow = element.copy()
#             new_purpose = {'purposes': input_flow_pur['purposes']}
#             flow.update(new_purpose)
#             iteration.append(flow)
#         else:
#             # checking if # of ppf inputs == # sig inputs
#             if int(ppf['input_number']) != len(assigned_sing['signature_inputs']):
#                 raise_error_num_inputs()
#             lexer = LexerPPF(ppf['def'])
#             def_inputs = []
#             # get purpose of each input flow
#             for i in range(len(assigned_sing['signature_inputs'])):
#                 input_flow = next((x for x in iteration if x['id'] == assigned_sing['signature_inputs'][i]), None)
#                 if input_flow == None:
#                     input_flow = [x for x in list_flows if x['id'] == assigned_sing['signature_inputs'][i]][0]
#                 def_inputs.append(input_flow['purposes'])
#             formula = lexer.generate_formula(def_inputs)
#             flow = element.copy()
#             new_purpose = {'purposes': formula}
#             flow.update(new_purpose)
#             iteration.append(flow)
#     return iteration

# [{'id': '7', 'value': 'FLOW1', 'purposes': set(), 'style': 'endArrow=classic', 'source': '2', 'target': '4',
#   'type': 'endArrow=classic', 'sig_name': 'sign1', 'sig_inputs': [' '], 'sig_tree': log},
#  {'id': '8', 'value': 'FLOW2', 'purposes': set(), 'style': 'endArrow=classic', 'source': '3', 'target': '4',
#   'type': 'endArrow=classic', 'sig_name': 'sign2', 'sig_inputs': [' '], 'sig_tree': add},
#  {'id': '9', 'value': 'FLOW3', 'purposes': set(), 'style': 'endArrow=classic', 'source': '4', 'target': '6',
#   'type': 'endArrow=classic', 'sig_name': 'sign3', 'sig_inputs': ['7', '8'],
#   'sig_tree': (# 1|#2)}, {'id': '10', 'value': 'FLOW4', 'purposes': set(), 'style': 'endArrow=classic', 'source': '6', 'target': '5', 'type': 'endArrow=classic', 'sig_name': 'sign4', 'sig_inputs': ['9'], 'sig_tree': None}]
# {'sign1': log, 'sign2': add, 'sign3': (#1|#2), 'sign4': None}

element = [{'sig_inputs': ['7', '8']}]
for i in element:
    testtt = i['sig_inputs'].copy()
    testtt.pop(0)
    print(testtt)
print(element)

# ---------------- final result of test 1 (parser only sig's def)------
# [{'id': '7', 'value': 'FLOW1', 'purposes': set(), 'style': 'endArrow=classic', 'source': '2', 'target': '4',
#   'type': 'endArrow=classic', 'sig_name': 'sign1', 'sig_inputs': [' '], 'sig_tree': log},
#  {'id': '9', 'value': 'FLOW3', 'purposes': set(), 'style': 'endArrow=classic', 'source': '4', 'target': '6',
#   'type': 'endArrow=classic', 'sig_name': 'sign3', 'sig_inputs': ['7', '8'], 'sig_tree': (
#      # 1|#2)}, {'id': '8', 'value': 'FLOW2', 'purposes': set(), 'style': 'endArrow=classic', 'source': '3', 'target': '4', 'type': 'endArrow=classic', 'sig_name': 'sign2', 'sig_inputs': [' '], 'sig_tree': add}, {'id': '10', 'value': 'FLOW4', 'purposes': set(), 'style': 'endArrow=classic', 'source': '6', 'target': '5', 'type': 'endArrow=classic', 'sig_name': 'sign4', 'sig_inputs': ['9'], 'sig_tree': None}]
#      [{'id': '7', 'value': 'FLOW1', 'purposes': {'log'}, 'style': 'endArrow=classic', 'source': '2', 'target': '4',
#        'type': 'endArrow=classic', 'sig_name': 'sign1', 'sig_inputs': [' '], 'sig_tree': log},
#       {'id': '9', 'value': 'FLOW3', 'purposes': {'log'}, 'style': 'endArrow=classic', 'source': '4', 'target': '6',
#        'type': 'endArrow=classic', 'sig_name': 'sign3', 'sig_inputs': ['7', '8'], 'sig_tree': (
#           # 1|#2)}, {'id': '8', 'value': 'FLOW2', 'purposes': {'add'}, 'style': 'endArrow=classic', 'source': '3', 'target': '4', 'type': 'endArrow=classic', 'sig_name': 'sign2', 'sig_inputs': [' '], 'sig_tree': add}, {'id': '10', 'value': 'FLOW4', 'purposes': {'log'}, 'style': 'endArrow=classic', 'source': '6', 'target': '5', 'type': 'endArrow=classic', 'sig_name': 'sign4', 'sig_inputs': ['9'], 'sig_tree': None}]
#           # {'sign1': log, 'sign2': add, 'sign3': (#1|#2), 'sign4': None}
#           [{'id': '7', 'value': 'FLOW1', 'purposes': {'log'}, 'style': 'endArrow=classic', 'source': '2', 'target': '4',
#             'type': 'endArrow=classic', 'sig_name': 'sign1', 'sig_inputs': [' '], 'sig_tree': log},
#            {'id': '9', 'value': 'FLOW3', 'purposes': {'add', 'log'}, 'style': 'endArrow=classic', 'source': '4',
#             'target': '6', 'type': 'endArrow=classic', 'sig_name': 'sign3', 'sig_inputs': ['7', '8'],
#             'sig_tree': (  # 1|#2)}, {'id': '8', 'value': 'FLOW2', 'purposes': {'add'}, 'style': 'endArrow=classic', 'source': '3', 'target': '4', 'type': 'endArrow=classic', 'sig_name': 'sign2', 'sig_inputs': [' '], 'sig_tree': add}, {'id': '10', 'value': 'FLOW4', 'purposes': {'add', 'log'}, 'style': 'endArrow=classic', 'source': '6', 'target': '5', 'type': 'endArrow=classic', 'sig_name': 'sign4', 'sig_inputs': ['9'], 'sig_tree': None}]
