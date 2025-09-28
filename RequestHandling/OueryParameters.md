# **🔍 Request Object: Query Parameters and Form Data**


- `request.` :
- `request.` :
- `request.` :
- `request.` :
- `request.` :
- `request.` :
- `request.` :
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