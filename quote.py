import json
from flask import Flask, jsonify

app = Flask(__name__)

with open("time-quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)


@app.route("/quotes.json", methods=['GET', 'POST'])
# returns contents of json file as a GET request
def get_quote():
    return jsonify(quotes)


if __name__ == "__main__":
    app.run()
