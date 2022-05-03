import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.LanguageCodeException import LanguageCodeException
from respect_validation.Rules.LanguageCode import LanguageCode


@pytest.mark.parametrize('code_type, value', [
    [LanguageCode.ALPHA2, 'en'],
    [LanguageCode.ALPHA2, 'it'],
    [LanguageCode.ALPHA2, 'la'],
    [LanguageCode.ALPHA2, 'pt'],
    [LanguageCode.ALPHA3, 'eng'],
    [LanguageCode.ALPHA3, 'ita'],
    [LanguageCode.ALPHA3, 'lat'],
    [LanguageCode.ALPHA3, 'por'],
])
def test_success_languageCode(code_type, value):
    assert v.languageCode(code_type).validate(value)
    assert v.languageCode(code_type).check(value) is None
    assert v.languageCode(code_type).claim(value) is None


@pytest.mark.parametrize('code_type, value', [
    [LanguageCode.ALPHA2, 'por'],
    [LanguageCode.ALPHA2, False],
    [LanguageCode.ALPHA2, []],
    [LanguageCode.ALPHA2, ''],
    [LanguageCode.ALPHA2, None],
    [LanguageCode.ALPHA3, 'pt'],
    [LanguageCode.ALPHA3, True],
    [LanguageCode.ALPHA3, []],
    [LanguageCode.ALPHA3, ''],
    [LanguageCode.ALPHA3, None],
])
def test_fail_languageCode(code_type, value):
    assert v.languageCode(code_type).validate(value) is False

    with pytest.raises(LanguageCodeException, match=r'must be a valid ISO 639 alpha-\d language code'):
        assert v.languageCode(code_type).check(value)
        assert v.languageCode(code_type).claim(value)
