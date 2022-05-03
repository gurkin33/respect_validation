from respect_validation.Exceptions import ValidationException


class IncludeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be in {haystack}',
        },
        'negative': {
            'standard': '{name} must not be in {haystack}',
        }
    }
