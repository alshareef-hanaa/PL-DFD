import sys
import xml.etree.ElementTree as ET
import csv
from value_lexer import LexerValue
from signature_lexer import LexerSignatures
# from ppf_lexer import LexerPPF
from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

node_types = ['external_entity', 'composite_process', 'process', 'data_base']


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
                if child.attrib['style'].startswith("rounded=0"):
                    news['value'] = child.attrib['value']
                    news['style'] = 'rounded=0'
                    news['source'] = 'null'
                    news['target'] = 'null'
                    news['type'] = 'external_entity'
                elif "doubleEllipse" in child.attrib['style']:
                    news['value'] = child.attrib['value']
                    news['style'] = 'ellipse;shape=doubleEllipse'
                    news['source'] = 'null'
                    news['target'] = 'null'
                    news['type'] = 'composite_process'
                elif child.attrib['style'].startswith("ellipse"):
                    news['value'] = child.attrib['value']
                    news['style'] = 'ellipse'
                    news['source'] = 'null'
                    news['target'] = 'null'
                    news['type'] = 'process'
                elif child.attrib['style'].startswith("shape"):
                    news['value'] = child.attrib['value']
                    news['style'] = 'shape=partialRectangle'
                    news['source'] = 'null'
                    news['target'] = 'null'
                    news['type'] = 'data_base'
                elif child.attrib['style'].startswith("endArrow=classic"):
                    news['style'] = 'endArrow=classic'
                    news['source'] = child.attrib['source']
                    news['target'] = child.attrib['target']
                    news['type'] = 'endArrow=classic'
                    text = child.attrib['value']
                    lexer = LexerValue(text)
                    tokens = lexer.generate_value_tokens()
                    list_tokens = list(tokens)
                    news['value'] = list_tokens[0]
                    news['purposes'] = list_tokens[1]
                elif child.attrib['style'].startswith("endArrow=cross"):
                    news['style'] = 'endArrow=cross'
                    news['source'] = child.attrib['source']
                    news['target'] = child.attrib['target']
                    news['type'] = 'endArrow=cross'
                    text = child.attrib['value']
                    lexer = LexerValue(text)
                    tokens = lexer.generate_value_tokens()
                    list_tokens = list(tokens)
                    news['value'] = list_tokens[0]
                    news['purposes'] = list_tokens[1]
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


# this function changes the format of signatures from csv to list(dict)
def generate_dict_assigned_sigs(filename):
    data = csv.DictReader(open(filename))
    signatures = []
    for row in data:
        signatures.append(row)
    return signatures


# this function creates list of basic purposes form csv file
def generate_set_Bpur(filename):
    data = open(filename, 'r')
    file = csv.reader(data)
    purposes_list = []
    for raw in file:
        purposes_list.append(raw[0])
    return set(purposes_list[0].split(';'))


# for each node (ex, pro, db) get list of node's input and output flows
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


def corresponding_signature(node, signatures):
    # TODO: checks that number of signatures on node_sigs list is == to
    #  node's output flows
    node_sigs = list()
    for item in signatures:
        if item['element_name'] == node:
            node_sigs.append(item['privacy_signature'])
    return node_sigs


# this function changes the format of sigs with exprs fil from csv to list(dict)
def generate_dict_sigs_with_exprs(filename):
    data = csv.DictReader(open(filename))
    sigs_with_exprs = []
    for row in data:
        sigs_with_exprs.append(row)
    return sigs_with_exprs


def generate_env(dfd_data):
    # Env: flow's id/Var -> Val (env dict)
    env = dict()
    for flow in dfd_data:
        if flow['type'] not in node_types:
            purposes = set(flow['purposes'].split(','))
            env.update({flow['id']: purposes})
    return env


# this function to get sig's expr as dict {sig_name : expr/tree}
def parser_sigs_expr(sigs_with_exprs_dict):
    sigs_expr = {}
    for sig in sigs_with_exprs_dict:
        if sig['def'] != '':
            lexer = Lexer(sig['def'])
            tokens = lexer.generate_tokens()
            parser = Parser(tokens)
            tree = parser.parse()
            sig_name_expr = {sig['function_name']: tree}
            sigs_expr.update(sig_name_expr)
        else:
            sig_name_expr = {sig['function_name']: None}
            sigs_expr.update(sig_name_expr)
    return sigs_expr


