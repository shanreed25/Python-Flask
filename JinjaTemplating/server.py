from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/include-method")
def include():
    return render_template("./include.html")


@app.route("/try")
def try_code():
    return render_template("./try/parent.html")

if __name__ == "__main__":
    app.run(debug=True)