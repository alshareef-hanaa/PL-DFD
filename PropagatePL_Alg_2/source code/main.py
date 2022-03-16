import sys
import xml.etree.ElementTree as ET
import csv
from signature_lexer import LexerSignatures
from ppf_lexer import LexerPPF
from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter


# First_Step: transform xml to csv
def xml_to_csv(xmlfile_DFD, csvfile_DFD):
    tree = ET.parse(xmlfile_DFD)
    root = tree.getroot()
    newsitems = []
    for subroot in root:
        for child in subroot:
            news = {}
            if int(child.attrib['id']) >= 2:
                news['id'] = int(child.attrib['id'])
                news['value'] = child.attrib['value']
                if child.attrib['style'].startswith("rounded=0"):
                    news['style'] = 'rounded=0'
                    news['source'] = 'null'
                    news['target'] = 'null'
                    news['type'] = 'external_entity'
                elif "doubleEllipse" in child.attrib['style']:
                    news['style'] = 'ellipse;shape=doubleEllipse'
                    news['source'] = 'null'
                    news['target'] = 'null'
                    news['type'] = 'composite_process'
                elif child.attrib['style'].startswith("ellipse"):
                    news['style'] = 'ellipse'
                    news['source'] = 'null'
                    news['target'] = 'null'
                    news['type'] = 'process'
                elif child.attrib['style'].startswith("shape"):
                    news['style'] = 'shape=partialRectangle'
                    news['source'] = 'null'
                    news['target'] = 'null'
                    news['type'] = 'data_base'
                elif child.attrib['style'].startswith("endArrow=classic"):
                    news['style'] = 'endArrow=classic'
                    news['source'] = child.attrib['source']
                    news['target'] = child.attrib['target']
                    news['type'] = 'endArrow=classic'
                    news['purposes'] = 'F'
                elif child.attrib['style'].startswith("endArrow=cross"):
                    news['style'] = 'endArrow=cross'
                    news['source'] = child.attrib['source']
                    news['target'] = child.attrib['target']
                    news['type'] = 'endArrow=cross'
                    news['purposes'] = 'F'
                newsitems.append(news)

    fields = ['id', 'value', 'purposes', 'style', 'source', 'target', 'type']
    with open(csvfile_DFD, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newsitems)


# this function changes the format of DFD from csv to list(dict)
def generate_dict_dfd(filename):
    data = csv.DictReader(open(filename))
    DFD_data_dict = []
    for row in data:
        DFD_data_dict.append(row)
    return DFD_data_dict


# this function changes the format of DFD from dic to nested dic
# where key is the id of each DFD element (activators and flows)
def generate_dfd_graph(original):
    output = {}
    for elem in original:
        output[elem['id']] = elem
    return output


