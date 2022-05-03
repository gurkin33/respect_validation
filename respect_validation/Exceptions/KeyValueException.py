from respect_validation.Exceptions import ValidationException


class KeyValueException(ValidationException):

    COMPONENT = 'component'

    _default_templates = {
        'default': {
            'standard': 'Key {name} must be present',
            'component': '{base_key} must be valid to validate {compared_key}',
        },
        'negative': {
            'standard': 'Key {name} must not be present',
            'component': '{base_key} must not be valid to validate {compared_key}',
        }
    }

    def choose_template(self):
        return self.COMPONENT if self.get_param('component') else self.STANDARD
