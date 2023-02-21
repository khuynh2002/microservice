import random
import json
from flask import Flask, jsonify

app = Flask(__name__)

with open("time-quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)


@app.route("/quotes.json", methods=['GET', 'POST'])
# returns contents of json file as a GET request
def get_quote():
    return jsonify(quotes)


@app.route("/random.json", methods=['GET', 'POST'])
def get_random_quote():
    if not quotes:
        return "Error. No quotes.", 404
    random_index = random.randint(0, len(quotes["quotes"]) - 1)
    random_quote = quotes["quotes"][random_index]
    return jsonify(random_quote) 


if __name__ == "__main__":
    app.run()
