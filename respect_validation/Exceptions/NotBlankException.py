from respect_validation.Exceptions import ValidationException


class NotBlankException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must not be blank',
        },
        'negative': {
            'standard': '{name} must be blank',
        }
    }
