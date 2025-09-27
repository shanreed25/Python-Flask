from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template("index.html")
#
# @app.route("/form-entry", methods=["POST"])
# def send_data():
#     message_info = request.form # returns ImmutableMultiDict
#     print(message_info)
#     # Iterate through items and print values as strings
#     # for key, values imessage_info.lists():
#     #     for value in values:
#     #         print(f"{str(value)}")
#     name = message_info['name']
#     email = message_info['email']
#     phone_number = message_info['phone']
#     message = message_info['message']
#     print(name)
#     print(email)
#     print(phone_number)
#     print(message)
#     return "<h1>💪 Success! Form submitted</h1>"
#************************************************************************************************************
# Combine the / route with /form-entry so that they are both under the route "/"
# but depending on which method (GET/POST) that triggered the route, handle it appropriately
    # modify both the action in the index.html and your server.py
#
# @app.route('/', methods=["GET", "POST"])
# def contact():
#     # used request.method to check which method triggered the route
#     if request.method == "POST":
#         data = request.form
#         print(data["name"])
#         print(data["email"])
#         print(data["phone"])
#         print(data["message"])
#     #     return "<h1>💪 Success! Form submitted</h1>"
#     # return render_template("index.html")
#
#     #     Instead of returning a < h1 > that says "Successfully sent message",
#     #     update the index.html file so that the < h1 > on the index.html
#     #     file becomes "Successfully sent message".
#         return render_template("index.html", msg_sent=True)
#     return render_template("index.html", msg_sent=False)

#************************************************************************************************************

# make the contact form complete and actually send us (website owner) an email when a user is trying to get in touch
OWN_EMAIL = "tralainereed@gmail.com"
OWN_PASSWORD = "rtlgdseitbxdymhy"
PORT= 587

@app.route('/', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=PORT) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True, port=5001)