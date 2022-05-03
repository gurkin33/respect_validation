from respect_validation.Exceptions import ValidationException


class JsonException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid JSON string',
        },
        'negative': {
            'standard': '{name} must not be a valid JSON string',
        }
    }
