from respect_validation.Exceptions.ValidationException import ValidationException


class FilteredValidationException(ValidationException):

    EXTRA = 'extra'

    def choose_template(self):
        return self.EXTRA if self.get_param('additional_chars') != '' else self.STANDARD
