from respect_validation.Exceptions import ValidationException


class UrlException(ValidationException):

    PUBLIC = 'public'

    _default_templates = {
        'default': {
            'standard': '{name} must be a URL',
            'public': '{name} must be a public URL',
        },
        'negative': {
            'standard': '{name} must not be a URL',
            'public': '{name} must not be a public URL',
        }
    }

    def choose_template(self) -> str:
        return self.PUBLIC if self.get_param('public') else self.STANDARD
