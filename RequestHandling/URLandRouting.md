### **🔗 Request Object: URL and Routing Information**
- `request.url` : is the full URL with domain `http://127.0.0.1:5000/dashboard/python`
- `request.endpoint` : name of view function `dashboard_section`
- `request.url_rule` : route pattern `/dashboard/<language>/<section>`
    - url parameters captured from route pattern
    - url parameters usually passed to the view function as arguments
- `request.path` : url path `/dashboard/python/basics`

#### URL Parameters: can be accessed 2 ways
1. `current_lang = language`  use the function parameter to access value directly from url parameter(most common)
2. `request.view_args` : through a dictionary of URL parameters(redundant but safe)
- `{'language': 'python', 'section': 'basics'}`
- ✅ SAFE : Returns default if key doesn't exist
    - use `dict.get(key, default_value)`, to get the value for a key
    - `request.view_args.get('language', 'html')` : gets the language parameter value
        - if key exists returns the actual value: `python`
        - if key doesn't exist returns: `html`
- ❌ DANGEROUS, direct dictionary access: `request.view_args['language'] `
        - Will crash(Raises KeyError) if key doesn't exist
- ✅ SAFE but verbose
```python
try:
    current_language = request.view_args['language']
except KeyError:
    current_language = 'html'
```
##### Use Cases
- **Navigation States:** `request.view_args` can be used for active navigation states, in your Jinja2 template
    - `<a href="" class="{% if request.view_args.get('language') == 'python' %}active{% endif %}">Python</a>`
- **Type Conversion Integer:** `page = request.view_args.get('page', 1)  # Default to page 1`
    - Ensure it's an integer : `page = int(page) if page else 1`  

##### ✅ Best Practices: `request.view_args`
- Always use `.get()` instead of direct dictionary access
    - `dict.get(key, default)`: cornerstone of defensive programming in Python - it prevents crashes and provides predictable fallback behavior when data might be missing or unexpected
- Provide meaningful defaults that make sense for your application
- Validate the retrieved value before using it
- Consider using the function parameter directly when available
- Use descriptive variable names to clarify intent


```python
@app.route("/dashboard/<language>/<section>")
def dashboard_section(language, section):
    print(f"URL params as function args: {language}, {section}")
    print(f"view_args: {request.view_args}")  
    
    # Safe access to URL parameters
    current_language = request.view_args['language'] 
    current_language = request.view_args.get('language', 'html')
    current_section = request.view_args.get('section', 'overview')
    
    # Route information
    print(f"Endpoint: {request.endpoint}") 
    print(f"URL Rule: {request.url_rule}") 
    print(f"Path: {request.path}")  
    print(f"Full URL: {request.url}") 
    print(f"Base URL: {request.base_url}")
```
