from flask import Flask, request
from flask_migrate import Migrate


if __name__ == '__main__':
    from db import db
    from user_model import UserModel
else:
    from examples.db import db
    from examples.user_model import UserModel

app = Flask(__name__)
migrate = Migrate(app, db)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/user", methods=['POST'])
def validation_test():
    r = request.json
    output = {"error": False, "validation": None, "data": None}

    if UserModel.find_by_name(r.get('username', None)):
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
else:
    #  to init db run this commands:
    #    export FLASK_APP=flask_sqlalchemy_app.py; flask db init; flask db migrate; flask db upgrade;
    db.init_app(app)
