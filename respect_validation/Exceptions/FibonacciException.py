from respect_validation.Exceptions import ValidationException


class FibonacciException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid Fibonacci number',
        },
        'negative': {
            'standard': '{name} must not be a valid Fibonacci number',
        }
    }
