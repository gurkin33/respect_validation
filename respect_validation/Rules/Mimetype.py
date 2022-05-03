import mimetypes

from respect_validation.Rules.AbstractRule import AbstractRule


class Mimetype(AbstractRule):

    _mimetype = None

    def __init__(self, mimetype: str):
        super().__init__()
        self._mimetype = mimetype

        self.set_param('mimetype', mimetype)

    def validate(self, input_val) -> bool:
        if not isinstance(input_val, str):
            return False

        return self._mimetype == str(mimetypes.guess_type(input_val)[0])
