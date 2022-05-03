from respect_validation.Exceptions import ValidationException


class IdenticalException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be identical as {compare_to}',
        },
        'negative': {
            'standard': '{name} must not be identical as {compare_to}',
        }
    }
