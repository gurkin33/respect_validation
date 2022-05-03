from respect_validation.Exceptions import ValidationException
from respect_validation.Rules.CreditCard import CreditCard


class CreditCardException(ValidationException):

    BRANDED = 'branded'

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid Credit Card number',
            'branded': '{name} must be a valid {brand} Credit Card number'
        },
        'negative': {
            'standard': '{name} must not be a valid Credit Card number',
            'branded': '{name} must not be a valid {brand} Credit Card number'
        }
    }

    def choose_template(self):
        if self.get_param('brand') == CreditCard.ANY:
            return self.STANDARD
        return self.BRANDED
