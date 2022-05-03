from respect_validation.Exceptions import ValidationException


class ImageException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid image',
        },
        'negative': {
            'standard': '{name} must not be a valid image',
        }
    }
