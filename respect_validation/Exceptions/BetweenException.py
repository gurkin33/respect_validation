from respect_validation.Exceptions.NestedValidationException import NestedValidationException


class BetweenException(NestedValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be between {min_value} and {max_value}',
        },
        'negative': {
            'standard': '{name} must not be between {min_value} and {max_value}',
        }
    }
