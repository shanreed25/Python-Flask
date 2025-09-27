import random
from flask import Flask

app = Flask(__name__)

ran_number = random.randint(0, 9)
print(ran_number)
@app.route("/")
def guess():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"'
            ' style="height: 200" />'
            )
@app.route("/<int:num>")
def evaluate_guessed_number(num):
    if num > 9:
        return (f'<h1>{num} is not a number between 0 and 9</h1>'
                '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWNhMjJ6MzN0ZThkMm1oM2p4bWpuZ2FlcmN1d2h4a3E5aWZ3YmxzdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wofftnAdDtx4s/giphy.gif"/>'
                )
    elif ran_number > num:
        return (f'<h1>{num} is Too Low</h1>'
                '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWNhMjJ6MzN0ZThkMm1oM2p4bWpuZ2FlcmN1d2h4a3E5aWZ3YmxzdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wofftnAdDtx4s/giphy.gif"/>'
                )
    elif ran_number < num:
        return (f'<h1>{num} is Too High</h1>'
                '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWNhMjJ6MzN0ZThkMm1oM2p4bWpuZ2FlcmN1d2h4a3E5aWZ3YmxzdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wofftnAdDtx4s/giphy.gif"/>'
                )
    else:
        return (f'<h1>{num} is Right</h1>'
                '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmR6aXpxenY3aWpmcnlmd3h1bXZ5bzBqZXYwbGlob2dkb2pjcnJnZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7abKhOpu0NwenH3O/giphy.gif"/>'
                )


if __name__ == '__main__':
    app.run(debug=True)