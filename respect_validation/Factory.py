from typing import Dict, Any

from respect_validation.Exceptions.ValidationException import ValidationException
from respect_validation.Exceptions.ComponentException import ComponentException


class Factory(object):

    default_instance = None

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
        #
        # here we have to set "formatter"
        #
        formatter: Dict[Any, Any] = {}
        rule_name = str(type(rule).__name__)
        if rule_name == 'Validator':
            rule_name = 'AllOf'
        params = {
            'input': input,
        }
        params = {**params, **self.extract_properties(rule)}
        params = {**params, **extra_params}
        _id = rule_name[0].lower() + rule_name[1:]
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
                return mod(input, _id, params, formatter)  # type: ignore
            except Exception:
                continue
        return ValidationException(input, _id, params, formatter)

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
