from flask_login import UserMixin
from app import db, login, log
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(120), index = True, unique = True)

    def __repr__(self):
        return '<User %r>' % self.email    
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
        
    def get_id(self):
        return unicode(self.id)
    


    def check_password(self, supplied_pw):
        log.warning(supplied_pw)
        return check_password_hash(self.password, supplied_pw)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

