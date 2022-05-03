import re

from respect_validation.Rules.AbstractRule import AbstractRule


class Isbn(AbstractRule):

    #
    #  see for details:
    #  https://howtodoinjava.com/regex/java-regex-validate-international-standard-book-number-isbns
    #

    PIECES = [
        '^(?:ISBN(?:-1[03])?:? )?(?=[0-9X]{10}$|(?=(?:[0-9]+[- ]){3})',
        '[- 0-9X]{13}$|97[89][0-9]{10}$|(?=(?:[0-9]+[- ]){4})[- 0-9]{17}$)',
        '(?:97[89][- ]?)?[0-9]{1,5}[- ]?[0-9]+[- ]?[0-9]+[- ]?[0-9X]$',
    ]

    def validate(self, input_val):

        if not isinstance(input_val, str):
            return False

        return bool(re.match(''.join(self.PIECES), input_val))
