import re
from typing import Optional, Union

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class Uuid(AbstractRule):

    _version: Union[Optional[int], Optional[str]] = None

    PATTERN_FORMAT = '^[0-9a-f]{8}-[0-9a-f]{4}-%s[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'

    def __init__(self, version: Union[Optional[int], Optional[str]] = None):
        super().__init__()
        self._version = version

        if isinstance(version, str) and not version.isdigit():
            raise ComponentException('Only versions 1, 3, 4, and 5 are supported: %s given' % str(version)) from None

        if version is not None and not isinstance(version, str) and not isinstance(version, int):
            raise ComponentException('Incorrect version type. Only versions 1, 3, 4, and 5 are supported: %s given' % str(version)) from None

        if version is not None and not self._is_supported_version(int(version)):
            raise ComponentException('Only versions 1, 3, 4, and 5 are supported: %s given' % str(version)) from None
        if version:
            self.set_param('version', version)

    def validate(self, input_val) -> bool:
        if not isinstance(input_val, str):
            return False

        return bool(re.search(self._get_pattern(), input_val))

    def _is_supported_version(self, version: int) -> bool:
        return 1 <= version <= 5 and version != 2

    def _get_pattern(self):

        if self._version is not None:
            return re.compile(
                self.PATTERN_FORMAT % str(self._version), re.IGNORECASE)

        return re.compile(self.PATTERN_FORMAT % '[13-5]', re.IGNORECASE)
