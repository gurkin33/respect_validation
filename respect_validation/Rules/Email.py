import re
from email.utils import parseaddr
from typing import List, Optional

from respect_validation.Rules.AbstractRule import AbstractRule


class Email(AbstractRule):
    #  Main check I got from validators lib
    #  https://github.com/kvesteri/validators/blob/master/validators/email.py
    #

    _user_regex = re.compile(
        # dot-atom
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+"
        r"(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*$"
        # quoted-string
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|'
        r"""\\[\001-\011\013\014\016-\177])*"$)""",
        re.IGNORECASE
    )
    _domain_regex = re.compile(
        # domain
        r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
        r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?$)'
        # literal form, ipv4 address (SMTP 4.1.3)
        r'|^\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)'
        r'(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]$',
        re.IGNORECASE)
    _domain_whitelist = ['localhost']

    def __init__(self, whitelist: Optional[List[str]] = None):
        super().__init__()
        if whitelist is not None:
            self._domain_whitelist = whitelist

    def validate(self, input_val) -> bool:
        if not isinstance(input_val, str) or '@' not in input_val:
            return False

        user_part, domain_part = input_val.rsplit('@', 1)
        if not bool(self._user_regex.match(user_part)):
            return False
        if len(user_part.encode("utf-8")) > 64:
            return False
        if domain_part not in self._domain_whitelist and not self._domain_regex.match(domain_part):
            # Try for possible IDN domain-part
            try:
                domain_part = domain_part.encode('idna').decode('ascii')
                return bool(self._domain_regex.match(domain_part))
            except UnicodeError:
                return False
        #  Additional check
        #  Here is regular expression to check email https://emailregex.com/
        #  regex was changed, I added [\w\d] at the end to be sure test@test.com. will be not valid
        return bool(
            re.match(
                r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+[\w\d]$)", input_val)
        ) and '@' in parseaddr(input_val)[1]
