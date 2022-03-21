import sys
import xml.etree.ElementTree as ET
import csv
from signature_lexer import LexerSignatures
# from ppf_lexer import LexerPPF
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


# this function changes the format of signatures from csv to list(dict)
def generate_dict_assigned_sigs(filename):
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
def generate_set_Bpur(filename):
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


def get_dfd_flows(typed_dfd_dic):
    dfd_flows = []
    node_types = ['composite_process', 'process', 'data_base', 'external_entity']
    for element in typed_dfd_dic:
        if element['type'] not in node_types:
            dfd_flows.append(element)
    return dfd_flows


def flow_sing_info(typed_dfd_dic, ref_signatures_dict, map_sig_tree):
    for flow in typed_dfd_dic:
        assigned_sing = [x for x in ref_signatures_dict if x['signature_output'] == flow['id']][0]
        sig_tree = map_sig_tree.get(assigned_sing['signature_name'])
        sig_info = {'purposes': set(), 'sig_name': assigned_sing['signature_name'],
                    'sig_inputs': assigned_sing['signature_inputs'], 'sig_tree': sig_tree}
        flow.update(sig_info)


def generate_env(flows_dict):
    # Env: flow's id/Var -> Val (env dict)
    env = dict()
    for flow in flows_dict:
        purposes = flow['purposes']
        env.update({flow['id']: purposes})
    return env


def propaget_pur_expr(flows_dict):
    env = generate_env(flows_dict)
    iteration = []
    for element in flows_dict:
        computed_purposes = set()
        # eval the tree based on assigned sig inputs
        if element['sig_tree'] != None:
            sig_inputs = element['sig_inputs'].copy()
            interpreter = Interpreter()
            computed_purposes = interpreter.visit(element['sig_tree'], env, basic_purposes,sig_inputs)
        else:
            # in case of none means we forward input's purposes label to the output
            computed_purposes = env.get(element['sig_inputs'][0])
        flow = element.copy()
        new_purpose = {'purposes': computed_purposes}
        flow.update(new_purpose)
        iteration.append(flow)
        # update env with new change
        new_value = {element['id']: computed_purposes}
        env.update(new_value)
    return iteration


# steps: get flows of all DFD for every flow
dfd_xml_filename = sys.argv[1]
dfd_csv_filename = sys.argv[2]
signatures_csv_filename = sys.argv[3]
ppfs_csv_filename = sys.argv[4]
basic_purposes_csv_filename = sys.argv[5]
result_csv_filename = sys.argv[6]
xml_to_csv(dfd_xml_filename, dfd_csv_filename)
DFD_data_dict = generate_dict_dfd(dfd_csv_filename)
# print(DFD_data_dict)
signatures_dict = generate_dict_assigned_sigs(signatures_csv_filename)
ref_signatures_dict = reformatting_signatures_dict(DFD_data_dict, signatures_dict)
# print(ref_signatures_dict)
ppfs_dict = generate_dict_ppfs(ppfs_csv_filename)
# print(ppfs_dict)
map_sig_tree = parser_sigs_expr(ppfs_dict)
# print(sigs_with_exprs_dict)
basic_purposes = generate_set_Bpur(basic_purposes_csv_filename)
# print(basic_purposes)

dfd_flows = get_dfd_flows(DFD_data_dict)
flow_sing_info(dfd_flows, ref_signatures_dict, map_sig_tree)
result = propaget_pur_expr(dfd_flows)
while dfd_flows != result:
    dfd_flows = result
    result = propaget_pur_expr(result)

# for presentation
# get the name of 'source' and 'target' nodes
def naming_t_s_nodes(result, DFD_data_dict):
    for flow in result:
        source_name = [element['value'] for element in DFD_data_dict if element['id'] == flow['source']][0]
        target_name = [element['value'] for element in DFD_data_dict if element['id'] == flow['target']][0]
        names = {'source': source_name, 'target': target_name}
        flow.update(names)

naming_t_s_nodes(result,DFD_data_dict)
#
# get the result on CSV file
columns = ['value', 'purposes', 'source', 'target']

with open(result_csv_filename, "w") as File:
    csvwriter = csv.DictWriter(File, fieldnames=columns, restval="NA", extrasaction='ignore')
    csvwriter.writeheader()  # write header
    csvwriter.writerows(result)

