from respect_validation import Validator as v


def test_snake_case():
    assert v.string_val().string_type().validate("gurkin33")
    assert v.int_val().int_type().validate(23)
