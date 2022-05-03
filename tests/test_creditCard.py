import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.CreditCardException import CreditCardException
from respect_validation.Rules.CreditCard import CreditCard


@pytest.mark.parametrize('card_type, value', [
    [None, 5555444433331111],  # MasterCard 5 BIN Range
    [None, '5376 7473 9720 8720'],  # MasterCard 5 BIN Range
    [CreditCard.MASTERCARD, '5376 7473 9720 8720'],
    [None, '2223000048400011'],  # MasterCard 2 BIN Range
    [CreditCard.MASTERCARD, '2222 4000 4124 0011'],
    [None, '4024.0071.5336.1885'],  # Visa 16
    [CreditCard.VISA, '4024.0071.5336.1885'],
    [None, '4024 007 193 879'],  # Visa 13
    [CreditCard.VISA, '4024 007 193 879'],
    [None, '340-3161-9380-9364'],  # American Express
    [CreditCard.AMERICAN_EXPRESS, '340-3161-9380-9364'],
    [None, '30351042633884'],  # Diners Club
    [CreditCard.DINERS_CLUB, '30351042633884'],
    [None, '6011000990139424'],  # Discover
    [CreditCard.DISCOVER, '6011000990139424'],
    [None, '3566002020360505'],  # JBC
    [CreditCard.JCB, '3566002020360505'],
])
def test_success_creditCard(card_type, value):
    if card_type:
        assert v.creditCard(card_type).validate(value)
        assert v.creditCard(card_type).check(value) is None
        assert v.creditCard(card_type).claim(value) is None
    else:
        assert v.creditCard().validate(value)
        assert v.creditCard().check(value) is None
        assert v.creditCard().claim(value) is None


@pytest.mark.parametrize('card_type,value', [
    [None, ''],
    [None, None],
    [None, 'it isnt my credit card number'],
    [None, '&stR@ng3|) (|-|@r$'],
    [None, '1234 1234 1234 1234'],
    [None, '1234.1234.1234.1234'],
    [CreditCard.MASTERCARD, '6011111111111117'],  # Discover
    [CreditCard.VISA, '3530111333300000'],  # JCB
    [CreditCard.AMERICAN_EXPRESS, '5555555555554444'],  # MasterCard
    [CreditCard.DINERS_CLUB, '4012888888881881'],  # Visa
    [CreditCard.DISCOVER, '371449635398431'],  # American Express
    [CreditCard.JCB, '38520000023237'],  # Diners Club
])
def test_fail_creditCard(card_type, value):
    if card_type:
        assert v.creditCard(card_type).validate(value) is False
        with pytest.raises(CreditCardException, match="must be a valid .* Credit Card number"):
            assert v.creditCard(card_type).check(value)
            assert v.creditCard(card_type).claim(value)
    else:
        assert v.creditCard().validate(value) is False
        with pytest.raises(CreditCardException, match="must be a valid .* Credit Card number"):
            assert v.creditCard().check(value)
            assert v.creditCard().claim(value)


def test_fail_creditCard2():
    with pytest.raises(ComponentException, match='"123123" is not a valid credit card brand \\(Available:'):
        assert v.creditCard('123123').validate('test')
        assert v.creditCard('123123').check('test')
        assert v.creditCard('123123').claim('test')
