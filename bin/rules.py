import json
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
    def get_exceptions_default_messages():
        mypath = str(__file__).replace('rules.py', '../respect_validation/Exceptions/')
        exceptions = [
            str(f).replace('Exception.py', '') for f in listdir(mypath)
            if isfile(join(mypath, f)) and 'Exception.py' in f]
        import_path = 'respect_validation.Exceptions'
        all_messages = {}
        for e in exceptions:
            if e in ['NonOmissible', 'Component', 'NestedValidation']:
                continue
            try:
                fullname = f'{import_path}.{e}Exception'
                mod = __import__(fullname)
                components = fullname.split('.')
                for comp in components[1:]:
                    mod = getattr(mod, comp)
                if e != 'Validation':
                    mod = getattr(mod, f'{e}Exception')
                all_messages[e[0].lower() + e[1:]]=mod._default_templates
            except Exception as exception:
                print(f"Something was wrong with {e}Exception")
                print(f"Exception {exception}")
        print(json.dumps(all_messages, indent=2))
        current_path = str(__file__).replace('rules.py', '')
        with open(f'{current_path}/default_messages.json', 'w') as outfile:
            json.dump(all_messages, outfile, indent=2)
        return True

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


if __name__ == '__main__':
    Rules.get_exceptions_default_messages()
