from respect_validation.Exceptions import ValidationException


class LeapYearException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a leap year',
        },
        'negative': {
            'standard': '{name} must not be a leap year',
        }
    }
