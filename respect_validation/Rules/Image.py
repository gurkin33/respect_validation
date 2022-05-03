import mimetypes

from respect_validation.Rules.AbstractRule import AbstractRule


class Image(AbstractRule):

    def validate(self, input_val):
        if not isinstance(input_val, str):
            return False

        return 'image/' in str(mimetypes.guess_type(input_val)[0])
