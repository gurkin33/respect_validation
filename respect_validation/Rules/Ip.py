from ipaddress import ip_address, ip_network
from typing import Optional

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class Ip(AbstractRule):

    _ip_range = None
    _private = None

    def __init__(self, ip_range: str = '*', private: bool = False):
        super().__init__()
        self._ip_range = ip_range
        self._private = private
        if self._parse_range_and_validate(ip_range):
            self.set_param('ip_range', ip_range)

    def validate(self, input_val: str):
        try:
            ip_addr = ip_address(input_val)
        except Exception:
            self.set_param('ip_range', None)
            return False

        if self._private and not ip_addr.is_private:
            self.set_param('must_be_private', True)
            return False

        if not self.get_param('ip_range'):
            return True
        return self._parse_range_and_validate(self._ip_range, input_val)  # type: ignore

    def _parse_range_and_validate(self, ip_range: str, ip_addr: Optional[str] = None):

        if ip_range == '*':
            return False

        if '-' in ip_range:
            try:
                min_ip = ip_address(str(ip_range.split('-')[0].strip()))
                max_ip = ip_address(str(ip_range.split('-')[1].strip()))
            except Exception:
                raise ComponentException('Invalid network range') from None

            if ip_addr is not None and \
                    (type(min_ip) != type(max_ip) or type(min_ip) != type(ip_address(ip_addr))):  # type: ignore
                raise ComponentException('Incompatible version of IP protocol') from None

            if ip_addr is not None:
                return min_ip <= ip_address(ip_addr) <= max_ip  # type: ignore

            return True

        if '/' in ip_range:
            try:
                network = ip_network(ip_range)
            except Exception:
                raise ComponentException('Invalid network range') from None
            if ip_addr:
                return ip_address(ip_addr) in network
            return True

        raise ComponentException('Invalid network range') from None
