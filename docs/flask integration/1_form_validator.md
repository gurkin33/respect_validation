# Form Validator

Class `FormValidator` is a helper class to validate incoming requests.

## FormValidator methods

There are several methods in `FormValidator`:

- `validate(request: Dict[str, Any], rules: Dict[str, Any], check_missed: bool = False,
check_unknown: bool = True, templates: Dict[str, str] = {})` - the main action method, I will describe 
  arguments in the section below. It returns itself (FormValidation instance)
- `failed()` - returns `True` if a validation failed, else `False`
- `get_errors()` - returns list of all validation errors, if there are no errors, it returns empty list (`[]`) 
- `get_messages()` - returns dictionary with validation errors related to keys in provided rules, if rule doesn't have 
errors, then value of key will be `None`.

## FormValidator validate arguments

Method validate has several arguments:

- `request: Dict[str, Any]` - data received from form. Must be a dictionary.
- `rules: Dict[str, Any]` - it is a dictionary where keys must much with keys of *request*, values of this 
  dictionary are validation rules.
- `check_missed: bool = False` - check if *request* doesn't have one or more keys which are available in 
  *rules*. If `False` all missed keys have `None` as a value, else keys treated as failed and have this 
  error message - Item *key_name* must be present.
- `check_unknown: bool = True` - check if some addition keys appeared in *request* which are not present 
  in *rules*. If `True` addition key appears in messages - `_unknown_`.
- `templates: Dict[str, str] = {}` - dictionary of templates which must be applied to rule exceptions, 
[here are more details](../feature-guide.md#custom-messages).

## Examples of usage

### Successful validation

```python
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
```
Output
```text
# form_validation.failed()
False

# form_validation.get_messages()
{'_unknown_': None, 'username': None, 'email': None, 'password': None}

# form_validation.get_errors()
[]
```
---
### Unexpected field in request

```python
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
```
Output
```text
# form_validation.failed()
True

# form_validation.get_messages()
{'_unknown_': ['Unknown field personal_id'], 'username': None, 'email': None, 'password': None}

# form_validation.get_errors()
[{'_unknown_': ['Unknown field personal_id']}]
```
---
### Missed field in request (with check)

```python
user_data = {
    "username": "gurkin33",
    "email": "gurkin33@mail.com",
}

form_validation = fv()
form_validation.validate(request=user_data, rules=rules, check_missed=True)

print(form_validation.failed())
print(form_validation.get_messages())
print(form_validation.get_errors())
```
Output
```text
# form_validation.failed()
True

# form_validation.get_messages()
{'_unknown_': None, 'username': None, 'email': None, 'password': ['Item password must be present']}

# form_validation.get_errors()
[{'password': ['Item password must be present']}]
```

Now we can go to integration with [simple flask app](./2_simple_flask.md).