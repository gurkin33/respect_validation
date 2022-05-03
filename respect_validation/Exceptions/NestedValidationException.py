from typing import Dict, Any

from respect_validation.Exceptions.ValidationException import ValidationException


class NestedValidationException(ValidationException):

    def __init__(self, input, _id, params, formatter):
        super().__init__(input, _id, params, formatter)
        self._parsed_exceptions = ''
        self._nested_messages = []
        self._exceptions = []

    def get_children(self):
        return self._exceptions

    def add_child(self, exception):
        if self.get_param('name') and not exception.get_param('name'):
            exception.set_param('name', self.get_param('name'))
        self._exceptions.append(exception)

        return self

    def add_children(self, exceptions):
        for ex in exceptions:
            self.add_child(ex)
        return self

    def get_messages(self, templates: Dict[str, Any] = {}, simple: bool = False):
        messages: Dict[str, Any] = dict()
        if not simple:
            messages = self._get_children_messages(templates)
        else:
            for ex in self.get_children():
                ex_id = ex.get_id()
                if isinstance(ex, NestedValidationException) and len(ex.get_children()):
                    messages[ex_id] = self._get_nested_messages(templates, ex.get_children())[0]
                    self._nested_messages = []
                    continue
                messages[ex_id] = str(self.render_message(ex, templates))
        return messages

    def _get_children_messages(self, templates: Dict[str, Any]) -> Dict[str, Any]:
        messages: Dict[str, Any] = dict()
        for ex in self.get_children():
            if isinstance(ex, NestedValidationException) and len(ex.get_children()):
                if messages.get(ex.get_id(), False):
                    messages[ex.get_id()].append(ex._get_children_messages(templates))
                else:
                    messages[ex.get_id()] = [str(ex), ex._get_children_messages(templates)]
                continue
            if messages.get(ex.get_id(), False):
                messages[ex.get_id()].append(str(self.render_message(ex, templates)))
            else:
                messages[ex.get_id()] = [str(self.render_message(ex, templates))]
        return messages

    def _get_nested_messages(self, templates: Dict[str, Any], exceptions):
        for e in exceptions:
            if isinstance(e, NestedValidationException) and len(e.get_children()):
                self._get_nested_messages(templates, e.get_children())
                continue
            self._nested_messages.append(str(self.render_message(e, templates)))
        return self._nested_messages

    def get_full_message(self):
        self._parsed_exceptions = "- {}\n".format(str(self))
        self._exception_parser(self.get_children())
        return self._parsed_exceptions

    def _exception_parser(self, exceptions, level: int = 0):
        for e in exceptions:
            if isinstance(e, NestedValidationException) and len(e.get_children()):
                self._parsed_exceptions += " " * int(level+2) + "- {}\n".format(e)
                self._exception_parser(e.get_children(), (level + 2))
                continue
            self._parsed_exceptions += " " * int(level+2) + "- {}\n".format(e)
        return self._parsed_exceptions

    def render_message(self, exception, templates: Dict[str, Any] = {}):
        if templates.get(exception.get_id(), False) and isinstance(templates[exception.get_id()], str):
            exception.update_template(templates[exception.get_id()])
        return exception