# this function assigns type to each flow in DFD (that format as nested dic)
def get_data_flow_types(dfd_graph):
    for index, data_flow in dfd_graph.items():
        if data_flow['style'] == 'endArrow=classic':
            if dfd_graph[data_flow['source']]['style'] == 'rounded=0' and dfd_graph[data_flow['target']][
                'style'] == 'ellipse':
                dfd_graph[index]['type'] = 'in'
            if dfd_graph[data_flow['source']]['style'] == 'rounded=0' and dfd_graph[data_flow['target']][
                'style'] == 'ellipse;shape=doubleEllipse':
                dfd_graph[index]['type'] = 'inc'
            elif dfd_graph[data_flow['source']]['style'] == 'ellipse' and dfd_graph[data_flow['target']][
                'style'] == 'rounded=0':
                dfd_graph[index]['type'] = 'out'
            elif dfd_graph[data_flow['source']]['style'] == 'ellipse;shape=doubleEllipse' and \
                    dfd_graph[data_flow['target']]['style'] == 'rounded=0':
                dfd_graph[index]['type'] = 'outc'
            elif (dfd_graph[data_flow['source']]['style'] == 'ellipse' and dfd_graph[data_flow['target']][
                'style'] == 'ellipse'):
                dfd_graph[index]['type'] = 'comp'
            elif (dfd_graph[data_flow['source']]['style'] == 'ellipse;shape=doubleEllipse' and
                  dfd_graph[data_flow['target']]['style'] == 'ellipse;shape=doubleEllipse'):
                dfd_graph[index]['type'] = 'ccompc'
            elif (dfd_graph[data_flow['source']]['style'] == 'ellipse;shape=doubleEllipse' and
                  dfd_graph[data_flow['target']]['style'] == 'ellipse'):
                dfd_graph[index]['type'] = 'ccomp'
            elif (dfd_graph[data_flow['source']]['style'] == 'ellipse' and
                  dfd_graph[data_flow['target']]['style'] == 'ellipse;shape=doubleEllipse'):
                dfd_graph[index]['type'] = 'compc'
            elif dfd_graph[data_flow['source']]['style'] == 'ellipse' and dfd_graph[data_flow['target']][
                'style'] == 'shape=partialRectangle':
                dfd_graph[index]['type'] = 'store'
            elif dfd_graph[data_flow['source']]['style'] == 'ellipse;shape=doubleEllipse' and \
                    dfd_graph[data_flow['target']][
                        'style'] == 'shape=partialRectangle':
                dfd_graph[index]['type'] = 'cstore'
            elif dfd_graph[data_flow['source']]['style'] == 'shape=partialRectangle' and dfd_graph[data_flow['target']][
                'style'] == 'ellipse':
                dfd_graph[index]['type'] = 'read'
            elif dfd_graph[data_flow['source']]['style'] == 'shape=partialRectangle' and dfd_graph[data_flow['target']][
                'style'] == 'ellipse;shape=doubleEllipse':
                dfd_graph[index]['type'] = 'cread'
            if data_flow['style'] == 'endArrow=cross':
                if dfd_graph[data_flow['source']]['style'] == 'ellipse' and dfd_graph[data_flow['target']][
                    'style'] == 'shape=partialRectangle':
                    dfd_graph[index]['type'] = 'delete'
                elif dfd_graph[data_flow['source']]['style'] == 'ellipse;shape=doubleEllipse' and \
                        dfd_graph[data_flow['target']]['style'] == 'shape=partialRectangle':
                    dfd_graph[index]['type'] = 'cdelete'

    typed_dfd_dic = []
    for index, element in dfd_graph.items():
        typed_dfd_dic.append(element)
    return typed_dfd_dic


# this function changes the format of signatures from csv to list(dict)
def generate_dict_signatures(filename):
    data = csv.DictReader(open(filename))
    signatures = []
    for row in data:
        signatures.append(row)
    return signatures


# this function changes the format of ppfs from csv to list(dict)
def generate_dict_ppfs(filename):
    data = csv.DictReader(open(filename))
    ppfs_dict = []
    for row in data:
        ppfs_dict.append(row)
    return ppfs_dict


# this function creates list of basic purposes form csv file
def generate_list_purposes(filename):
    data = open(filename, 'r')
    file = csv.reader(data)
    purposes_list = []
    for raw in file:
        purposes_list.append(raw[0])
    return purposes_list


# for each node (ex, pro, db) get list of node's input flows and output flows
def node_i_o_flows(node_id, DFD_data_dict):
    node_inputs = list()
    node_outputs = list()
    node_types = ['external_entity', 'composite_process', 'process', 'data_base']
    for element in DFD_data_dict:
        if element['type'] not in node_types:
            if element['target'] == node_id:
                node_inputs.append(element)
            elif element['source'] == node_id:
                node_outputs.append(element)
    return node_inputs, node_outputs


def corresponding_ppf(signature_name, ppfs):
    ppf = any
    for item in ppfs:
        if item['function_name'] == signature_name:
            ppf = item
            break
    return ppf


def raise_error_num_inputs():
    raise Exception("Invalid number of inputs in the signature")


def reformatting_signatures_dict(typed_dfd_dic, signatures_dict):
    reformat_signatures_dict = []
    # print(signatures_dict)
    for sig in signatures_dict:
        lexer = LexerSignatures(sig['privacy_signature'])
        signature_dict = lexer.generate_signature_dict()
        # get sig inputs -> [id, id ]
        node_value = sig['element_name']
        node_id = [element['id'] for element in typed_dfd_dic if element['value'] == node_value][0]
        node_inputs, node_outputs = node_i_o_flows(node_id, typed_dfd_dic)
        if signature_dict['signature_inputs'][0] != ' ':
            for i in range(len(signature_dict['signature_inputs'])):
                for item in node_inputs:
                    # TODO: what if a node has two or more output flows that carry the same label/value
                    if item['value'] == signature_dict['signature_inputs'][i]:
                        signature_dict['signature_inputs'][i] = item['id']
                        break
        # get sig output -> id
        if signature_dict['signature_output'] != ' ':
            for item in node_outputs:
                # TODO: what if a node has two or more output flows that carry the same label/value
                if item['value'] == signature_dict['signature_output']:
                    signature_dict['signature_output'] = item['id']
                    break
        reformat_signatures_dict.append(signature_dict)
    return reformat_signatures_dict


