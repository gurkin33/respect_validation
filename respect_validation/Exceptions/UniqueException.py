from respect_validation.Exceptions import ValidationException


class UniqueException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must not contain duplicates',
        },
        'negative': {
            'standard': '{name} must contain duplicates',
        }
    }
