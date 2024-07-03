from flask import Flask, render_template, request
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call cheese that isn't yours? Nacho cheese."
]

punchlines = [
    "I bet {name} would find this hilarious!",
    "{name}, you should tell this one at your next meeting!",
    "Even {name} couldn't come up with something this funny!",
    "Share this with {name}, they'll love it!",
    "{name}, this one's for you!"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_joke', methods=['POST'])
def get_joke():
    name = request.form['name']
    joke = random.choice(jokes)
    punchline = random.choice(punchlines).format(name=name)
    return f"{joke} {punchline}"

if __name__ == '__main__':
    app.run(debug=True)
