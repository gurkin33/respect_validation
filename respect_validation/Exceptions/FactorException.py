from respect_validation.Exceptions import ValidationException


class FactorException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a factor of {dividend}',
        },
        'negative': {
            'standard': '{name} must not be a factor of {dividend}',
        }
    }
