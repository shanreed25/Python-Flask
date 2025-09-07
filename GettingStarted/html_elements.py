from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # This just adds the text into an HTML body tag <body>Hello, World!</body>
    # return "Hello, World!"

    # This adds the text as a h1 tag into an HTML body tag
    # <body><h1 style="text-align: center >Hello, World!</h1></body>
    #return '<h1 style="text-align: center" >Hello, World!</h1>'

    return ('<h1 style="text-align: center" >Hello, World!</h1>'
            '<p>This is a Flask application</p>'
            '<img src="https://gallery.yopriceville.com/var/albums/Free-Clipart-Pictures/Butterflies-PNG/Purple_Butterfly_PNG_Clipart.png?m=1629783361" style="height: 200" />'
            '<br>'
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWNoeHJlZjY3ODdvM2IxdXFsYndqZXZtaXV6cmVwcXQ0bnFlNnAwbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AanHDMdjhFSBrOmzYF/giphy.gif"'
            ' style="height: 200" />'
            )

#OR**************************************************************

    return '<h1 style="text-align: center" >Hello, World!</h1>'\
            '<p>This is a Flask application</p>'\
            '<img src="https://gallery.yopriceville.com/var/albums/Free-Clipart-Pictures/Butterflies-PNG/Purple_Butterfly_PNG_Clipart.png?m=1629783361" style="height: 200" />'\
            '<br>'\
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWNoeHJlZjY3ODdvM2IxdXFsYndqZXZtaXV6cmVwcXQ0bnFlNnAwbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AanHDMdjhFSBrOmzYF/giphy.gif"'\
            ' style="height: 200" />'
            

if __name__ == "__main__":
    app.run(debug=True)