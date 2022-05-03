from respect_validation.Exceptions.FilteredValidationException import FilteredValidationException


class PunctException(FilteredValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must contain only punctuation characters',
            'extra': '{name} must contain only punctuation characters and {additional_chars}',
        },
        'negative': {
            'standard': '{name} must not contain punctuation characters',
            'extra': '{name} must not contain punctuation characters or {additional_chars}',
        }
    }
