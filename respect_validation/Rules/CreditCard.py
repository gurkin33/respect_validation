import re

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule
from respect_validation.Rules.Luhn import Luhn


class CreditCard(AbstractRule):
    ANY = 'Any'
    AMERICAN_EXPRESS = 'American Express'
    DINERS_CLUB = 'Diners Club'
    DISCOVER = 'Discover'
    JCB = 'JCB'
    MASTERCARD = 'MasterCard'
    VISA = 'Visa'

    #  Note
    #  Here is good article about Credit Card parser:
    #  https://web.archive.org/web/20180904130300/https://creditcardjs.com/credit-card-type-detection
    #
    #  Also read third comment here (DO. NOT. USE. REGEX !!!):
    #  https://stackoverflow.com/questions/9315647/regex-credit-card-number-tests

    BRAND_REGEX_LIST = {
        'any': r'^[0-9]+$',
        'American Express': r'^3[47]\d{13}$',
        'Diners Club': r'^3(?:0[0-5]|[68]\d)\d{11}$',
        'Discover': r'^6(?:011|5\d{2})\d{12}$',
        'JCB': r'^(?:2131|1800|35\d{3})\d{11}$',
        'MasterCard': r'(5[1-5]|2[2-7])\d{14}$',
        'Visa': r'^4\d{12}(?:\d{3})?$',
    }

    _brand: str

    def __init__(self, brand: str = 'any'):
        if brand not in self.BRAND_REGEX_LIST.keys():
            raise ComponentException('"{}" is not a valid credit card brand (Available: {})'.format(
                brand, list(self.BRAND_REGEX_LIST.keys())))
        self._brand = brand
        self.set_param('brand', brand)

    def validate(self, input_val):

        input_val = str(re.sub("[^0-9]", "", str(input_val)))
        if not Luhn().validate(input_val):
            return False
        return len(re.findall(self.BRAND_REGEX_LIST[self._brand], input_val)) == 1
