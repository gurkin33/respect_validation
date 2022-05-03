import re

from respect_validation.Rules.AbstractRule import AbstractRule


class Iban(AbstractRule):

    COUNTRIES_LENGTHS = {
        'AL': 28,
        'AD': 24,
        'AT': 20,
        'AZ': 28,
        'BH': 22,
        'BE': 16,
        'BA': 20,
        'BR': 29,
        'BG': 22,
        'CR': 21,
        'HR': 21,
        'CY': 28,
        'CZ': 24,
        'DK': 18,
        'DO': 28,
        'EE': 20,
        'FO': 18,
        'FI': 18,
        'FR': 27,
        'GE': 22,
        'DE': 22,
        'GI': 23,
        'GR': 27,
        'GL': 18,
        'GT': 28,
        'HU': 28,
        'IS': 26,
        'IE': 22,
        'IL': 23,
        'IT': 27,
        'JO': 30,
        'KZ': 20,
        'KW': 30,
        'LV': 21,
        'LB': 28,
        'LI': 21,
        'LT': 20,
        'LU': 20,
        'MK': 19,
        'MT': 31,
        'MR': 27,
        'MU': 30,
        'MD': 24,
        'MC': 27,
        'ME': 22,
        'NL': 18,
        'NO': 15,
        'PK': 24,
        'PL': 28,
        'PS': 29,
        'PT': 25,
        'QA': 29,
        'XK': 20,
        'RO': 24,
        'LC': 32,
        'SM': 27,
        'ST': 25,
        'SA': 24,
        'RS': 22,
        'SC': 31,
        'SK': 24,
        'SI': 19,
        'ES': 24,
        'SE': 24,
        'CH': 21,
        'TL': 23,
        'TN': 24,
        'TR': 26,
        'UA': 29,
        'AE': 23,
        'GB': 22,
        'VG': 24,
    }

    def validate(self, input_val):
        if not isinstance(input_val, str):
            return False

        iban = input_val.replace(' ', '').upper()
        if not bool(re.match('[A-Z0-9]{15,34}', iban)):
            return False

        country_code = iban[:2]

        if not self._check_country_length(iban, country_code):
            return False

        check_digits = iban[2:4]
        bban = iban[4:]
        re_arranged = str(bban) + str(country_code) + str(check_digits)

        return int(self._convert_to_integer(re_arranged)) % 97 == 1

    def _check_country_length(self, iban, country_code):
        if not self.COUNTRIES_LENGTHS.get(country_code, None):
            return False
        return len(iban) == self.COUNTRIES_LENGTHS.get(country_code)

    def _convert_to_integer(self, re_arranged_iban):
        def replace_letter(m):
            return str(ord(m[0]) - 55)
        return re.sub('[A-Z]', replace_letter, re_arranged_iban)
