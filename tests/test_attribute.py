import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException, NestedValidationException


class UserSubInfo:
    address: str
    phone: str
    zip: int

    def __init__(self, address: str = None, phone: str = None, zip: int = None):
        self.address = '' if address is None else address
        self.phone = '' if phone is None else phone
        self.zip = 0 if zip is None else zip


class User:
    username: str
    password: str
    user_id: str
    sub_info: UserSubInfo

    def __init__(self, username: str, password: str, id: int = None):
        self.username = username
        self.password = password
        self.sub_info = UserSubInfo()


def test_success_attribute():
    user1 = User('Alexey', "Password")
    user1.sub_info.address = "Kovrov"
    user1.sub_info.phone = "56565"
    user1.sub_info.zip = 123123

    v_test = v.attribute("username", v.stringType().length(3, 10)). \
        attribute("password",
                  v.stringType().length(6, 20)).attribute("sub_info",
                                                          v.attribute("address",
                                                                      v.stringType()).
                                                          attribute("phone", v.stringType()).attribute("zip", v.intType()))
    assert v_test.check(user1) is None
    assert v_test.claim(user1) is None
    assert v_test.validate(user1)


def test_fail_attribute():
    user1 = User('Alexey Mochalin', "123")
    user1.sub_info.address = 33
    user1.sub_info.phone = list()
    user1.sub_info.zip = 123123

    v_test = v.attribute("username", v.stringType().length(3, 10)). \
        attribute("password", v.stringType().length(6, 20)). \
        attribute("sub_info",
                  v.attribute("address",
                              v.stringType()).attribute("phone", v.stringType()).attribute("zip", v.intType()))
    assert v_test.validate(user1) is False

    with pytest.raises(ValidationException):
        assert v_test.check(user1)
    try:
        v_test.claim(user1)
    except NestedValidationException as nve:
        # print(nve.get_messages())
        assert nve.get_messages() == {'attribute': ['Attribute username must be valid', {
            'allOf': ['All of the required rules must pass for username',
                      {'length': ['username must have a length between 3 and 10']}]}, {
                                                        'allOf': ['All of the required rules must pass for password', {
                                                            'length': [
                                                                'password must have a length between 6 and 20']}]}, {
                                                        'allOf': ['All of the required rules must pass for sub_info', {
                                                            'attribute': ['Attribute address must be valid', {'allOf': [
                                                                'All of the required rules must pass for address',
                                                                {'stringType': ['address must be of type string']}]}, {
                                                                              'allOf': [
                                                                                  'All of the required rules must pass for phone',
                                                                                  {'stringType': [
                                                                                      'phone must be of type string']}]}]}]}]}

        # {'attribute':
        #      ['Attribute usernam must be valid',
        #       {'allOf':
        #            ['All of the required rules must pass for username',
        #             {'length':
        #                  ['username must have a length between 3 and 10']}]},
        #       {'allOf':
        #            ['All of the required rules must pass for password',
        #             {'length':
        #                  ['password must have a length between 6 and 20']}]},
        #       {'allOf':
        #            ['All of the required rules must pass for sub_info',
        #             {'attribute':
        #                  ['Attribute address must be valid',
        #                   {'allOf':
        #                        ['All of the required rules must pass for address',
        #                         {'stringType':
        #                              ['address must be of type string']}]},
        #                   {'allOf':
        #                        ['All of the required rules must pass for phone',
        #                         {'stringType': ['phone must be of type string']}]}
        #                   ]}]}]}
