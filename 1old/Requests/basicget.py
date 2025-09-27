from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")# this function only triggers if the user is accessing the('/') route
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/recipes")# this function only triggers if the user is accessing the('/recipes') route
def get_recipes():
    response = requests.get(url="https://dummyjson.com/recipes")  # get data from endpoint
    response.raise_for_status()
    data = response.json()
    print(data)
    return "<p>RECIPES!!!!</p>"


if __name__ == "__main__":
    app.run(debug=True)