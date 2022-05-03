from respect_validation.Exceptions import NestedValidationException


class KeyException(NestedValidationException):

    NOT_PRESENT = 'not_present'
    INVALID = 'invalid'

    _default_templates = {
        'default': {
            'not_present': '{name} must be present',
            'invalid': '{name} must be valid',
        },
        'negative': {
            'not_present': '{name} must not be present',
            'invalid': '{name} must not be valid',
        }
    }

    def choose_template(self):

        return self.INVALID if self.get_param('has_reference') else self.NOT_PRESENT
