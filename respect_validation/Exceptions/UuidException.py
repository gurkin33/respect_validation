from respect_validation.Exceptions import ValidationException


class UuidException(ValidationException):

    VERSION = 'version'

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid UUID',
            'version': '{name} must be a valid UUID version {version}',
        },
        'negative': {
            'standard': '{name} must not be a valid UUID',
            'version': '{name} must not be a valid UUID version {version}',
        }
    }

    def choose_template(self) -> str:
        return self.VERSION if self.get_param('version') else self.STANDARD
