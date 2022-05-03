from respect_validation.Exceptions.FilteredValidationException import FilteredValidationException


class ConsonantException(FilteredValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must contain only consonants',
            'extra': '{name} must contain only consonants and {additional_chars}'
        },
        'negative': {
            'standard': '{name} must not contain consonants',
            'extra': '{name} must not contain consonants or {additional_chars}'
        }
    }
