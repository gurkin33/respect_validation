import pytest
import respect_validation.Validator as v


@pytest.mark.parametrize('value', [
    '6',
    'String',
    1.0,
    42,
    False,
    True
])
def test_success_stringVal(value):
    assert v.stringVal().validate(value)
    assert v.stringVal().check(value) is None
    assert v.stringVal().claim(value) is None

# Do we have value which we cannot convert to string? I don't know :)
#
# @pytest.mark.parametrize('value', [
#     b'0x12'
# ])
# def test_fail_stringVal(value):
#     assert v.stringVal().validate(value) is False
#
#     with pytest.raises(StringValException, match=r' is not considered as'):
#         assert v.stringVal().check(value)
#         assert v.stringVal().claim(value)
