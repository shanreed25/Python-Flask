# **📄 Request Object: Content and JSON Handling**
```python
@app.route("/api/submit", methods=['POST'])
def api_submit():
    # Content Type checking
    print(f"Content-Type: {request.content_type}")
    print(f"Content-Length: {request.content_length}")
    
    # JSON Data
    if request.is_json:
        data = request.get_json()  # Parses JSON automatically
        
        # Safe JSON parsing with error handling
        try:
            json_data = request.get_json(force=True)
        except:
            return {'error': 'Invalid JSON'}, 400
    
    # Raw request data
    raw_data = request.data                  # Raw bytes
    text_data = request.get_data(as_text=True)  # Raw data as text
    
    # Request body stream (for large uploads)
    stream_data = request.stream.read()
```