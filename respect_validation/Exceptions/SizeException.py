from respect_validation.Exceptions import NestedValidationException


class SizeException(NestedValidationException):

    BOTH = 'both'
    LOWER = 'lower'
    GREATER = 'greater'

    _default_templates = {
        'default': {
            'both': '{name} must be between {min_size} and {max_size}',
            'lower': '{name} must be greater than {min_size}',
            'greater': '{name} must be lower than {max_size}',
        },
        'negative': {
            'both': '{name} must not be between {min_size} and {max_size}',
            'lower': '{name} must not be greater than {min_size}',
            'greater': '{name} must not be lower than {max_size}',
        }
    }

    def choose_template(self) -> str:
        if not self.get_param('min_value'):
            return self.GREATER

        if not self.get_param('max_value'):
            return self.LOWER

        return self.BOTH
