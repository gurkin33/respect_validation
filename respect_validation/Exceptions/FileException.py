from respect_validation.Exceptions import ValidationException


class FileException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a file',
        },
        'negative': {
            'standard': '{name} must not be a file',
        }
    }
