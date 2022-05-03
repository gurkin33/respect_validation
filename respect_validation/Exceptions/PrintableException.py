from respect_validation.Exceptions.FilteredValidationException import FilteredValidationException


class PrintableException(FilteredValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must contain only printable characters',
            'extra': '{name} must contain only printable characters and {additional_chars}',
        },
        'negative': {
            'standard': '{name} must not contain printable characters',
            'extra': '{name} must not contain printable characters or {additional_chars}',
        }
    }
