import re

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.RegexException import RegexException


@pytest.mark.parametrize('regex, value', [
    [r'^[a-z]+$', 'wpoiur'],
    [re.compile(r'^[a-z]+$', re.IGNORECASE), 'wPoiur'],
])
def test_success_regex(regex, value):
    assert v.regex(regex).validate(value)
    assert v.regex(regex).check(value) is None
    assert v.regex(regex).claim(value) is None


@pytest.mark.parametrize('regex,value', [
    [r'^w+$', 'w poiur'],
    [r'^w+$', object()],
    [r'^w+$', []],
    [re.compile(r'^[0-9]+$', re.IGNORECASE), 42],
])
def test_fail_regex(regex, value):
    assert v.regex(regex).validate(value) is False

    with pytest.raises(RegexException, match=r' must validate against '):
        assert v.regex(regex).check(value)
        assert v.regex(regex).claim(value)
