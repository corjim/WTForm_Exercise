from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, Length


class AddPetForm(FlaskForm):
    """Adds pets"""

    name = StringField("Pet Name",validators=[InputRequired(message='Please type pets name')])

    species = SelectField('Species',  choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', "Porcupine")], validators=[InputRequired()])

    photo_url = StringField('Photo Url', validators=[Optional()])

    age = IntegerField("Age",  validators=[Optional(), NumberRange(min=0, max=15)])

    notes = TextAreaField("Notes",validators=[Optional(), Length(min=10)])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")