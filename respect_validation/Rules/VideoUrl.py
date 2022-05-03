import re
from typing import Optional

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class VideoUrl(AbstractRule):

    SERVICES = {
        'youtube': r'^https?://(www\.)?(?:youtube\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)/|.*[?&]v=)|youtu\.be/)([^\"&?/]{11})',
        'vimeo': r'^https?://(www\.)?(player\.)?(vimeo\.com/)((channels/[A-z]+/)|(groups/[A-z]+/videos/)|(video/))?([0-9]+)',
        'twitch': r'^https?://(((www\.)?twitch\.tv/videos/[0-9]+)|clips\.twitch\.tv/[a-zA-Z]+)$',
    }

    _service = None

    def __init__(self, service: Optional[str] = None):
        super().__init__()

        if service is not None and (not isinstance(service, str) or not self._is_supported_service(service)):
            raise ComponentException('"%s" is not a recognized video service' % service) from None
        if service:
            self._service = service.lower()
            self.set_param('service', service)

    def validate(self, input_val) -> bool:
        if not isinstance(input_val, str):
            return False

        if self._service is not None:
            return bool(self._is_valid(self._service, input_val))

        for service in self.SERVICES.keys():
            if not self._is_valid(service, input_val):
                continue
            return True
        return False

    def _is_supported_service(self, service: str) -> bool:
        return service.lower() in self.SERVICES.keys()

    def _is_valid(self, service: str, input_value: str):
        return bool(re.search(re.compile(self.SERVICES[service], re.IGNORECASE), input_value))
