from respect_validation.Exceptions import ValidationException


class MultipleException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be multiple of {multiple_of}',
        },
        'negative': {
            'standard': '{name} must not be multiple of {multiple_of}',
        }
    }
