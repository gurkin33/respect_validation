from respect_validation.Exceptions import ValidationException


class MimetypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must have {mimetype} MIME type',
        },
        'negative': {
            'standard': '{name} must not have {mimetype} MIME type',
        }
    }
