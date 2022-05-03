from respect_validation.Exceptions import ValidationException


class SlugException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid slug',
        },
        'negative': {
            'standard': '{name} must not be a valid slug',
        }
    }
