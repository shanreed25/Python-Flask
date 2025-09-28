# 📁 File Uploads (request.files)
- File uploads are handled through a special form data type
- HTML File Upload Form
```html
<form method="POST" action="/upload" enctype="multipart/form-data">
    <input type="file" name="avatar" accept="image/*">
    <input type="file" name="documents" multiple>
    <input type="text" name="description">
    <button type="submit">Upload</button>
</form>
```
- Processing File Uploads
```python
import os
from werkzeug.utils import secure_filename

@app.route("/upload", methods=['POST'])
def upload_files():
    # Check if file was uploaded
    if 'avatar' not in request.files:
        return "No file selected", 400
    
    file = request.files['avatar']
    
    # Check if file was actually selected
    if file.filename == '':
        return "No file selected", 400
    
    # Process single file
    if file and allowed_file(file.filename):
        # Secure the filename
        filename = secure_filename(file.filename)
        
        # Save file
        file.save(os.path.join('uploads', filename))
        
        # File properties
        file_info = {
            'original_name': file.filename,
            'secure_name': filename,
            'content_type': file.content_type,
            'content_length': file.content_length
        }
    
    # Process multiple files
    documents = request.files.getlist('documents')
    uploaded_docs = []
    
    for doc in documents:
        if doc and doc.filename != '':
            filename = secure_filename(doc.filename)
            doc.save(os.path.join('uploads/docs', filename))
            uploaded_docs.append(filename)
    
    # Regular form data still available
    description = request.form.get('description', '')
    
    return {
        'avatar': file_info,
        'documents': uploaded_docs,
        'description': description
    }

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}
```




____________________________________________