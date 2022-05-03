# Flask + SqlAlchemy

This example is here because I want to show you how you can use validation 
in Model section.

## Create Model with validation

First we will create our UserModel with validation inside:

```python
class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True, default='')
    first_name = db.Column(db.String(255), nullable=True, default='')
    second_name = db.Column(db.String(255), nullable=True, default='')

    @classmethod
    def find_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, _id: int):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def get(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'second_name': self.second_name
        }

    @classmethod
    def validate(cls, request):
        validator = Validator()
        return validator.validate(request, {
            "username": v.stringType().alnum().noWhitespace().length(4, 64),
            "email": v.optional(v.email()),
            "first_name": v.optional(v.stringType().length(3, 64)).set_name('First name'),
            "second_name": v.optional(v.stringType().length(3, 64)).set_name('Second name'),
            "password": v.stringType().length(8, 64),
            "password_confirmation": v.stringType().equals(request.get('password', None)).set_template(
                'Password confirmation'),
        }, templates={'equals': "Password confirmation does match with Password"}, check_unknown=True)
```

With validation inside of Model you can easily validate incoming 
request to create or update your object. In example above I 
described validation for object creation, but you can 
play with it and add more validation if required (for example, for 
object update case).

## Flask preparation
Finally, we will review our new simple flask app:
```python
from flask import Flask, request
from flask_migrate import Migrate

from db import db
from user_model import UserModel

app = Flask(__name__)
migrate = Migrate(app, db)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/user", methods=['POST'])
def validation_test():
    r = request.json
    output = {"error": False, "validation": None, "data": None}
    
    #  check if username already in DB
    if UserModel.find_by_name(r.get('username', None)):
        output["error"] = True
        return output

    validation = UserModel.validate(r)

    if validation.failed():
        output["error"] = True
        output["validation"] = validation.get_messages()
        return output

    del r['password_confirmation']

    new_user = UserModel(**r)
    new_user.save_to_db()
    output["data"] = {"id": new_user.id}

    return output


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5959, host='127.0.0.1', debug=True)
```

You can see the first check is if username is in DataBase or not. 
Of course, you can add your own custom rule to respect_validation to 
make this check in background, but it is out of scope for this guide.

## Example request/response

Here is input request:
```json
{
    "username": "Alexey",
    "first_name": "A",
    "second_name": "Mochalin",
    "email": "Mochalin",
    "password": "123123",
    "password_confirmation": "123132"
}
```

And response of flask:
```json
{
    "data": null,
    "error": true,
    "validation": {
        "_unknown_": [],
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
        "first_name": {
            "allOf": [
                "All of the required rules must pass for First name",
                {
                    "length": [
                        "First name must have a length between 3 and 64"
                    ]
                }
            ]
        },
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
        "username": null
    }
}
```

Hope it will be useful for you. You can find this code
in example directory of main repository.