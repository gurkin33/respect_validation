#!/usr/bin/env python

import argparse
from rules import Rules


parser = argparse.ArgumentParser(description='Respect Validation helper script. Version 1.0.0')

parser.add_argument('-chk', "--check", action='store_true')
parser.add_argument('-mkdoc', "--make-doc", action='store_true')

args = parser.parse_args()


def _rules_preparation(_rules: list):
    rules_ = []
    for r in _rules:
        if "Abstract" in r:
            continue
        if "__init__" in r:
            continue
        rules_.append(r)
    return rules_


if args.check:
    rules = Rules.get_rules()
    print('Total rules count: ', len(_rules_preparation(rules)))

    print('Test tests...')
    error = False
    for r in _rules_preparation(rules):
        if r not in Rules.get_test_rules():
            error = True
            print('Rule {} not found in tests!'.format(r))
    if error:
        print('Error in tests!! Please check!')
    else:
        print('Good job! Awesome! Tests is ok!')

    print('######################################')
    print('Test exceptions...')
    error = False
    for r in _rules_preparation(rules):
        if r not in Rules.get_exceptions():
            error = True
            print('Rule {} not found in exceptions!'.format(r))
    if error:
        print('Error in exceptions!! Please check!')
    else:
        print('Good job! Awesome! Exceptions is ok!')

    print('######################################')
    print('Test docs...')
    error = False
    for r in _rules_preparation(rules):
        if r not in Rules.get_doc_rules()[0]:
            error = True
            print('Rule {} not found in docs!'.format(r))
    if error:
        print('Error in docs!! Please check!')
    else:
        print('Good job! Awesome! Docs is ok!')
    quit()

if args.make_doc:
    rules, categories = Rules.get_doc_rules()
    list_of_rules = "# List of rules \n\n"
    for c in sorted(categories.keys()):
        list_of_rules += "## {}\n\n".format(c)
        for c_item in sorted(categories[c]):
            list_of_rules += "- [{0}](rules/{0}.md)\n".format(c_item)
        list_of_rules += "\n"
    print(list_of_rules)
    f = open(str(__file__).replace('main.py', '../docs/list-of-rules.md'), "w")
    f.write(list_of_rules)
    f.close()
    quit()

parser.print_help()