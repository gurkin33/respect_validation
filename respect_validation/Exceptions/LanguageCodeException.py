from respect_validation.Exceptions import ValidationException


class LanguageCodeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid ISO 639 {code_set} language code',
        },
        'negative': {
            'standard': '{name} must not be a valid ISO 639 {code_set} language code',
        }
    }
