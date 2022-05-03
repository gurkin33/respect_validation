from respect_validation.Exceptions import ValidationException


class ImeiException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid IMEI',
        },
        'negative': {
            'standard': '{name} must not be a valid IMEI',
        }
    }
