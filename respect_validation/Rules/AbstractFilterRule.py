from respect_validation.Rules.AbstractRule import AbstractRule


class AbstractFilterRule(AbstractRule):

    def validate_filtered_input(self, input_val) -> bool:
        return False

    def __init__(self, *additional_chars: str):
        super().__init__()
        self.set_param('additional_chars', str(''.join(additional_chars)))

    def validate(self, input_val) -> bool:

        if input_val is None:
            return False
        input_val = str(input_val)
        if input_val == '':
            return False

        filtered_input = self._filter(str(input_val))
        return filtered_input == '' and self.get_param('additional_chars') or self.validate_filtered_input(filtered_input)

    def _filter(self, input_val: str) -> str:
        if not self.get_param('additional_chars') or not isinstance(self.get_param('additional_chars'), str):
            return input_val
        for s in list(self.get_param('additional_chars')):
            input_val = input_val.replace(s, '')
        return input_val
