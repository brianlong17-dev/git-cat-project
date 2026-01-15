from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import random
import os

app = Flask(__name__)
# Tell Flask to use the Database URL from Render, or a local one if testing
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create a "Table" for our Pet Count
class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    emoji = db.Column(db.String(10), nullable=False)
    bg_color = db.Column(db.String(20), default="#ffffff") # Hex code for the background
    pet_count = db.Column(db.Integer, default=0)

# Create the database table if it doesn't exist
with app.app_context():
    db.create_all()
    # Initialize the row if it's empty
    if not Cat.query.first():
        starting_cats = [
            {"name": "My Boy", "emoji": "🦁", "color": "#F1C40F"},
            {"name": "Olly G", "emoji": "🐱", "color": "#9B59B6"},
            {"name": "Number One", "emoji": "🐯", "color": "#E67E22"},
            {"name": "Untrustworthy", "emoji": "🐈‍⬛", "color": "#2D73B9"}
        ]
        for cat_data in starting_cats:
            new_cat = Cat(
                name=cat_data["name"],
                emoji=cat_data["emoji"],
                bg_color=cat_data["color"]
            )
            db.session.add(new_cat)
        
        db.session.commit()
        print("Database seeded with the starter cats!")

@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/initial_pet')
def initial_pet():
    cat = Cat.query.order_by(func.random()).first()
    return jsonify(id=cat.id, pet_count=cat.pet_count, name=cat.name, emoji=cat.emoji, bg_color=cat.bg_color)





@app.route('/pet_cat/<int:cat_id>') # <int:cat_id> tells Flask to expect a number here
def pet_cat(cat_id):
    cat = Cat.query.get_or_404(cat_id) # Find the specific cat or return a 404 error
    cat.pet_count += 1
    db.session.commit()
    return jsonify(pet_count=cat.pet_count) 


if __name__ == '__main__':
    app.run(debug=True)
