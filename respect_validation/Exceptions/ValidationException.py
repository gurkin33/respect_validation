from typing import Dict, Any


class ValidationException(Exception):

    MODE_DEFAULT = 'default'
    MODE_NEGATIVE = 'negative'
    STANDARD = 'standard'

    _input = None
    _id: str = ''
    _mode = 'default'
    _params: Dict[str, Any] = {}
    _formatter = None
    _template = 'standard'
    _message = None

    _default_templates = {
        'default': {
            'standard': '{name} must be valid'
        },
        'negative': {
            'standard': '{name} must not be valid'
        },
    }

    def __init__(self, input, _id, params, formatter):
        self._mode = self.MODE_DEFAULT
        self._exceptions = list()
        self._input = input
        self._id = _id
        self._params = params
        self._formatter = formatter
        self._template = self.choose_template()

        if not self._params.get('name', False):
            self._params['name'] = '"'+str(input)+'"'
        super().__init__(self._create_message().format(**params))

    def choose_template(self) -> str:
        return list(self._default_templates[self._mode].keys())[0]

    def refresh_template(self) -> 'ValidationException':
        self._template = self.choose_template()
        return self

    def _create_message(self) -> str:
        #
        # here should be formatter
        #
        if not self._default_templates[self._mode].get(self._template, False):
            return self._template
        return self._default_templates[self._mode][self._template]

    def get_message(self) -> str:
        return str(self)

    def get_id(self) -> str:
        return self._id

    def get_params(self) -> Dict[str, Any]:
        return self._params

    def get_param(self, name: str):
        return self._params.get(name, None)

    def set_param(self, param_name: str, param_val) -> 'ValidationException':
        self._params[param_name] = param_val
        return self

    def update_params(self, params: Dict[str, Any]) -> None:
        self._params = params
        self._message = self._create_message()
        return

    def update_mode(self, mode: str) -> None:
        self._mode = mode
        self._message = self._create_message()
        return

    def update_template(self, template: str) -> None:
        self._template = template
        self._message = self._create_message()
        return

    def has_customer_template(self) -> bool:
        return bool(self._default_templates[self._mode].get(self._template, False))

    def __str__(self):
        return str(self._create_message().format(**self._params))
