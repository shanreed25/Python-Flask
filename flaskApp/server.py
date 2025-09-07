from flask import Flask, render_template, request
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year

    # **context(**kwargs): represents the variables to make available in the template
    # each variable must have a name and value, the name will be used in the HTML file
    return render_template("index.html", num=random_number, year=year)

@app.route("/guess/<name>")
def get_name(name):
    age_res = requests.get(url=f'https://api.agify.io?name={name}')
    gender_res = requests.get(url=f'https://api.genderize.io?name={name}')
    age = age_res.json()["age"]
    print(age_res.json())
    gender = gender_res.json()["gender"]
    print(gender_res.json())
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog")
def get_blogs():
    res = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    posts = res.json()
    print(res.json())
    return render_template("blog.html", posts=posts)


@app.route("/post/<int:index>")#index parameter come from blog.html
def get_post(index):
    print(index)
    res = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    posts = res.json()
    post_choice = None
    for post in posts:
        if post["id"] == index:
            post_choice = post
    print(post_choice)
    return render_template("post.html", post=post_choice)

###POST WITHHTML FORM***********************************************************************************************************

@app.route("/form")
def hello_form():
    return render_template("form.html")

@app.route("/sendform", methods=["POST"])
def receive_data():
    user = request.form['user_name']
    print(request.form['user_name'])
    return f"<h1>{user}</h1> "
    # return "💪 Success! Form submitted"

if __name__ == "__main__":
    app.run(debug=True)