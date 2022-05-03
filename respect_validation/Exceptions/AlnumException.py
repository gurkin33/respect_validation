from respect_validation.Exceptions.FilteredValidationException import FilteredValidationException


class AlnumException(FilteredValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must contain only letters (a-z) and digits (0-9)',
            'extra': '{name} must contain only letters (a-z), digits (0-9) and {additional_chars}',
        },
        'negative': {
            'standard': '{name} must contain only letters (a-z) and digits (0-9)',
            'extra': '{name} must contain only letters (a-z), digits (0-9) and {additional_chars}',
        }
    }
