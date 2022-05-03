from respect_validation.Exceptions import ValidationException


class MacAddressException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid MAC address',
        },
        'negative': {
            'standard': '{name} must not be a valid MAC address',
        }
    }
