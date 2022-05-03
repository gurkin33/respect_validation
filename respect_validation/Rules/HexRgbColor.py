from respect_validation.Rules.AbstractEnvelope import AbstractEnvelope
from respect_validation.Rules.Regex import Regex


class HexRgbColor(AbstractEnvelope):

    def __init__(self):
        super().__init__(Regex(r'(?i)^#?([0-9A-F]{3}|[0-9A-F]{6})$'))
