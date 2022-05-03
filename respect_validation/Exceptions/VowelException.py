from respect_validation.Exceptions.FilteredValidationException import FilteredValidationException


class VowelException(FilteredValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must contain only vowels',
            'extra': '{name} must contain only vowels and {additional_chars}',
        },
        'negative': {
            'standard': '{name} must not contain vowels',
            'extra': '{name} must not contain vowels or {additional_chars}',
        }
    }
