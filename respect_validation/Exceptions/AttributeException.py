from respect_validation.Exceptions import NestedValidationException


class AttributeException(NestedValidationException):

    NOT_PRESENT = 'not_present'
    INVALID = 'invalid'

    _default_templates = {
        'default': {
            'not_present': 'Attribute {name} must be present',
            'invalid': 'Attribute {name} must be valid',
        },
        'negative': {
            'not_present': 'Attribute {name} must not be present',
            'invalid': 'Attribute {name} must not validate',
        }
    }

    def choose_template(self):
        return self.INVALID if self.get_param('has_reference') else self.NOT_PRESENT
