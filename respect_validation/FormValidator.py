from typing import Dict, Any, List

from respect_validation.Exceptions import NestedValidationException


class FormValidator(object):
    _errors: List[Any] = []
    _error_messages: Dict[str, Any] = {}

    def validate(self, request: Dict[str, Any], rules: Dict[str, Any], check_missed: bool = False,
                 check_unknown: bool = True, templates: Dict[str, str] = {}) -> 'FormValidator':
        self._errors = []
        self._error_messages = {}
        received_fields = list(request.keys())

        if check_unknown:
            self._error_messages["_unknown_"] = None

        for field, rule in rules.items():
            self._error_messages[field] = None

            if check_missed and field not in received_fields:
                self._errors.append({field: ["Item {} must be present".format(field)]})
                self._error_messages[field] = ["Item {} must be present".format(field)]
                continue

            item = request.get(field, None)

            try:
                if rule.get_name() is None:
                    rule.set_name(field[0].upper() + field[1:])
                rule.claim(item)
            except NestedValidationException as nve:
                self._errors.append(nve.get_messages(templates))
                self._error_messages[field] = nve.get_messages(templates)

            if field in received_fields:
                received_fields.remove(field)

        if check_unknown and len(received_fields):
            self._error_messages["_unknown_"] = []
            for f in received_fields:
                self._error_messages["_unknown_"].append("Unknown field {}".format(f))

        if self._error_messages.get("_unknown_"):
            self._errors.append({"_unknown_": self._error_messages.get("_unknown_")})

        return self

    def failed(self) -> bool:
        return len(self._errors) > 0

    def get_errors(self):
        return self._errors

    def get_messages(self) -> Dict[str, Any]:
        return self._error_messages
