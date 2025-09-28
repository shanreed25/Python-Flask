# **🔍 Request Object: Query Parameters and Form Data**
**The Flask request object provides access to two main types of user input data: query parameters (from URLs) and form data (from HTML forms).**
- Query parameters and form data are the primary ways users interact with your Flask application
- Understanding how to safely access, validate, and process this data is crucial for building robust web applications


- `request.method` : is the HTTP method (GET, POST, etc.)
- `request.request.args` : query parameters access
- `request.form` :
- `request.` :
- `request.` :
- `request.` :
- `request.` :



## 🔗 Query Parameters (request.args)
**Query parameters are data passed in the URL after the ? symbol, using key-value pairs.**

##### Basic Access
- access query parameters using `request.request.args`, the value is always a string
    - `?q=python&category=tutorial&page=2&active=true`
    - `query = request.args.get('q', 'html')` : 'python', 'html' is the defaulf value
    - `category = request.args.get('category', '' )` : 'tutorial', empty string is default
    - `page = request.args.get('page')` : '2', value is always returned as a string

##### Type Conversion
- query parameters are always strings, convert as needed
- `page = request.args.get('page', 1, type=int)`, to int
- `price_min = request.args.get('min_price', 0.0, type=float)`, to float
- `active = request.args.get('active', False, type=bool)`, to boolean
- ***Manual conversion with error handling**
```python
try:
        limit = int(request.args.get('limit', '10'))
    except ValueError:
        limit = 10  # Fallback if invalid
```

##### Multiple Values for Same Parameter
- `/filter?tags=python&tags=web&tags=tutorial`
    - `first_tag = request.args.get('tags')` : get first occurrence, **`python`**
    - `all_tags = request.args.getlist('tags')` : get all occurrences, **`['python', 'web', 'tutorial']`**
- get all query parameters as a dictionary
    - `all_params = request.args.to_dict()` : gets only first value **`{'tags': 'python'}`**
    - `all_params_multi = request.args.to_dict(flat=False)` **`{'tags': ['python', 'web', 'tutorial']}`**
- check if parameter exists : `has_tags = 'tags' in request.args` : **`True`**


__________________________________________
- [Form Handling](./FormHandling.md)
- [File Uploads](./FileUploads.md)


