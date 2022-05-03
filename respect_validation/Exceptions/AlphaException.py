from respect_validation.Exceptions.FilteredValidationException import FilteredValidationException


class AlphaException(FilteredValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must contain only letters (a-z)',
            'extra': '{name} must contain only letters (a-z) and {additional_chars}',
        },
        'negative': {
            'standard': '{name} must not contain letters (a-z)',
            'extra': '{name} must not contain letters (a-z) or {additional_chars}',
        }
    }
