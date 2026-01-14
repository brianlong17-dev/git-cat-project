from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import os

app = Flask(__name__)
# Tell Flask to use the Database URL from Render, or a local one if testing
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create a "Table" for our Pet Count
class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_pets = db.Column(db.Integer, default=0)

# Create the database table if it doesn't exist
with app.app_context():
    db.create_all()
    # Initialize the row if it's empty
    if not Stats.query.first():
        db.session.add(Stats(total_pets=0))
        db.session.commit()

@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/initial_pet')
def initial_pet():
    stats = Stats.query.first()
    return jsonify(total_pets=stats.total_pets)


@app.route('/pet_cat')
def pet_cat():
    names = ["Professor Pawsy", "Lord Fluffingtony", "Sir Purr-a-lot", "Captain Meow", "General Whiskers"]
    stats = Stats.query.first()
    stats.total_pets += 1
    db.session.commit()
    return jsonify(total_pets=stats.total_pets, name=random.choice(names))


if __name__ == '__main__':
    app.run(debug=True)
