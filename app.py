from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database_setup import db, Flavor, Ingredient, Suggestion, Allergy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chocolate_house.db'
db.init_app(app)

with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# owner route
@app.route('/owner')
def owner_home():
    # Get all flavors and ingredients from the database
    flavors = Flavor.query.all()
    ingredients = Ingredient.query.all()
    return render_template('owner_home.html', flavors=flavors, ingredients=ingredients)


# customer route
@app.route('/customer')
def customer_home():
    return render_template('customer_home.html')

# Route to add a flavor
@app.route('/add_flavor', methods=['GET', 'POST'])
def add_flavor():
    if request.method == 'POST':
        flavor_name = request.form['name']
        seasonal = request.form.get('seasonal') == 'on'  # Checkbox for seasonal
        new_flavor = Flavor(name=flavor_name, seasonal=seasonal)
        db.session.add(new_flavor)
        db.session.commit()
        return redirect(url_for('owner_home'))
    return render_template('add_flavor.html')

# Route to delete a flavor
@app.route('/delete_flavor/<int:flavor_id>')
def delete_flavor(flavor_id):
    flavor = Flavor.query.get(flavor_id)
    if flavor:
        db.session.delete(flavor)
        db.session.commit()
    return redirect(url_for('owner_home'))

# Route to add an ingredient
@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'POST':
        ingredient_name = request.form['name']
        quantity = int(request.form['quantity'])
        new_ingredient = Ingredient(name=ingredient_name, quantity=quantity)
        db.session.add(new_ingredient)
        db.session.commit()
        return redirect(url_for('owner_home'))
    return render_template('add_ingredient.html')

# Route to delete an ingredient
@app.route('/delete_ingredient/<int:ingredient_id>')
def delete_ingredient(ingredient_id):
    ingredient = Ingredient.query.get(ingredient_id)
    if ingredient:
        db.session.delete(ingredient)
        db.session.commit()
    return redirect(url_for('owner_home'))

# Route to handle suggestions
@app.route('/add_suggestion', methods=['GET', 'POST'])
def add_suggestion():
    if request.method == 'POST':
        flavor_name = request.form['flavor_name']
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        new_suggestion = Suggestion(flavor_name=flavor_name, customer_name=customer_name, customer_email=customer_email)
        db.session.add(new_suggestion)
        db.session.commit()
        return redirect(url_for('customer_home'))
    return render_template('add_suggestion.html')

# Route to view all suggestions
@app.route('/suggestions')
def view_suggestions():
    suggestions = Suggestion.query.all()
    return render_template('suggestions.html', suggestions=suggestions)

# Route to handle allergies
@app.route('/add_allergy', methods=['GET', 'POST'])
def add_allergy():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        allergy_ingredient = request.form['allergy_ingredient']
        new_allergy = Allergy(customer_name=customer_name, customer_email=customer_email, allergy_ingredient=allergy_ingredient)
        db.session.add(new_allergy)
        db.session.commit()
        return redirect(url_for('customer_home'))
    return render_template('add_allergy.html')

# Route to view all allergies
@app.route('/allergies')
def view_allergies():
    allergies = Allergy.query.all()
    return render_template('allergies.html', allergies=allergies)

if __name__ == '__main__':
    app.run(debug=True)
