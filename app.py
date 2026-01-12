from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_cat_name')
def get_name():
    names = ["Professor Paws", "Lord Fluffington", "Sir Purr-a-lot", "Captain Meow", "General Whiskers"]
    return jsonify(name=random.choice(names))

if __name__ == '__main__':
    app.run(debug=True)