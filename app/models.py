# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Usuario(UserMixin, db.Model):
    """
    Create an Usuario table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    # acho que postagens e grupos ficam em outra tabela
    grupos = db.relationship('Grupo', backref='usuario',
                                lazy='dynamic')
    postagens = db.relationship('Postagem', backref='usuario',
                                lazy='dynamic')
    #department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    #role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Usuario: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Grupo(db.Model):
    """
    Create a Grupo table
    """

    __tablename__ = 'grupos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    usuarios = db.relationship('Usuario', backref='grupo',
                                lazy='dynamic')

    def __repr__(self):
        return '<Grupo: {}>'.format(self.name)

class Postagem(db.Model):
    """
    Create a Postagem table
    """

    __tablename__ = 'postagens'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    usuarios_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    def __repr__(self):
        return '<Postagem: {}>'.format(self.name)