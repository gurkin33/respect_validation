from respect_validation.Exceptions import ValidationException


class ListTypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be of type list',
        },
        'negative': {
            'standard': '{name} must not be of type list',
        }
    }
