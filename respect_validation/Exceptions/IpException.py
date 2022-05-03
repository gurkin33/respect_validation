from respect_validation.Exceptions import ValidationException


class IpException(ValidationException):

    NETWORK_RANGE = 'network_range'
    MUST_BE_PRIVATE = 'must_be_private'

    _default_templates = {
        'default': {
            'standard': '{name} must be an IP address',
            'must_be_private': '{name} must be a private IP address',
            'network_range': '{name} must be an IP address in the {ip_range} range',
        },
        'negative': {
            'standard': '{name} must not be an IP address',
            'must_be_private': '{name} must not be a private IP address',
            'network_range': '{name} must not be an IP address in the {ip_range} range',
        }
    }

    def choose_template(self):
        if self.get_param('must_be_private'):
            return self.MUST_BE_PRIVATE
        return self.NETWORK_RANGE if self.get_param('ip_range') else self.STANDARD
