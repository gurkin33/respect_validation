import re
from os import listdir
from os.path import isfile, join


class Rules(object):

    @staticmethod
    def get_rules():
        mypath = str(__file__).replace('rules.py', '../respect_validation/Rules/')
        return [str(f).replace('.py', '') for f in listdir(mypath) if isfile(join(mypath, f))]

    @staticmethod
    def get_exceptions():
        mypath = str(__file__).replace('rules.py', '../respect_validation/Exceptions/')
        return [str(f).replace('Exception.py', '') for f in listdir(mypath) if isfile(join(mypath, f)) and 'Exception.py' in f]

    @staticmethod
    def get_test_rules():
        mypath = str(__file__).replace('rules.py', '../tests/')
        return [Rules._uppercase_name(str(f).replace('.py', '').replace('test_', '')) \
                for f in listdir(mypath) if isfile(join(mypath, f))]

    @staticmethod
    def _uppercase_name(name: str):
        return name[0].upper() + name[1:]

    @staticmethod
    def get_doc_rules():
        mypath = str(__file__).replace('rules.py', '../docs/rules/')
        rules_list = [str(f).replace('.md', '') for f in listdir(mypath) if isfile(join(mypath, f))]
        categories = {}
        for f in listdir(mypath):
            if isfile(join(mypath, f)):
                for c in Rules._parse_doc_rule(join(mypath, f)):
                    if categories.get(c, False):
                        categories[c].append(f.replace('.md', ''))
                    else:
                        categories[c] = [f.replace('.md', '')]
        return rules_list, categories

    @staticmethod
    def _parse_doc_rule(file: str):
        categories = []
        file1 = open(file, 'r')
        Lines = file1.readlines()
        start_collect = False
        for line in Lines:
            if bool(re.match('## Categorization', line)):
                start_collect = True
                continue
            if start_collect is False:
                continue
            if bool(re.match('## Changelog', line)):
                break
            if line.strip() != '':
                categories.append(line.replace('-', '').strip())
        return categories