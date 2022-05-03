from respect_validation.Exceptions.ValidationException import ValidationException
from respect_validation.Rules.AllOf import AllOf
from respect_validation.Factory import Factory


class MetaValidator(type):
    """In case if you use Validator Statically"""

    def __getattr__(self, method):
        "doc __getattr__"
        return Validator().__getattr__(method)


class Validator(AllOf, metaclass=MetaValidator):
    """class Validator"""

    def __getattr__(self, method):
        "doc __getattr__"

        def _add_rule(*args, **kwargs):
            """create dynamic validation rule and put into _rule list"""
            self.add_rule(Factory.get_default_instance().rule(method, *args, **kwargs))
            return self
        return _add_rule

    def check(self, input_val):
        try:
            super().check(input_val=input_val)
        except ValidationException as e:
            if len(self.get_rules()) == 1 and self._template:
                e.update_template(self._template)
            raise e
