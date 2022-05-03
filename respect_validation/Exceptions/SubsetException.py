from respect_validation.Exceptions import ValidationException


class SubsetException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be subset of {superset}',
        },
        'negative': {
            'standard': '{name} must not be subset of {superset}',
        }
    }
