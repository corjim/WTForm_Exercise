from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def connect_db(app):
    with app.app_context():
        db.app = app 
        db.init_app(app)

default_pet_url = "https://thecontemporarypet.com/wp-content/themes/contemporarypet/images/default.png"

#   MODEL BELOW


class Pet(db.Model):
    """ Pets for adoption"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text,nullable=True, default= 'default_pet_url')

    age = db.Column(db.Integer, nullable=True)

    notes = db.Column(db.Text, nullable=True)

    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return image for pet"""

        return self.photo_url or default_pet_url
    

