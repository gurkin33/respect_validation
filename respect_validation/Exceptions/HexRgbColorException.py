from respect_validation.Exceptions import ValidationException


class HexRgbColorException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a hex RGB color',
        },
        'negative': {
            'standard': '{name} must not be a hex RGB color',
        }
    }
