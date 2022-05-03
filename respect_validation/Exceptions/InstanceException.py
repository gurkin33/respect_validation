from respect_validation.Exceptions import ValidationException


class InstanceException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be an instance of {instance_name}',
        },
        'negative': {
            'standard': '{name} must not be an instance of {instance_name}',
        }
    }
