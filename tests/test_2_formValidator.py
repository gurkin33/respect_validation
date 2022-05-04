from respect_validation import FormValidator as fv, Validator as v

rules = {
    "username": v.stringType().alnum().noWhitespace().length(4, 64),
    "email": v.optional(v.email()),
    "password": v.stringType().length(8, 64)
}


def test_success_fv():
    user_data = {
        "username": "gurkin33",
        "email": "gurkin33@mail.com",
        "password": "123123123",
    }

    form_validation = fv()
    form_validation.validate(request=user_data, rules=rules)

    assert form_validation.failed() is False

    for k, val in form_validation.get_messages().items():
        assert val is None

    assert len(form_validation.get_errors()) == 0


def test_success_fv_unknown():
    user_data = {
        "username": "gurkin33",
        "email": "gurkin33@mail.com",
        "password": "123123123",
        "personal_id": "123123123",
        "first_name": "123123123",
    }

    form_validation = fv()
    form_validation.validate(request=user_data, rules=rules, check_unknown=False)

    assert form_validation.failed() is False

    for k, val in form_validation.get_messages().items():
        assert val is None

    assert len(form_validation.get_errors()) == 0


def test_fail_fv_unknown():
    user_data = {
        "username": "gurkin33",
        "email": "gurkin33@mail.com",
        "password": "123123123",
        "personal_id": "123123123",
        "first_name": "123123123",
    }

    form_validation = fv()
    form_validation.validate(request=user_data, rules=rules)

    assert form_validation.failed() is True

    for k, val in form_validation.get_messages().items():
        if k == "_unknown_":
            assert val[0] == 'Unknown field personal_id'
            assert val[1] == 'Unknown field first_name'
            continue
        assert val is None

    assert len(form_validation.get_errors()) == 1


def test_fail_fv_empty():
    user_data = {
        "username": "",
        "email": "",
        "password": "",
    }

    form_validation = fv()
    form_validation.validate(request=user_data, rules=rules)

    assert form_validation.failed() is True

    for k, val in form_validation.get_messages().items():
        if k in ["email", "_unknown_"]:
            assert val is None
            continue
        assert (isinstance(val, list) or isinstance(val, dict)) and len(val)

    assert len(form_validation.get_errors()) == 2


def test_fail_fv_empty2():
    user_data = {}

    form_validation = fv()
    form_validation.validate(request=user_data, rules=rules)

    assert form_validation.failed() is True

    for k, val in form_validation.get_messages().items():
        if k in ["email", "_unknown_"]:
            assert val is None
            continue
        assert (isinstance(val, list) or isinstance(val, dict)) and len(val)

    assert len(form_validation.get_errors()) == 2


def test_fail_fv_missed():
    user_data = {}

    form_validation = fv()
    form_validation.validate(request=user_data, rules=rules, check_missed=True)

    assert form_validation.failed() is True

    for k, val in form_validation.get_messages().items():
        if k == "_unknown_":
            assert val is None
            continue
        assert 'must be present' in val[0]

    assert len(form_validation.get_errors()) == 3
