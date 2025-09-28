# 📝 Request Object: Form Handling (request.method, request.form)

- [Query parameters](./OueryParameters.md) and form data are the primary ways users interact with your Flask application
- Understanding how to safely access, validate, and process this data is crucial for building robust web applications
**Form data comes from HTML forms submitted via POST (or other HTTP methods).**
- `<form method="POST" action="/submit">`
    - `@app.route("/submit", methods=['GET', 'POST'])` ???
    - `if request.method == 'GET'`: check the request method
- `<input type="text" name="username" required>`
    - `username = request.form.get('username')` returns string or None
    - `username = request.form.get('username', "")` returns string or empty string(default value)
- `<select name="country">`
    - `country = request.form.get('country', "US")` returns selected option value or "US"(default value)
         # 
- `<input type="checkbox" name="newsletter" value="yes">`
    - `newsletter = request.form.get('newsletter')` returns 'yes' or None
    - `subscribe = request.form.get('newsletter') == 'yes'` : check if the checkbox is checked

### Multiple Form Values
- Multiple checkboxes with same name 
```html
<form method="POST" action="/preferences">
    <input type="checkbox" name="interests" value="web"> Web Development
    <input type="checkbox" name="interests" value="mobile"> Mobile Apps  
    <input type="checkbox" name="interests" value="ai"> AI/ML
    <input type="checkbox" name="interests" value="data"> Data Science
    <button type="submit">Save</button>
</form>
```
- `first_interest = request.form.get('interests')` : first occurrence ***`'web'`***  (if checked)
- `all_interests = request.form.getlist('interests')` : all checked boxes **`['web', 'ai', 'data']`**

# 🔍 Advanced Form Processing
- Form Validation
```python
@app.route("/register", methods=['POST'])
def register():
    # Get form data
    username = request.form.get('username', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')
    
    # Validation
    errors = []
    
    if not username or len(username) < 3:
        errors.append("Username must be at least 3 characters")
    
    if not email or '@' not in email:
        errors.append("Valid email required")
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
    
    if password != confirm_password:
        errors.append("Passwords don't match")
    
    # Return errors or success
    if errors:
        return {'errors': errors}, 400
    
    # Process registration
    return {'message': 'Registration successful'}
```

- Form Data Inspection
```python
@app.route("/debug-form", methods=['POST'])
def debug_form():
    # All form data
    all_form_data = request.form.to_dict()
    all_form_data_multi = request.form.to_dict(flat=False)
    
    # Check what's in the form
    form_keys = list(request.form.keys())
    
    # Iterate through all form fields
    form_details = {}
    for key in request.form.keys():
        values = request.form.getlist(key)
        form_details[key] = {
            'single_value': request.form.get(key),
            'all_values': values,
            'count': len(values)
        }
    
    return {
        'form_data': all_form_data,
        'form_data_multi': all_form_data_multi,
        'form_keys': form_keys,
        'form_details': form_details
    }
```

- Search with Filters
```python
@app.route("/products", methods=['GET', 'POST'])
def products():
    # GET: Query parameters from URL
    # POST: Form data from filter form
    
    if request.method == 'GET':
        # URL: /products?category=electronics&min_price=100&max_price=500
        category = request.args.get('category', 'all')
        min_price = request.args.get('min_price', 0, type=float)
        max_price = request.args.get('max_price', 1000, type=float)
        search_query = request.args.get('q', '')
        
    elif request.method == 'POST':
        # Form submission with filters
        category = request.form.get('category', 'all')
        min_price = float(request.form.get('min_price', 0))
        max_price = float(request.form.get('max_price', 1000))
        search_query = request.form.get('search', '')
        
        # Multiple selections
        brands = request.form.getlist('brands')
        features = request.form.getlist('features')
    
    # Use the same logic for both GET and POST
    filters = {
        'category': category,
        'min_price': min_price,
        'max_price': max_price,
        'query': search_query
    }
    
    if request.method == 'POST':
        filters.update({
            'brands': brands,
            'features': features
        })
    
    return render_template('products.html', filters=filters)
```

### ⚠️ Important Notes
1. Data Types
    - **Query parameters:** Always strings (use type=int to convert)
    - **Form data:** Always strings (convert manually)
    - **Files:** Special FileStorage objects

2. Security Considerations
```python
# Always validate and sanitize input
username = request.form.get('username', '').strip()
if not username.isalnum():
    return "Invalid username", 400

# Use secure_filename for file uploads
from werkzeug.utils import secure_filename
filename = secure_filename(file.filename)
```

3. Memory Usage
```python
# For large file uploads, consider streaming
@app.route("/large-upload", methods=['POST'])
def large_upload():
    file = request.files['large_file']
    
    # Stream large files instead of loading into memory
    file.save('/path/to/destination')  # Streams automatically
```

4. Content Type Handling
```python
@app.route("/api", methods=['POST'])
def api_endpoint():
    if request.content_type == 'application/json':
        data = request.get_json()
    elif request.content_type == 'application/x-www-form-urlencoded':
        data = request.form.to_dict()
    elif request.content_type.startswith('multipart/form-data'):
        data = request.form.to_dict()
        files = request.files.to_dict()
    else:
        return "Unsupported content type", 415
```

________________________________________________
```python
@app.route("/search", methods=['GET', 'POST'])
def search():
    # Query Parameters (URL: /search?q=python&type=tutorial&page=2)
    query = request.args.get('q')                    # 'python'
    search_type = request.args.get('type')           # 'tutorial' 
    page = request.args.get('page', 1, type=int)     # 2 (converted to integer)
    
    # Multiple values for same parameter (?tags=web&tags=python)
    tags = request.args.getlist('tags')              # ['web', 'python']
    
    # All query parameters
    print(f"All query args: {request.args}")
    
    # Form Data (POST requests)
    if request.method == 'POST':
        # Single form fields
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Multiple selections (checkboxes)
        interests = request.form.getlist('interests')
        
        # All form data
        print(f"Form data: {request.form}")
        
        # File uploads
        if 'avatar' in request.files:
            file = request.files['avatar']
            if file and file.filename != '':
                # Save uploaded file
                file.save(f'uploads/{file.filename}')
```