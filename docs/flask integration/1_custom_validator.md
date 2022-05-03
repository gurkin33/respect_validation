# Custom Validator

## Is it legal? 

It can sound wired - custom validator for respect validation, but it is something like helper for integration with 
flask. Let's look.

## New class Validator

Below you can find new Validation class and description. I will use with class for integration with flask.

```python
from respect_validation.Exceptions import NestedValidationException


class Validator:

    _errors: list = []
    _error_messages: dict = {}

    def validate(self, request: dict, rules: dict, check_unknown: bool = False, templates: dict = {}) -> 'Validator':
        self._errors = []
        self._error_messages = {}
        received_fields = list(request.keys())
        if check_unknown:
            self._error_messages["_unknown_"] = []

        for field, rule in rules.items():
            self._error_messages[field] = None

            item = request.get(field, None)

            try:
                if rule.get_name() is None:
                    rule.set_name(field[0].upper() + field[1:])
                rule.claim(item)
            except NestedValidationException as nve:
                self._errors.append(nve.get_messages(templates))
                self._error_messages[field] = nve.get_messages(templates)
            if field in received_fields: received_fields.remove(field)

        if check_unknown and len(received_fields):
            for f in received_fields:
                self._error_messages["_unknown_"].append("Unknown field {}".format(f))
                self._errors.append("Unknown field {}".format(f))

        return self

    def failed(self) -> bool:
        return len(self._errors) > 0

    def get_messages(self) -> dict:
        return self._error_messages
```
This class has 3 methods:

- `validate`, custom validation logic (more info below)
- `failed`, just to check if we have errors after validation
- `get_messages`, get messages which were collected after validation

The main method as you can see is `validate`, it has several arguments:

- `request` - input data. In examples with flask integration it will be json converted to dict
- `rules` - it is a dict where keys of this dict should match with keys of `request`
- `check_unknown` - when True, `validate` checks if count of keys in `request` different and more than keys in `rules`. 
In case of truth, it will add additional parameter to error messages `_unknown_`.
  
- templates - you can find more information [here](../../feature-guide/#custom-messages)

## Let's pass the input through "grinder"

I think example can clarify many things. First we need an input data - the data which should be validated:

```python
user_data = {
    "username": "",
    "email": "",
    "personal_id": "",
    "password": "",
}
```

Next we have to define rules for expected input:

```python
from respect_validation import Validator as v

rules = {
    "username": v.stringType().alnum().noWhitespace().length(4, 64),
    "email": v.optional(v.email()),
    "password": v.stringType().length(8, 64)
}
```
If you need any explanation for any of rules above, please try to find it [here](../../list-of-rules/).

Let's put our data to Validator:

```python
from Validator import Validator

validator = Validator()

validation = validator.validate(user_data, rules, check_unknown=True)

print(validation.get_messages())
```

We got this output:
```json
{
  "_unknown_": [
    "Unknown field personal_id"
  ],
  "username": {
    "alnum": [
      "Username must contain only letters (a-z) and digits (0-9)"
    ],
    "length": [
      "Username must have a length between 4 and 64"
    ]
  },
  "email": null,
  "password": {
    "length": [
      "Password must have a length between 8 and 64"
    ]
  }
}
```

The output above can clearly describe to user which field is incorrect and in our case also show extra field which 
unexpectedly appeared.

Now we can go to integration with [simple flask app](./2_simple_flask.md).