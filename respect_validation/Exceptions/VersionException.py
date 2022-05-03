from respect_validation.Exceptions import ValidationException


class VersionException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a version',
        },
        'negative': {
            'standard': '{name} must not be a version',
        }
    }
