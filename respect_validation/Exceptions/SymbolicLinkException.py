from respect_validation.Exceptions import ValidationException


class SymbolicLinkException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a symbolic link',
        },
        'negative': {
            'standard': '{name} must not be a symbolic link',
        }
    }
