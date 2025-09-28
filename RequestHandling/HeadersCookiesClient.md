# **🍪 Request Object: Headers, Cookies, and Client Information**
```python
@app.route("/client-info")
def client_info():
    # HTTP Headers
    user_agent = request.headers.get('User-Agent')
    content_type = request.headers.get('Content-Type')
    authorization = request.headers.get('Authorization')
    
    # Custom headers
    api_key = request.headers.get('X-API-Key')
    
    # All headers
    for header_name, header_value in request.headers:
        print(f"{header_name}: {header_value}")
    
    # Cookies
    session_cookie = request.cookies.get('session_id')
    user_pref = request.cookies.get('theme', 'light')  # Default to 'light'
    
    # Client Information
    client_ip = request.remote_addr          # Client's IP address
    user_agent_obj = request.user_agent      # Detailed user agent object
    
    # Security and Protocol
    is_secure = request.is_secure            # True if HTTPS
    protocol = request.scheme                # 'http' or 'https'
    
    return {
        'ip': client_ip,
        'browser': user_agent_obj.browser,
        'platform': user_agent_obj.platform,
        'secure': is_secure
    }
```