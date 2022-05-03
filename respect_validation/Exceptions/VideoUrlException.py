from respect_validation.Exceptions import ValidationException


class VideoUrlException(ValidationException):

    SERVICE = 'service'

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid video URL',
            'service': '{name} must be a valid {service} video URL',
        },
        'negative': {
            'standard': '{name} must not be a valid video URL',
            'service': '{name} must not be a valid {service} video URL',
        }
    }

    def choose_template(self) -> str:
        return self.SERVICE if self.get_param('service') else self.STANDARD