def propagate_pur(list_flows, ref_signatures_dict, ppfs_dict):
    iteration = []
    for element in list_flows:
        assigned_sing = [x for x in ref_signatures_dict if x['signature_output'] == element['id']][0]
        # get def of assigned_sing
        ppf = corresponding_ppf(assigned_sing['signature_name'], ppfs_dict)
        # check if def of the assigned_sing of type "sing()(output)"
        if assigned_sing['signature_inputs'][0] == ' ':
            flow = element.copy()
            new_purpose = {'purposes': ppf['def']}
            flow.update(new_purpose)
            iteration.append(flow)
        elif ppf['def'] == '':
            input_flow_pur = next((x for x in iteration if x['id'] == assigned_sing['signature_inputs'][0]), None)
            if input_flow_pur == None:
                input_flow_pur = [x for x in list_flows if x['id'] == assigned_sing['signature_inputs'][0]][0]
            flow = element.copy()
            new_purpose = {'purposes': input_flow_pur['purposes']}
            flow.update(new_purpose)
            iteration.append(flow)
        else:
            # checking if # of ppf inputs == # sig inputs
            if int(ppf['input_number']) != len(assigned_sing['signature_inputs']):
                raise_error_num_inputs()
            lexer = LexerPPF(ppf['def'])
            def_inputs = []
            # get purpose of each input flow
            for i in range(len(assigned_sing['signature_inputs'])):
                input_flow = next((x for x in iteration if x['id'] == assigned_sing['signature_inputs'][i]), None)
                if input_flow == None:
                    input_flow = [x for x in list_flows if x['id'] == assigned_sing['signature_inputs'][i]][0]
                def_inputs.append(input_flow['purposes'])
            formula = lexer.generate_formula(def_inputs)
            flow = element.copy()
            new_purpose = {'purposes': formula}
            flow.update(new_purpose)
            iteration.append(flow)
    return iteration


def get_dfd_flows(typed_dfd_dic):
    dfd_flows = []
    node_types = ['composite_process', 'process', 'data_base', 'external_entity']
    for element in typed_dfd_dic:
        if element['type'] not in node_types:
            dfd_flows.append(element)
    return dfd_flows


# steps: get flows of all DFD for every flow
dfd_xml_filename = sys.argv[1]
dfd_csv_filename = sys.argv[2]
signatures_csv_filename = sys.argv[3]
ppfs_csv_filename = sys.argv[4]
basic_purposes_csv_filename = sys.argv[5]
result_csv_filename = sys.argv[6]
xml_to_csv(dfd_xml_filename, dfd_csv_filename)
DFD_data_dict = generate_dict_dfd(dfd_csv_filename)
dfd_nested_dic = generate_dfd_graph(DFD_data_dict)
typed_dfd_dic = get_data_flow_types(dfd_nested_dic)
signatures_dict = generate_dict_signatures(signatures_csv_filename)
ref_signatures_dict = reformatting_signatures_dict(typed_dfd_dic, signatures_dict)
ppfs_dict = generate_dict_ppfs(ppfs_csv_filename)
basic_purposes = generate_list_purposes(basic_purposes_csv_filename)

dfd_flows = get_dfd_flows(typed_dfd_dic)
result = propagate_pur(dfd_flows, ref_signatures_dict, ppfs_dict)
while dfd_flows != result:
    dfd_flows = result
    result = propagate_pur(result, ref_signatures_dict, ppfs_dict)

# evaluate the purpose expression
for flows in result:
    lexer = Lexer(flows['purposes'])
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    interpreter = Interpreter()
    value = interpreter.visit(tree, basic_purposes)
    new_purpose = {'purposes': value}
    flows.update(new_purpose)


# for presentation
# get the name of 'source' and 'target' nodes
def naming_t_s_nodes(result, DFD_data_dict):
    for flow in result:
        source_name = [element['value'] for element in DFD_data_dict if element['id'] == flow['source']][0]
        target_name = [element['value'] for element in DFD_data_dict if element['id'] == flow['target']][0]
        names = {'source': source_name, 'target': target_name}
        flow.update(names)

naming_t_s_nodes(result,DFD_data_dict)

# get the result on CSV file
columns = ['value', 'purposes', 'source', 'target']

with open(result_csv_filename, "w") as File:
    csvwriter = csv.DictWriter(File, fieldnames=columns, restval="NA", extrasaction='ignore')
    csvwriter.writeheader()  # write header
    csvwriter.writerows(result)

