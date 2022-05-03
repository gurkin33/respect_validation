from respect_validation.Exceptions.GroupedValidationException import GroupedValidationException


class KeySetException(GroupedValidationException):

    STRUCTURE = 'structure'

    _default_templates = {
        'default': {
            'none': 'All of the required rules must pass for {name}',
            'some': 'These rules must pass for {name}',
            'structure': 'Must have keys {keys}',
        },
        'negative': {
            'none': 'None of these rules must pass for {name}',
            'some': 'These rules must not pass for {name}',
            'structure': 'Must not have keys {keys}',
        }
    }

    def choose_template(self):
        if len(self.get_children()) == 0:
            return self.STRUCTURE

        return super().choose_template()
