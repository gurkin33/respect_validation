import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.UuidException import UuidException

UUID_VERSION_1 = 'e4eaaaf2-d142-11e1-b3e4-080027620cdd'
UUID_VERSION_3 = '11a38b9a-b3da-360f-9353-a5a725514269'
UUID_VERSION_4 = '25769c6c-d34d-4bfe-ba98-e0ee856f3e7a'
UUID_VERSION_5 = 'c4a760a8-dbcf-5254-a0d9-6a4474bd1b62'


@pytest.mark.parametrize('uuid_ver, value', [
    [None, UUID_VERSION_1],
    [None, UUID_VERSION_3],
    [None, UUID_VERSION_4],
    [None, UUID_VERSION_5],
    [(1,), UUID_VERSION_1],
    [(3,), UUID_VERSION_3],
    [(4,), UUID_VERSION_4],
    [(5,), UUID_VERSION_5],
])
def test_success_uuid(uuid_ver, value):
    if uuid_ver:
        assert v.uuid(*uuid_ver).validate(value)
        assert v.uuid(*uuid_ver).check(value) is None
        assert v.uuid(*uuid_ver).claim(value) is None
    else:
        assert v.uuid().validate(value)
        assert v.uuid().check(value) is None
        assert v.uuid().claim(value) is None


@pytest.mark.parametrize('uuid_ver, value', [
    [None, ''],
    [None, '00000000-0000-0000-0000-000000000000'],
    [None, 'Not an UUID'],
    [None, 'g71a18f4-3a13-11e7-a919-92ebcb67fe33'],
    [None, 'a71a18f43a1311e7a91992ebcb67fe33'],
    [(1, ), UUID_VERSION_3],
    [(1, ), UUID_VERSION_4],
    [(1, ), UUID_VERSION_5],
    [(3, ), UUID_VERSION_1],
    [(3, ), UUID_VERSION_4],
    [(3, ), UUID_VERSION_5],
    [(4, ), UUID_VERSION_1],
    [(4, ), UUID_VERSION_3],
    [(4, ), UUID_VERSION_5],
    [(5, ), UUID_VERSION_1],
    [(5, ), UUID_VERSION_3],
    [(5, ), UUID_VERSION_4],
    [None, []],
    [None, True],
    [None, False],
    [None, bool()],
])
def test_fail_uuid(uuid_ver, value):
    if uuid_ver:
        assert v.uuid(*uuid_ver).validate(value) is False

        with pytest.raises(UuidException, match=r' must be a valid UUID'):
            assert v.uuid(*uuid_ver).check(value)
            assert v.uuid(*uuid_ver).claim(value)
    else:
        assert v.uuid().validate(value) is False

        with pytest.raises(UuidException, match=r' must be a valid UUID'):
            assert v.uuid().check(value)
            assert v.uuid().claim(value)


@pytest.mark.parametrize('uuid_ver, value', [
    [(6, ), UUID_VERSION_3],
    [([], ), UUID_VERSION_4],
    [(False, ), UUID_VERSION_5],
    [('AAA', ), UUID_VERSION_5],
])
def test_fail_uuid2(uuid_ver, value):
    with pytest.raises(ComponentException, match=r'Only versions 1, 3, 4, and 5 are'):
        assert v.uuid(*uuid_ver).validate(value) is False
        assert v.uuid(*uuid_ver).check(value)
        assert v.uuid(*uuid_ver).claim(value)
