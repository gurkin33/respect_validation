from respect_validation.Exceptions import ValidationException


class RegexException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must validate against {regex}',
        },
        'negative': {
            'standard': '{name} must not validate against {regex}',
        }
    }
