from respect_validation.Rules.AbstractRule import AbstractRule


class Instance(AbstractRule):

    _instance_name = None

    def __init__(self, instance_name: str):
        super().__init__()
        self._instance_name = instance_name
        self.set_param('instance_name', instance_name)

    def validate(self, input_val):

        return type(input_val).__name__ == self._instance_name
