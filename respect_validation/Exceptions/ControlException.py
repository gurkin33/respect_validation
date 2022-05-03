from respect_validation.Exceptions.FilteredValidationException import FilteredValidationException


class ControlException(FilteredValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must contain only control characters',
            'extra': '{name} must contain only control characters and {additional_chars}'
        },
        'negative': {
            'standard': '{name} must not contain control characters',
            'extra': '{name} must not contain control characters or {additional_chars}'
        }
    }
