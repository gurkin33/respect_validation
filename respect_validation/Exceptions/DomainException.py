from respect_validation.Exceptions import NestedValidationException


class DomainException(NestedValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid domain',
        },
        'negative': {
            'standard': '{name} must not be a valid domain',
        }
    }
