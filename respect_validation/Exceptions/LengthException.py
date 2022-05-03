from respect_validation.Exceptions import ValidationException


class LengthException(ValidationException):

    BOTH = 'both'
    LOWER = 'lower'
    LOWER_INCLUSIVE = 'lower_inclusive'
    GREATER = 'greater'
    GREATER_INCLUSIVE = 'greater_inclusive'
    EXACT = 'exact'

    _default_templates = {
        'default': {
            'both': '{name} must have a length between {min_value} and {max_value}',
            'lower': '{name} must have a length greater than {min_value}',
            'lower_inclusive': '{name} must have a length greater than or equal to {min_value}',
            'greater': '{name} must have a length lower than {max_value}',
            'greater_inclusive': '{name} must have a length lower than or equal to {max_value}',
            'exact': '{name} must have a length of {max_value}',
        },
        'negative': {
            'both': '{name} must not have a length between {min_value} and {max_value}',
            'lower': '{name} must not have a length greater than {min_value}',
            'lower_inclusive': '{name} must not have a length greater than or equal to {min_value}',
            'greater': '{name} must not have a length lower than {max_value}',
            'greater_inclusive': '{name} must not have a length lower than or equal to {max_value}',
            'exact': '{name} must not have a length of {max_value}',
        }
    }

    def choose_template(self):

        is_inclusive = self.get_param('inclusive')

        if not self.get_param('min_value'):
            return self.GREATER_INCLUSIVE if is_inclusive else self.GREATER

        if not self.get_param('max_value'):
            return self.LOWER_INCLUSIVE if is_inclusive else self.LOWER

        if self.get_param('max_value') == self.get_param('min_value'):
            return self.EXACT

        return self.BOTH
