# 🪄 How Flask Works


## 🧬 Application Structure
1. Create Flask application
2. Define URL routes
3. Run development server
```
from flask import Flask, render_template

app = Flask(__name__)  # Create Flask application

@app.route('/')        # Define URL routes
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  # Run development server
```

## 🔃 Request-Response Cycle
1. Client sends HTTP request to Flask server
2. Flask matches URL to a route function
3. Function processes request and returns response
4. Flask sends response back to client

## 📁 Flask Project Structure
```
project/
├── server.py              # Main application file
├── templates/             # HTML templates
│   ├── index.html
│   └── dashboard/
├── static/               # CSS, JS, images
│   ├── css/
│   ├── js/
│   └── images/
└── requirements.txt      # Dependencies
```