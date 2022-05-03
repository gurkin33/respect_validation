from os.path import splitext

from respect_validation.Rules.AbstractRule import AbstractRule


class Extension(AbstractRule):

    _extension = None

    def __init__(self, extension: str):
        super().__init__()
        self._extension = extension
        self.set_param('extension', extension)

    def validate(self, input_val):

        return isinstance(input_val, str) and str(splitext(input_val)[1]).replace('.', '') == self._extension
