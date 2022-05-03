from respect_validation.Exceptions import ValidationException


class DateTimeException(ValidationException):

    FORMAT = 'format'

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid date/time',
            'format': '{name} must be a valid date/time in the format {sample}'
        },
        'negative': {
            'standard': '{name} must not be a valid date/time',
            'format': '{name} must not be a valid date/time in the format {sample}'
        }
    }

    def choose_template(self):
        return self.FORMAT if self.get_param('format') else self.STANDARD
