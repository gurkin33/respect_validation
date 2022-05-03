from respect_validation.Exceptions.GroupedValidationException import GroupedValidationException


class AllOfException(GroupedValidationException):

    _default_templates = {
        'default': {
            'none': 'All of the required rules must pass for {name}',
            'some': 'These rules must pass for {name}'
        },
        'negative': {
            'none': 'None of there rules must pass for {name}',
            'some': 'These rules must not pass for {name}'
        },
    }
