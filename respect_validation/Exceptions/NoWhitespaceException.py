from respect_validation.Exceptions.ValidationException import ValidationException


class NoWhitespaceException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must not contain whitespace',
        },
        'negative': {
            'standard': '{name} must contain whitespace',
        }
    }
