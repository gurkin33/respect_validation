from typing import List

import chardet
import codecs

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class Charset(AbstractRule):
    _charset = None

    def __init__(self, *args: str):
        super().__init__()
        self._charset = self._exist_encodings(*args)
        if not len(self._charset):
            raise ComponentException('Invalid charset')

        self.set_param('charset', list(args))

    def validate(self, input_val):
        if isinstance(input_val, bytes):
            encoding = chardet.detect(input_val).get('encoding', False)
        elif isinstance(input_val, str):
            encoding = chardet.detect(input_val.encode()).get('encoding', False)
        else:
            return False

        return encoding and encoding.lower() in self._charset  # type: ignore

    def _exist_encodings(self, *args):
        encodings_found: List[str] = []
        if not list(args):
            return encodings_found
        for en in list(args):
            try:
                codecs.lookup(en)
                encodings_found.append(en.lower())
            except LookupError:
                pass
        return encodings_found
