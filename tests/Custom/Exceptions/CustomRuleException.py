from respect_validation.Exceptions import ValidationException


class CustomRuleException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be equal to "Hello custom rule!"'
        },
        'negative': {
            'standard': '{name} must not be equal to "Hello custom rule!"'
        }
    }
