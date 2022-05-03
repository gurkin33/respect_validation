from respect_validation.Exceptions.NestedValidationException import NestedValidationException


class GroupedValidationException(NestedValidationException):

    NONE = 'none'
    SOME = 'some'

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

    def choose_template(self) -> str:
        num_failed = self.get_param('failed')
        num_rules = len(self.get_children())
        return self.NONE if num_rules == num_failed else self.SOME
