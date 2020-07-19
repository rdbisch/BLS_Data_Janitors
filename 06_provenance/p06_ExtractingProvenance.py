import clingo
import re
import os
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

workflow_rules = "upstream(X,Y) :- edge(X,Y)." \
                 "upstream(X,Y) :- edge(X,Z), upstream(Z,Y)." \
                 "downstream(X,Y) :- edge(Y,X)." \
                 "downstream(X,Y) :- edge(Y,Z), downstream(X,Z)." \
                 "parallel_step(X,Y) :- edge(Z,X), edge(Z,Y), step(X), step(Y), X<Y." \
                 "parallel_data(X,Y) :- edge(Z,X), edge(Z,Y), data(X), data(Y), X<Y." \
                 "upstream_data_type(X,Y) :- upstream(X,Y), data(X)." \
                 "upstream_step_type(X,Y) :- upstream(X,Y), step(X)." \
                 "downstream_data_type(X,Y) :- downstream(X,Y), data(X)." \
                 "downstream_step_type(X,Y) :- downstream(X,Y), step(X)."

def read_data(link):
    """
    reading the data and recording the edges in a dataframe
    :param link: link of the raw data
    :return: a dataframe of all edges and the types of their nodes
    """
    df = pd.read_csv(link, sep=', ', header = None, engine = 'python')
    data_and_step = pd.DataFrame(columns = ['Data', 'Step', 'Info'])
    data_and_step['Data'] = df[3].str.split(r"->|<-").str[1].str.replace('\'','')
    #results['Out'] = results['Out'].str.replace('>','')
    data_and_step['Step'] = df[3].str.split(r"->|<-").str[0].str.replace('\'','')
    data_and_step['Info'] = df[1].str.replace('\'','')
    data_and_step = data_and_step[~((data_and_step['Info'] == 'param'))]
    data_and_step = data_and_step.reset_index(drop = True)
    results = pd.DataFrame(columns = ['Out', 'Out_type', 'In', 'In_type'])
    results['Out'] = np.where(data_and_step['Info'] == 'out', data_and_step['Step'], data_and_step['Data'])
    results['In'] = np.where(data_and_step['Info'] == 'out', data_and_step['Data'], data_and_step['Step'])
    results['Out_type'] = np.where(data_and_step['Data'] == results['Out'], 'data', 'step')
    results['In_type'] = np.where(data_and_step['Data'] == results['Out'], 'step', 'data')
    results = results[~((results['Out'] == 'CS513') | (results['In'] == 'CS513') |
                        (results['Out'] == 'CleanMenu') | (results['In'] == 'CleanMenu') |
                        (results['Out'] == 'CleanDish' ) | (results['In'] == 'CleanDish') |
                        (results['Out'] == 'CleanMenuPage' ) | (results['In'] == 'CleanMenuPage') |
                        (results['Out'] == 'CleanMenuItem' ) | (results['In'] == 'CleanMenuItem'))]
    results['Out'] = results['Out'].str.replace('CS513.','')
    results['In'] = results['In'].str.replace('CS513.', '')
    results = results.reset_index(drop = True)
    return results

def parsing(df):
    """
    parsing the dataframe and generating facts for clingo
    :param df: a dataframe of edges and the types of their nodes
    :return: a list of edges and node types concatenated for clingo
    """
    edge_list = []
    type_list = []
    for i in range(len(df)):
        edge = 'edge(' + str(df['Out'][i]) + ',' + str(df['In'][i]) + ').'
        edge_list.append(edge)
        out_type = str(df['Out_type'][i]) + '(' + str(df['Out'][i]) + ').'
        in_type = str(df['In_type'][i]) + '(' + str(df['In'][i]) + ').'
        if out_type not in type_list:
            type_list.append(out_type)
        if in_type not in type_list:
            type_list.append(in_type)
    facts = ''
    for item in edge_list:
        facts += str(item)
    for item in type_list:
        facts += str(item)
    facts = facts.lower()
    facts = re.sub('\/', '_', facts)
    facts = re.sub('-', '_', facts)
    facts = re.sub('#', '', facts)
    facts = re.sub('([a-z])\.', '\\1_', facts)
    return facts

def run_clingo(facts, rules, sample_queries, output_link):
    """
    running clingo
    :param facts: a string of facts set
    :param rules: a string of rules set
    :param queries: a string of sample queries set
    :param output_link: link for the output file
    :return:
    """
    ctl = clingo.Control()
    ctl.add("base",[], facts)
    ctl.add("base", [], rules)
    ctl.add("base", [], sample_queries)
    ctl.ground([("base", [])])
    ctl.configuration.solve.models = 0
    output = open(output_link, 'w')  # creating data output files
    with ctl.solve(yield_=True) as handle:
        # loop over all models and print them
        for model in handle:
            print(model, file = output)

