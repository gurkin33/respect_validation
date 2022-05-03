from respect_validation.Exceptions import ValidationException


class LeapDateException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be leap date',
        },
        'negative': {
            'standard': '{name} must not be leap date',
        }
    }
