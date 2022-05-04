# Simple Flask APP

First read previous [page](./1_form_validator.md) because here we will use FormValidator described on 
the previous page.

## Prepare Flask APP

Let's start with example of simple Flask APP and integrated validator:

```python
from flask import Flask, request
from respect_validation import Validator as v, FormValidator as fv

app = Flask(__name__)


@app.route("/user", methods=['POST'])
def validation_test():
    r = request.json

    output = {"error": False, "validation": None, "data": None}
    validator = fv()
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

## Examples request/response

### Successful validation
```json
{
    "username": "gurkin33",
    "email": "",
    "first_name": "Alexey",
    "second_name": "",
    "password": "123123123",
    "password_confirmation": "123123123"
}
```
Flask will responses us with this JSON:
```json
{
    "data": "User data is correct :)",
    "error": false,
    "validation": null
}
```
---
### Failed validation

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

With some skill of JavaScript this output can turn into clear error messages for a user in web interface.
If you have example of validation parser please share with us, else I will add my example later. :)

Hope you will find this useful. Also, if you use 
[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/), you can integrate validator 
into your [Models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/).