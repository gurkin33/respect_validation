from respect_validation.Exceptions import ValidationException


class CallException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{input} must be valid when executed with {callable}',
        },
        'negative': {
            'standard': '{input} must not be valid when executed with {callable}',
        }
    }
