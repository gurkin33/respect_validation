from typing import Any

from respect_validation.Exceptions import ValidationException
from respect_validation.Rules.AbstractRule import AbstractRule


class Call(AbstractRule):

    _callable: Any = None
    _rule: AbstractRule

    def __init__(self, callable_fun: Any, rule: AbstractRule):
        super().__init__()
        self._callable = None

        if callable(callable_fun):
            self.set_param('callable', type(callable_fun).__name__)
            self._callable = callable_fun
        elif isinstance(callable_fun, str):
            self.set_param('callable', callable_fun)
            self._callable = callable_fun
        else:
            raise self.report_error('Callable function or method')

        self._rule = rule

    def claim(self, input_val) -> None:
        try:
            if callable(self._callable):
                self._rule.claim(self._callable(input_val))
            elif isinstance(self._callable, str) and hasattr(input_val, self._callable) and callable(getattr(input_val, self._callable)):
                self._rule.claim(getattr(input_val, self._callable)())
            else:
                raise self.report_error('Callable function or method')
        except ValidationException as ve:
            raise ve from None
        except Exception:
            raise self.report_error(input_val) from None

    def check(self, input_val) -> None:

        try:
            if callable(self._callable):
                self._rule.check(self._callable(input_val))
            elif isinstance(self._callable, str) and hasattr(input_val, self._callable) and callable(
                    getattr(input_val, self._callable)):
                self._rule.check(getattr(input_val, self._callable)())
            else:
                raise self.report_error('Callable function or method')
        except ValidationException as ve:
            raise ve from None
        except Exception:
            raise self.report_error(input_val) from None

    def validate(self, input_val) -> bool:
        try:
            self.check(input_val)
        except ValidationException:
            return False
        return True
