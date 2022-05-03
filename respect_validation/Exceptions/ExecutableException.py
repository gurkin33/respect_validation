from respect_validation.Exceptions import ValidationException


class ExecutableException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be an executable file',
        },
        'negative': {
            'standard': '{name} must not be an executable file',
        }
    }
