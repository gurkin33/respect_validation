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
