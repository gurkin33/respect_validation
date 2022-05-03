if __name__ == 'user_model':
    from db import db
    from Validator import Validator
    from respect_validation import Validator as v
else:
    from examples.db import db


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