def clean_output_txt(file, output_link):
    """
    clean the output file and record the results only (not the original facts)
    :param file: full clingo output file
    :param output_link: link of the output file
    :return:
    """
    with open(file, 'r') as file:
        data = file.read()
    data = re.sub('edge\([a-z_0-9]*,[a-z_0-9]*\) *', '', data)
    data = re.sub('data\([a-z_0-9]*\) *', '', data)
    data = re.sub('step\([a-z_0-9]*\) *', '', data)
    data = re.sub(' ','\n', data)
    output = open(output_link, 'w')
    print(data, file = output)

def clean_output_txt_as_sample_query(file, output_link):
    """
    clean the output file and record the results of the sample query only
    :param file: full clingo output file
    :param output_link: link of the output file
    :return:
    """
    with open(file, 'r') as file:
        data = file.read()
    data = re.sub('edge\([a-z_0-9]*,[a-z_0-9]*\) *', '', data)
    data = re.sub('data\([a-z_0-9]*\) *', '', data)
    data = re.sub('step\([a-z_0-9]*\) *', '', data)
    data = re.sub('upstream\([a-z_0-9]*,[a-z_0-9]*\) *', '', data)
    data = re.sub('downstream\([a-z_0-9]*,[a-z_0-9]*\) *', '', data)
    data = re.sub('parallel_data\([a-z_0-9]*,[a-z_0-9]*\) *', '', data)
    data = re.sub('parallel_step\([a-z_0-9]*,[a-z_0-9]*\) *', '', data)
    data = re.sub('upstream_data_type\([a-z_0-9]*,[a-z_0-9]*\) *', '', data)
    data = re.sub('upstream_step_type\([a-z_0-9]*,[a-z_0-9]*\) *', '', data)
    data = re.sub('downstream_data_type\([a-z_0-9]*,[a-z_0-9]*\) *', '', data)
    data = re.sub('downstream_step_type\([a-z_0-9]*,[a-z_0-9]*\) *', '', data)
    data = re.sub(' ','\n', data)
    output = open(output_link, 'w')
    print(data, file = output)

if __name__ == '__main__':
    overall = read_data('overall.txt')
    facts_overall = parsing(overall)
    cleanmenu = read_data('openrefine_cleanmenu.txt')
    facts_cleanmenu = parsing(cleanmenu)
    cleandish = read_data('openrefine_cleandish.txt')
    facts_cleandish = parsing(cleandish)
    cleanmenupage = read_data('openrefine_cleanmenupage.txt')
    facts_cleanmenupage = parsing(cleanmenupage)
    cleanmenuitem = read_data('openrefine_cleanmenuitem.txt')
    facts_cleanmenuitem = parsing(cleanmenuitem)

    sample_query = "parallel_data_tokens(X) :- parallel_data(X, tokens)." \
                   "parallel_data_tokens(X) :- parallel_data(tokens, X)." \
                   "upstream_data_type_tokens(X) :- upstream_data_type(X, tokens)." \
                   "upstream_step_type_tokens(X) :- upstream_step_type(X, tokens)." \
                   "downstream_data_type_tokens(X) :- downstream_data_type(X, tokens)." \
                   "downstream_step_type_tokens(X) :- downstream_step_type(X, tokens)."

    run_clingo(facts_overall, workflow_rules, '', 'Clingo.txt')
    clean_output_txt('Clingo.txt', 'overall_output.txt')
    run_clingo(facts_cleanmenu, workflow_rules, '', 'Clingo.txt')
    clean_output_txt('Clingo.txt', 'cleanmenu_output.txt')
    run_clingo(facts_cleandish, workflow_rules, '', 'Clingo.txt')
    clean_output_txt('Clingo.txt', 'cleandish_output.txt')
    run_clingo(facts_cleanmenupage, workflow_rules, '', 'Clingo.txt')
    clean_output_txt('Clingo.txt', 'cleanmenupage_output.txt')
    run_clingo(facts_cleanmenuitem, workflow_rules, '', 'Clingo.txt')
    clean_output_txt('Clingo.txt', 'cleanmenuitem_output.txt')
    run_clingo(facts_overall, workflow_rules, sample_query, 'Clingo.txt')
    clean_output_txt_as_sample_query('Clingo.txt', 'sample_query_output.txt')
    os.remove('Clingo.txt')
