from respect_validation.Exceptions import NestedValidationException


class Validator:

    _errors: list = []
    _error_messages: dict = {}

    def validate(self, request: dict, rules: dict, check_unknown: bool = False, templates: dict = {}) -> 'Validator':
        self._errors = []
        self._error_messages = {}
        received_fields = list(request.keys())
        if check_unknown:
            self._error_messages["_unknown_"] = []

        for field, rule in rules.items():
            self._error_messages[field] = None

            item = request.get(field, None)

            try:
                if rule.get_name() is None:
                    rule.set_name(field[0].upper() + field[1:])
                rule.claim(item)
            except NestedValidationException as nve:
                self._errors.append(nve.get_messages(templates))
                self._error_messages[field] = nve.get_messages(templates)
            if field in received_fields: received_fields.remove(field)

        if check_unknown and len(received_fields):
            for f in received_fields:
                self._error_messages["_unknown_"].append("Unknown field {}".format(f))
                self._errors.append("Unknown field {}".format(f))

        return self

    def failed(self) -> bool:
        return len(self._errors) > 0

    def get_messages(self) -> dict:
        return self._error_messages
