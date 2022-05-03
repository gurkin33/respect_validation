from respect_validation.Exceptions import ValidationException


class ExtensionException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must have {extension} extension',
        },
        'negative': {
            'standard': '{name} must not have {extension} extension',
        }
    }
