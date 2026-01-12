from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__)
STATS_FILE = "stats.txt"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_cat_name')
def get_name():
    names = ["Professor Paws", "Lord Fluffington", "Sir Purr-a-lot", "Captain Meow", "General Whiskers"]
    return jsonify(name=random.choice(names))

@app.route('/initial_pet')
def initial_pet():
    # 1. Read the current count from the file
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            try:
                count = int(f.read())
            except ValueError:
                count = 0
    else:
        count = 0

    return jsonify(total_pets=count)


@app.route('/pet_cat')
def pet_cat():

    # 1. Read the current count from the file
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            try:
                count = int(f.read())
            except ValueError:
                count = 0
    else:
        count = 0
    
    # Increase it
    count += 1
    
    # Save it back
    with open("stats.txt", "w") as f:
        f.write(str(count))
        
    return jsonify(total_pets=count)


if __name__ == '__main__':
    app.run(debug=True)
