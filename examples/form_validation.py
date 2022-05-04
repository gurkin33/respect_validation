from respect_validation import FormValidator as fv, Validator as v

# rules are the same for all examples below
rules = {
    "username": v.stringType().alnum().noWhitespace().length(4, 64),
    "email": v.optional(v.email()),
    "password": v.stringType().length(8, 64)
}

user_data = {
    "username": "gurkin33",
    "email": "gurkin33@mail.com",
    "password": "123123123",
}

form_validation = fv()
form_validation.validate(request=user_data, rules=rules)

print(form_validation.failed())
print(form_validation.get_messages())
print(form_validation.get_errors())

# Unexpected field in request

user_data = {
    "username": "gurkin33",
    "email": "gurkin33@mail.com",
    "password": "123123123",
    "personal_id": "123123123",
}

form_validation = fv()
form_validation.validate(request=user_data, rules=rules)

print(form_validation.failed())
print(form_validation.get_messages())
print(form_validation.get_errors())

# Missed field in request (with check)

user_data = {
    "username": "gurkin33",
    "email": "gurkin33@mail.com",
}

form_validation = fv()
form_validation.validate(request=user_data, rules=rules, check_missed=True)

print(form_validation.failed())
print(form_validation.get_messages())
print(form_validation.get_errors())
