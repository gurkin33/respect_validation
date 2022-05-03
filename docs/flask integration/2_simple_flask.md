# Simple Flask APP

First read previous [page](./1_custom_validator.md) because here we will use new class Validator.

## Prepare Flask APP

Let's start with example of simple Flask APP and integrated validator:

```python
from flask import Flask, request
from respect_validation import Validator as v
from Validator import Validator


app = Flask(__name__)
validator = Validator()


@app.route("/test", methods=['POST'])
def validation_test():
    r = request.json

    output = {"error": False, "validation": None, "data": None}

    validation = validator.validate(r, {
        "username": v.stringType().alnum().noWhitespace().length(4, 64),
        "email": v.optional(v.email()),
        "first_name": v.optional(v.stringType().length(3, 64)).set_name('First name'),
        "second_name": v.optional(v.stringType().length(3, 64)).set_name('Second name'),
        "password": v.stringType().length(8, 64),
        "password_confirmation": v.stringType().equals(r.get('password', None)).set_template('Password confirmation'),
    }, templates={'equals': "Password confirmation does match with Password"}, check_unknown=True)

    if validation.failed():
        output['error'] = True
        output['validation'] = validation.get_messages()
        return output

    output["data"] = "User data is correct :)"

    return output


if __name__ == '__main__':
    app.run(port=5959, host='0.0.0.0', debug=True)
```

We imported `respect_validation.Validator` to write our validation rules and new class Validator to run validation.

## Example request/response

For example, we send this request:
```json
{
    "username": "A",
    "email": "B",
    "first_name": "Alexey",
    "second_name": "",
    "personal_id": "",
    "password": "123",
    "password_confirmation": "321"
}
```

Flask will responses us with this JSON:
```json
{
    "data": null,
    "error": true,
    "validation": {
        "_unknown_": [
            "Unknown field personal_id"
        ],
        "email": {
            "allOf": [
                "All of the required rules must pass for Email",
                {
                    "email": [
                        "Email must be valid email"
                    ]
                }
            ]
        },
        "first_name": null,
        "password": {
            "length": [
                "Password must have a length between 8 and 64"
            ]
        },
        "password_confirmation": {
            "equals": [
                "Password confirmation does match with Password"
            ]
        },
        "second_name": null,
        "username": {
            "length": [
                "Username must have a length between 4 and 64"
            ]
        }
    }
}
```

With some skill of JavaScript this output can turn into clear error messages for a user in web interface, 
but it is beyond of this guide :)

Hope you will find this useful. If you want another example of using flask, sqlalchemy and respect_validation, please 
follow next page.