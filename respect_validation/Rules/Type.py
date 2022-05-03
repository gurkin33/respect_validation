from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class Type(AbstractRule):

    AVAILABLE_TYPES = [
        'list', 'bool', 'int',
        'str', 'float', 'complex',
        'list', 'tuple', 'range',
        'dict', 'set', 'frozenset',
        'bytes', 'bytearray', 'memoryview',
        'function', 'NoneType'
    ]

    _type: str

    def __init__(self, type_name: str):
        super().__init__()
        self._type = str(type_name)
        if self._type not in self.AVAILABLE_TYPES:
            raise ComponentException('"{}" is not a valid type (Available: {})'.format(self._type, self.AVAILABLE_TYPES))
        self.set_param('type_name', self._type)

    def validate(self, input_val) -> bool:

        return type(input_val).__name__ == self._type
