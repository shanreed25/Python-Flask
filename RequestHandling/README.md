# Python: Flask Request Handling
**Flask request handling is the core mechanism that processes incoming HTTP requests and generates appropriate responses. Let me break this down comprehensively.**

### 🔄 Request-Response Cycle

1. Request Flow
- Client Browser ➡️ HTTP Request ➡️ Flask Server ➡️ Route Matching ➡️ Function Execution ➡️ Response Generation ➡️ Client Browse
2. Flask's Internal Flow
- Client visits: http://........
- Flask receives HTTP request ➡️ Flask creates request context ➡️ URL routing system activates ➡️ Route matching occurs View function executes ➡️ Response is generated and sent

### 📍 Route Matching and URL Patterns
- **Static Routes** : matches exactly
    - `@app.route("/")` : matches exactly `"/"`
    - `@app.route("/about")` : matches exactly `"/about"`

- **Dynamic Routes (Variable Rules)**
    - `@app.route("/user/<username>")` : `<username>` captures any string, string is the default data type
    - `@app.route("/post/<int:post_id>")` : `<int:post_id>` captures integers only
    - `@app.route("/files/<path:filename>")` : `<path:filename>` captures paths with slashes

- **HTTP Methods**
    - `@app.route("/data", methods=['GET'])` : only GET requests
    - `@app.route("/submit", methods=['POST'])` : only POST requests  
    - `@app.route("/api", methods=['GET', 'POST'])` : both GET and POST
    - `@app.route("/resource", methods=['GET', 'POST', 'PUT', 'DELETE'])`  # RESTful

#### 📦 The Request Object
- Flask creates request context that contains information about the current HTTP request
    - GET, POST, PUT, DELETE methods
    - URL parameters and query strings
    - Form data and file uploads
    - Session management
- Learn more about the request object [here](./RequestObject.md)

_____________________________________________________

- [Content and JSON Handling](./ContentandJSONHandling.md)
- [File Uploads](./FileUploads.md)
- [Form Handling](./FormHandling.md)
- [Headers, Cookies and Client](./HeadersCookiesClient.md)
- [HTTP Methods](./HTTPMethods.md)
- [Query Parameters](./OueryParameters.md)
- [Request Object](./RequestObject.md)
- [URL and Routing](./URLandRouting.md)
- []()
- []()
- []()
- []()