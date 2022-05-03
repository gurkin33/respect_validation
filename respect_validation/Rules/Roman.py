from respect_validation.Rules.AbstractEnvelope import AbstractEnvelope
from respect_validation.Rules.Regex import Regex


class Roman(AbstractEnvelope):

    def __init__(self):
        super().__init__(
            Regex(r'^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$')
        )