def flow_sing_info(DFD_dict, assigned_sigs_dict):
    for element in DFD_dict:
        if element['type'] in node_types:
            node_inputs, node_outputs = node_i_o_flows(element['id'], DFD_dict)
            signatures = corresponding_signature(element['value'], assigned_sigs_dict)
            for sig in signatures:
                lexer = LexerSignatures(sig)
                signature_dict = lexer.generate_signature_dict()
                # get sig inputs -> id
                signature_inputs = signature_dict['signature_inputs']
                if signature_inputs[0] != ' ':
                    for i in range(len(signature_inputs)):
                        for item in node_inputs:
                            # TODO: what if a node has two or more output flows that carry the same label/value
                            if item['value'] == signature_inputs[i]:
                                signature_inputs[i] = item['id']
                                break
                # find output flow of this sig and update it with sig info
                signature_output = signature_dict['signature_output']
                for item in node_outputs:
                    if item['value'] == signature_output:
                        flow = [x for x in DFD_dict if x['id'] == item['id']][0]
                        sig_info = {'sig_name': signature_dict['signature_name'], 'sig_inputs': signature_inputs}
                        flow.update(sig_info)
                        break


def check_compatibility(DFD_dict, map_sig_tree, basic_purposes):
    env = generate_env(DFD_dict)
    for element in DFD_dict:
        if element['type'] not in node_types:
            computed_purposes = set()
            # get the tree of assigned sig
            tree_assigned_sig = map_sig_tree.get(element['sig_name'])
            # eval the tree based on assigned sig inputs
            if tree_assigned_sig != None:
                interpreter = Interpreter()
                computed_purposes = interpreter.visit(tree_assigned_sig, env, basic_purposes, element['sig_inputs'])
            else:
                # in case of none means we forward input's purposes label to the output
                computed_purposes = env.get(element['sig_inputs'][0])
                # sig_input_flow = [x for x in DFD_dict if x['id'] == element['sig_inputs'][0]][0]
            # get labeled purposes and compare
            if element['purposes'] != '':
                labeled_purposes = set(element['purposes'].split(','))
            else:
                labeled_purposes = set()
            compatibility_result = labeled_purposes.issubset(computed_purposes)
            result = {'computed_purposes': computed_purposes, 'compatibility_result': compatibility_result}
            element.update(result)


# set the 5 files
dfd_xml_filename = sys.argv[1]
dfd_csv_filename = sys.argv[2]
assigned_sigs_csv_filename = sys.argv[3]
sigs_exprs_csv_filename = sys.argv[4]
Bpurs_csv_filename = sys.argv[5]
result_csv_filename = sys.argv[6]
xml_to_csv(dfd_xml_filename, dfd_csv_filename)
DFD_data_dict = generate_dict_dfd(dfd_csv_filename)
assigned_sigs_dict = generate_dict_assigned_sigs(assigned_sigs_csv_filename)
sigs_with_exprs_dict = generate_dict_sigs_with_exprs(sigs_exprs_csv_filename)
basic_purposes = generate_set_Bpur(Bpurs_csv_filename)
map_sig_tree = parser_sigs_expr(sigs_with_exprs_dict)
flow_sing_info(DFD_data_dict, assigned_sigs_dict)
check_compatibility(DFD_data_dict, map_sig_tree, basic_purposes)


# -----------------for presentation-----------------
flows_DFD_result = []
for element in DFD_data_dict:
    if element['type'] not in node_types:
        flows_DFD_result.append(element)

# get the name of 'source' and 'target' nodes
def naming_t_s_nodes(flows_DFD_result, DFD_data_dict):
    for flow in flows_DFD_result:
        source_name = [element['value'] for element in DFD_data_dict if element['id'] == flow['source']][0]
        target_name = [element['value'] for element in DFD_data_dict if element['id'] == flow['target']][0]
        names = {'source': source_name, 'target': target_name}
        flow.update(names)


naming_t_s_nodes(flows_DFD_result, DFD_data_dict)

# result of checking on csv
columns = ['value', 'purposes', 'source', 'target', 'computed_purposes', 'compatibility_result']
with open(result_csv_filename, "w") as File:
    csvwriter = csv.DictWriter(File, fieldnames=columns, restval="NA", extrasaction='ignore')
    csvwriter.writeheader()  # write header
    csvwriter.writerows(flows_DFD_result)
