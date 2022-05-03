from respect_validation.Exceptions import ValidationException


class ExistsException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must exists',
        },
        'negative': {
            'standard': '{name} must not exists',
        }
    }
