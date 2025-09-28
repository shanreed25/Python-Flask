### **📦 The Request Object**
**Request is a global object in Flask that contains information about the current HTTP request**
- the `request` object is imported from Flask
    - `from flask import Flask, request`
    - `from flask import request`
- the `request` object is used to access request-specific information 
#### **Request Context Creation**
- Flask automatically creates a request object for each incoming request
    1. Parsed the incoming HTTP request
    2. Created the request object
    3. Populated it with all request data
    4. Made it available as a global variable
**All of this happens BEFORE your view function is called**

```python
@app.route("/about")
def get_about():
    print(f"Request object ready: {request}")
```


#### **Request Data Categories**

[🔗 URL and Routing Information](./URLandRouting.md)

[🔍 Query Parameters and Form Data](./OueryParameters.md)

[🍪 Headers, Cookies, and Client Information](./HeadersCookiesClient.md)

[📄 Content and JSON Handling](./ContentandJSONHandling.md)








