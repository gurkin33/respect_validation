from respect_validation.Rules.AbstractRule import AbstractRule


class AbstractSearcher(AbstractRule):

    def _get_data_source(self):
        return []

    def validate(self, input_val):
        data_source = self._get_data_source()
        if input_val in [None, ''] and len(data_source) == 0:
            return True

        return input_val in data_source
