from typing import Any

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class Callback(AbstractRule):

    _callback: Any
    _args: Any = None
    _kwargs: Any = None

    def __init__(self, callback: Any, *args, **kwargs):
        if not callable(callback):
            raise ComponentException("Callback must be callable") from None
        super().__init__()
        self._callback = callback
        self._args = args
        self._kwargs = kwargs

    def validate(self, input_val):
        args = list(self._args) if self._args else list()
        kwargs = self._kwargs
        if isinstance(input_val, dict):
            kwargs = {**kwargs, **input_val}
        else:
            args.append(input_val)

        return bool(self._callback(*args, **kwargs))
