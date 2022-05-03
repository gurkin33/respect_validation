from respect_validation.Exceptions import ValidationException


class LowercaseException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be lowercase',
        },
        'negative': {
            'standard': '{name} must not be lowercase',
        }
    }
