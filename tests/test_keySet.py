import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException, NestedValidationException


@pytest.mark.parametrize('keySet, value', [
    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90))),
     {'foo': 42, 'bar': 73}],
    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90)),
      v.key('baz', v.intVal().Between(1, 100).max(90), False)),
     {'foo': 42, 'bar': 73}]
])
def test_success_keySet(keySet, value):
    assert v.keySet(*keySet).validate(value)
    assert v.keySet(*keySet).check(value) is None
    assert v.keySet(*keySet).claim(value) is None


@pytest.mark.parametrize('keySet, value', [
    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90))),
     {'foo': 42, 'bar': 120}],

    [(v.key('foo', v.intVal().Between(1, 100).max(90)),),
     {'foo': 42, 'bar': 120}],

    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90))),
     {'foo': 42}],

    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90))),
     {}],
    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90)),
      v.key('baz', v.intVal().Between(1, 100).max(90))),
     {'foo': 42, 'bar': 73}]
])
def test_fail_keySet(keySet, value):
    assert v.keySet(*keySet).validate(value) is False

    with pytest.raises(ValidationException, match=r'(Must have keys|bar must be between 1 and 100)'):
        assert v.keySet(*keySet).check(value)
        assert v.keySet(*keySet).claim(value)


def test_issue_success_keySet():
    info = {
        'status': True,
        'serial': '1123-3333-222',
        'hostname': 'hello.og.local',
        'ipaddr': '11.11.0.11',
        'wr': 0, 'rd': 0,
        'max_pkt': 3000,
        'wr_empty': 3000,
        'speed': 0,
        'save_image': 0,
        'save_avail':
        0, 'save_free': 439,
        'save_flines': 262099,
        'buffer_wr': 356250,
        'buffer_rd': 65803, 'error': ''
    }

    assert v.keySet(
        v.key('status', v.boolType().trueVal()),
        v.key('serial', v.stringType().Min(5)),
        v.key('hostname', v.stringType().Min(5)),
        v.key('ipaddr', v.stringType().Min(5)),

        v.key('wr', v.intType().Min(0)),
        v.key('rd', v.intType().Min(0)),
        v.key('max_pkt', v.intType().Min(0)),
        v.key('wr_empty', v.intType().Min(0)),
        v.key('speed', v.intType().Min(0)),
        v.key('save_image', v.intType().Min(0)),
        v.key('save_avail', v.intType().Min(0)),
        v.key('save_free', v.intType().Min(0)),
        v.key('save_flines', v.intType().Min(0)),
        v.key('buffer_wr', v.intType().Min(0)),
        v.key('buffer_rd', v.intType().Min(0)),

        v.key('error', v.stringType()),

    ).claim(info) is None

    try:
        assert v.keySet(
            v.key('status', v.boolType().trueVal()),
            v.key('serial', v.stringType().Min(5)),
            v.key('hostname', v.stringType().Min(5)),
            v.key('ipaddr', v.stringType().Min(5)),

            v.key('wr', v.intType().Min(0)),
            v.key('rd', v.intType().Min(0)),
            v.key('max_pkt', v.intType().Min(0)),
            v.key('wr_empty', v.intType().Min(0)),
            v.key('speed', v.intType().Min(0)),
            v.key('save_image', v.stringType().Min(0)),
            v.key('save_avail', v.stringType().Min(0)),
            v.key('save_free', v.stringType().Min(0)),
            v.key('save_flines', v.stringType().Min(0)),
            v.key('buffer_wr', v.intType().Min(0)),
            v.key('buffer_rd', v.intType().Min(0)),

            v.key('error', v.stringType()),

        ).claim(info)
    except NestedValidationException as nve:
        print(nve.get_messages())
        assert nve.get_messages() == \
               {'allOf': ['All of the required rules must pass for "{\'status\': True, \'serial\': \'1123-3333-222\', '
                          '\'hostname\': \'hello.og.local\', \'ipaddr\': \'11.11.0.11\', \'wr\': 0, \'rd\': 0, '
                          '\'max_pkt\': 3000, \'wr_empty\': 3000, \'speed\': 0, \'save_image\': 0, \'save_avail\': 0, '
                          '\'save_free\': 439, \'save_flines\': 262099, \'buffer_wr\': 356250, \'buffer_rd\': 65803, '
                          '\'error\': \'\'}"', {'key': ['save_image must be valid', {'allOf': ['All of the required '
                                                                                               'rules must pass for '
                                                                                               'save_image',
                                                                                               {'stringType': [
                                                                                                   'save_image must '
                                                                                                   'be of type '
                                                                                                   'string']}]},
                                                        {'allOf': ['All of the required rules must pass for '
                                                                   'save_avail', {'stringType': ['save_avail must be '
                                                                                                 'of type '
                                                                                                 'string']}]},
                                                        {'allOf': ['All of the required rules must pass for '
                                                                   'save_free', {'stringType': ['save_free must be of '
                                                                                                'type string']}]},
                                                        {'allOf': ['All of the required rules must pass for '
                                                                   'save_flines', {'stringType': ['save_flines must '
                                                                                                  'be of type '
                                                                                                  'string']}]}]}]}
