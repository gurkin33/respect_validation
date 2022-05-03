from respect_validation.Exceptions.FilteredValidationException import FilteredValidationException


class SpaceException(FilteredValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must contain only space characters',
            'extra': '{name} must contain only space characters and {additional_chars}',
        },
        'negative': {
            'standard': '{name} must not contain space characters',
            'extra': '{name} must not contain space characters or {additional_chars}',
        }
    }
