from respect_validation.Exceptions import ValidationException


class TypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be {type_name}',
        },
        'negative': {
            'standard': '{name} must not be {type_name}',
        }
    }
