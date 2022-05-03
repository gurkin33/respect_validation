from respect_validation.Exceptions import ValidationException


class DirectoryException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a directory'
        },
        'negative': {
            'standard': '{name} must not be a directory'
        }
    }
