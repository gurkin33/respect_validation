from datetime import datetime
from typing import Optional


class CanValidateDateTime:

    def _is_date_time(self, date_format: Optional[str] = None, value: Optional[str] = None):
        try:
            return bool(datetime.strptime(str(value), str(date_format)))
        except Exception:
            return False

    def _is_iso_format(self, value: Optional[str] = None):
        try:
            return bool(datetime.fromisoformat(str(value)))
        except Exception:
            return False

    def _is_date_format(self, date_format):
        b_day = 1657598400
        try:
            return str(datetime.fromtimestamp(b_day).strftime(date_format)) == datetime.strptime(
                str(datetime.fromtimestamp(b_day).strftime(date_format)), date_format).strftime(date_format)
        except Exception:
            return False
