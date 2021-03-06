from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractEnvelope import AbstractEnvelope
from respect_validation.Rules.CountryCode import CountryCode
from respect_validation.Rules.Regex import Regex


class PostalCode(AbstractEnvelope):
    DEFAULT_PATTERN = r'^$'
    POSTAL_CODES = {
        'AD': r'^(?:AD)*(\d{3})$',
        'AL': r'^(\d{4})$',
        'AM': r'^(\d{4})$',
        'AR': r'^[A-Z]?\d{4}[A-Z]{0,3}$',
        'AS': r'96799',
        'AT': r'^(\d{4})$',
        'AU': r'^(\d{4})$',
        'AX': r'^(?:FI)*(\d{5})$',
        'AZ': r'^(?:AZ)*(\d{4})$',
        'BA': r'^(\d{5})$',
        'BB': r'^(?:BB)*(\d{5})$',
        'BD': r'^(\d{4})$',
        'BE': r'^(\d{4})$',
        'BG': r'^(\d{4})$',
        'BH': r'^(\d{3}\d?)$',
        'BL': r'^(\d{5})$',
        'BM': r'^([A-Z]{2}\d{2})$',
        'BN': r'^([A-Z]{2}\d{4})$',
        'BR': r'^\d{5}-?\d{3}$',
        'BY': r'^(\d{6})$',
        'CA': r'^([ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ]) ?(\d[ABCEGHJKLMNPRSTVWXYZ]\d)$',
        'CH': r'^(\d{4})$',
        'CL': r'^(\d{7})$',
        'CN': r'^(\d{6})$',
        'CO': r'^(\d{6})$',
        'CR': r'^(\d{5})$',
        'CS': r'^(\d{5})$',
        'CU': r'^(?:CP)*(\d{5})$',
        'CV': r'^(\d{4})$',
        'CX': r'^(\d{4})$',
        'CY': r'^(\d{4})$',
        'CZ': r'^\d{3}\s?\d{2}$',
        'DE': r'^(\d{5})$',
        'DK': r'^(\d{4})$',
        'DO': r'^(\d{5})$',
        'DZ': r'^(\d{5})$',
        'EC': r'^(\d{6})$',
        'EE': r'^(\d{5})$',
        'EG': r'^(\d{5})$',
        'ES': r'^(\d{5})$',
        'ET': r'^(\d{4})$',
        'FI': r'^(?:FI)*(\d{5})$',
        'FM': r'^(\d{5})$',
        'FO': r'^(?:FO)*(\d{3})$',
        'FR': r'^(\d{5})$',
        'GB': r'^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9]['
              r'A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$',
        'GE': r'^(\d{4})$',
        'GF': r'^((97|98)3\d{2})$',
        'GG': r'^((?:(?:[A-PR-UWYZ][A-HK-Y]\d[ABEHMNPRV-Y0-9]|[A-PR-UWYZ]\d[A-HJKPS-UW0-9])\s\d[ABD-HJLNP-UW-Z]{'
              r'2})|GIR\s?0AA)$',
        'GL': r'^(\d{4})$',
        'GP': r'^((97|98)\d{3})$',
        'GR': r'^(\d{3}\s?\d{2})$',
        'GT': r'^(\d{5})$',
        'GU': r'^(969\d{2})$',
        'GW': r'^(\d{4})$',
        'HN': r'^([A-Z]{2}\d{4})$',
        'HR': r'^(?:HR)*(\d{5})$',
        'HT': r'^(?:HT)*(\d{4})$',
        'HU': r'^(\d{4})$',
        'ID': r'^(\d{5})$',
        'IE': r'^(D6W|[AC-FHKNPRTV-Y][0-9]{2})\s?([AC-FHKNPRTV-Y0-9]{4})',
        'IL': r'^(\d{7}|\d{5})$',
        'IM': r'^((?:(?:[A-PR-UWYZ][A-HK-Y]\d[ABEHMNPRV-Y0-9]|[A-PR-UWYZ]\d[A-HJKPS-UW0-9])\s\d[ABD-HJLNP-UW-Z]{'
              r'2})|GIR\s?0AA)$',
        'IN': r'^(\d{6})$',
        'IQ': r'^(\d{5})$',
        'IR': r'^(\d{10})$',
        'IS': r'^(\d{3})$',
        'IT': r'^(\d{5})$',
        'JE': r'^((?:(?:[A-PR-UWYZ][A-HK-Y]\d[ABEHMNPRV-Y0-9]|[A-PR-UWYZ]\d[A-HJKPS-UW0-9])\s\d[ABD-HJLNP-UW-Z]{'
              r'2})|GIR\s?0AA)$',
        'JO': r'^(\d{5})$',
        'JP': r'^\d{3}-\d{4}$',
        'KE': r'^(\d{5})$',
        'KG': r'^(\d{6})$',
        'KH': r'^(\d{5})$',
        'KP': r'^(\d{6})$',
        'KR': r'^(\d{5})$',
        'KW': r'^(\d{5})$',
        'KY': r'^KY[1-3]-\d{4}$',
        'KZ': r'^(\d{6})$',
        'LA': r'^(\d{5})$',
        'LB': r'^(\d{4}(\d{4})?)$',
        'LI': r'^(\d{4})$',
        'LK': r'^(\d{5})$',
        'LR': r'^(\d{4})$',
        'LS': r'^(\d{3})$',
        'LT': r'^(?:LT)*(\d{5})$',
        'LU': r'^(?:L-)?\d{4}$',
        'LV': r'^(?:LV)*(\d{4})$',
        'MA': r'^(\d{5})$',
        'MC': r'^(\d{5})$',
        'MD': r'^MD-\d{4}$',
        'ME': r'^(\d{5})$',
        'MF': r'^(\d{5})$',
        'MG': r'^(\d{3})$',
        'MH': r'^969\d{2}(-\d{4})$',
        'MK': r'^(\d{4})$',
        'MM': r'^(\d{5})$',
        'MN': r'^(\d{6})$',
        'MP': r'^9695\d{1}$',
        'MQ': r'^(\d{5})$',
        'MT': r'^[A-Z]{3}\s?\d{4}$',
        'MV': r'^(\d{5})$',
        'MW': r'^(\d{6})$',
        'MX': r'^(\d{5})$',
        'MY': r'^(\d{5})$',
        'MZ': r'^(\d{4})$',
        'NC': r'^(\d{5})$',
        'NE': r'^(\d{4})$',
        'NF': r'^(\d{4})$',
        'NG': r'^(\d{6})$',
        'NI': r'^(\d{7})$',
        'NL': r'^(\d{4} ?[A-Z]{2})$',
        'NO': r'^(\d{4})$',
        'NP': r'^(\d{5})$',
        'NZ': r'^(\d{4})$',
        'OM': r'^(\d{3})$',
        'PF': r'^((97|98)7\d{2})$',
        'PG': r'^(\d{3})$',
        'PH': r'^(\d{4})$',
        'PK': r'^(\d{5})$',
        'PL': r'^\d{2}-\d{3}$',
        'PM': r'^(97500)$',
        'PR': r'^00[679]\d{2}(?:-\d{4})?$',
        'PT': r'^\d{4}-?\d{3}$',
        'PW': r'^(96940)$',
        'PY': r'^(\d{4})$',
        'RE': r'^((97|98)(4|7|8)\d{2})$',
        'RO': r'^(\d{6})$',
        'RS': r'^(\d{5})$',
        'RU': r'^(\d{6})$',
        'SA': r'^(\d{5})$',
        'SD': r'^(\d{5})$',
        'SE': r'^(?:SE)?\d{3}\s\d{2}$',
        'SG': r'^(\d{6})$',
        'SH': r'^(STHL1ZZ)$',
        'SI': r'^(?:SI)*(\d{4})$',
        'SJ': r'^(\d{4})$',
        'SK': r'^\d{3}\s?\d{2}$',
        'SM': r'^(4789\d)$',
        'SN': r'^(\d{5})$',
        'SO': r'^([A-Z]{2}\d{5})$',
        'SV': r'^(?:CP)*(\d{4})$',
        'SZ': r'^([A-Z]\d{3})$',
        'TC': r'^(TKCA 1ZZ)$',
        'TH': r'^(\d{5})$',
        'TJ': r'^(\d{6})$',
        'TM': r'^(\d{6})$',
        'TN': r'^(\d{4})$',
        'TR': r'^(\d{5})$',
        'TW': r'^(\d{5})$',
        'UA': r'^(\d{5})$',
        'US': r'^\d{5}(-\d{4})?$',
        'UY': r'^(\d{5})$',
        'UZ': r'^(\d{6})$',
        'VA': r'^(\d{5})$',
        'VE': r'^(\d{4})$',
        'VI': r'^008\d{2}(?:-\d{4})?$',
        'VN': r'^(\d{6})$',
        'WF': r'^(986\d{2})$',
        'YT': r'^(\d{5})$',
        'ZA': r'^(\d{4})$',
        'ZM': r'^(\d{5})$'
    }

    def __init__(self, country_code: str):
        country_code_rule = CountryCode()
        if not country_code_rule.validate(country_code) or country_code not in self.POSTAL_CODES.keys():
            raise ComponentException('Cannot validate postal code from "{}" country'.format(country_code)) from None
        super().__init__(Regex(self.POSTAL_CODES[country_code]), {'country_code': country_code})
