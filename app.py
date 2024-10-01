from flask import Flask, request, render_template, redirect, session, flash, url_for, jsonify
from models import db, connect_db, Pet
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'

app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

connect_db(app) 

app.config['SECRET_KEY'] = "@dfjighi&forxll#i"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.drop_all()
db.create_all()

#   Create Pets

# dog1 = Pet(name='Jimmy', species="dog", age="2", notes="Very friendly with cute bark")
# dog2 = Pet(name='Bingo', species="dog", age="4", notes="fluffy with cute bark")
# dog3 = Pet(name='Doggy', species="dog", age="8", notes="Like cuddling and shy")

# db.session.add(dog1)
# db.session.add(dog2)
# db.session.add(dog3)

# db.session.commit()


@app.route('/')
def homepage():
    """Shows all the pet in adoption"""

    pets = Pet.query.all()

    return render_template('homepage.html', pets=pets)


@app.route('/add_pet', methods=['GET','POST'])
def add_pet():
    """Handles form submission and adds pet to the list"""

    form = AddPetForm()

    if form.validate_on_submit():

        name = form.name.data
        age = form.age.data
        species = form.species.data
        photo_url = form.photo_url.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, age=age, photo_url=photo_url, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f'{new_pet.name} is added')

        return redirect('/')
    else:
        return render_template('add_pet.html',form=form)
    

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Edit Pet"""

    
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")

        return redirect('/')

    else:
        return render_template('pet_edit_form.html', form=form, pet=pet)


@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5505, debug=True)

