from typing import Optional, Dict, Any
from respect_validation.Factory import Factory


class AbstractRule:

    _name: Optional[str] = None
    _template: Optional[str] = None
    _params: Dict[str, Any] = {}

    def __init__(self):
        self._name = None
        self._template = None
        self._params = dict()

    def claim(self, input_val) -> None:
        if self.validate(input_val):
            return
        raise self.report_error(input_val) from None

    def check(self, input_val) -> None:
        self.claim(input_val)

    def validate(self, input_val) -> bool:
        pass

    def get_name(self) -> Optional[str]:
        return self._name

    def report_error(self, input_val, extra_params: Dict[str, Any] = {}) -> Any:
        return Factory.get_default_instance().exception(self, input_val, extra_params)

    def set_name(self, name: str) -> 'AbstractRule':
        self._name = str(name)
        return self

    def set_template(self, template: str) -> 'AbstractRule':
        self._template = template
        return self

    def set_param(self, param_name: str, param_value) -> 'AbstractRule':
        self._params[param_name] = param_value
        return self

    def get_param(self, param_name: str):
        return self._params.get(param_name, None)

    def get_params(self) -> Dict[str, Any]:
        return self._params
