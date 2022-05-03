from respect_validation.Rules.AbstractFilterRule import AbstractFilterRule


class Alpha(AbstractFilterRule):

    def validate_filtered_input(self, input_val: str):

        return input_val.isalpha()
