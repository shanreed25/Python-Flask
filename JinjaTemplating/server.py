from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", active_page="home")

@app.route("/include-directive")
def include():
    return render_template("./include.html", active_page="include")


@app.route("/inheritance")
def inheritance():
    return render_template("./inheritance.html", active_page="inheritance")


# Route for practice code
@app.route("/try")
def try_code():
    return render_template("./try/try.html")

if __name__ == "__main__":
    app.run(debug=True)