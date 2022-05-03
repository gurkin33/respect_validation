from respect_validation.Exceptions.FilteredValidationException import FilteredValidationException


class DigitException(FilteredValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must contain only digits (0-9)',
            'extra': '{name} must contain only digits (0-9) and {additional_chars}'
        },
        'negative': {
            'standard': '{name} must not contain digits (0-9)',
            'extra': '{name} must not contain digits (0-9) and {additional_chars}'
        }
    }
