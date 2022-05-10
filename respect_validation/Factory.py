from typing import Dict, Any, Optional, ClassVar

from respect_validation.Exceptions.ValidationException import ValidationException
from respect_validation.Exceptions.ComponentException import ComponentException


class Factory(object):

    default_instance = None

    _translation: ClassVar[Optional[Dict[str, Any]]] = None
    _default_language: ClassVar[Optional[str]] = None

    rules_packages = ["respect_validation.Rules"]
    exceptions_packages = ["respect_validation.Exceptions"]

    @classmethod
    def get_default_instance(cls):
        if not cls.default_instance:
            cls.default_instance = cls()

        return cls.default_instance

    def rule(self, name: str, *args, **kwargs):
        name = name[0].upper() + name[1:]
        for package in self.rules_packages:
            try:
                fullname = '{}.{}'.format(package, name)
                mod = __import__(fullname)
                components = fullname.split('.')
                for comp in components[1:]:
                    mod = getattr(mod, comp)
                if not hasattr(mod, name):
                    raise ComponentException(
                        "Incorrect name of class in rule module {}.py. It expects to see the same name.".format(name))
                mod = getattr(mod, name)
            except ComponentException as ce:
                raise ComponentException(ce) from None
            except Exception:
                continue

            try:
                return mod(*args, **kwargs)  # type: ignore
            except Exception as e:
                raise e

        raise ComponentException("{} is not a valid rule name".format(name))

    def exception(self, rule, input, extra_params: Dict[str, Any]):

        translation: Optional[Dict[str, Any]] = None

        rule_name = str(type(rule).__name__)
        if rule_name == 'Validator':
            rule_name = 'AllOf'
        params = {
            'input': input,
        }
        params = {**params, **self.extract_properties(rule)}
        params = {**params, **extra_params}
        _id = rule_name[0].lower() + rule_name[1:]

        # One language in translation
        if isinstance(self._translation, dict) and not (self._default_language and params.get('_language_')) and \
                self._translation.get(_id):
            translation = self._translation[_id]

        # Several languages in translation
        if isinstance(self._translation, dict) and (self._default_language or params.get('_language_')):

            if self._default_language and self._translation.get(self._default_language) and \
                    self._translation[self._default_language].get(_id):
                translation = self._translation[self._default_language][_id]

            if params.get('_language_') and self._translation.get(str(params.get('_language_'))) and \
                    self._translation[str(params.get('_language_'))].get(_id):
                translation = self._translation[str(params.get('_language_'))][_id]

        if rule.get_name() not in [None, '']:
            params['name'] = rule.get_name()
        for package in self.exceptions_packages:
            try:
                fullname = '{}.{}Exception'.format(package, rule_name)
                mod = __import__(fullname)
                components = fullname.split('.')
                for comp in components[1:]:
                    mod = getattr(mod, comp)
                mod = getattr(mod, rule_name+'Exception')
                return mod(input, _id, params, translation)  # type: ignore
            except Exception:
                continue
        return ValidationException(input, _id, params, translation)

    def create_validation_exception(self, exception_name: str, _id: str, input_val, params: Dict[str, Any], formatter):
        exception = ValidationException(input, _id, params, formatter)
        if params.get('template', False):
            exception.update_template(params['template'])
        return exception

    def extract_properties(self, rule) -> Any:
        return rule.get_params()

    @classmethod
    def add_rules_packages(cls, *args) -> None:
        cls.rules_packages += args

    @classmethod
    def add_exceptions_packages(cls, *args) -> None:
        cls.exceptions_packages += args

    @classmethod
    def set_translation(cls, translation: Dict[str, Any]):
        cls._translation = translation
        return cls

    @classmethod
    def default_language(cls, language: str):
        cls._default_language = language
        return cls
