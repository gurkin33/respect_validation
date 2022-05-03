from respect_validation.Exceptions import ValidationException


class CnpjException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid CNPJ number',
        },
        'negative': {
            'standard': '{name} must not be a valid CNPJ number',
        }
    }
