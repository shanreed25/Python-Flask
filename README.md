# Flask-Projects






### Flask Examples
- [Getting Started](./GettingStarted/get_started_flask.py)
    - routing
- [URL Paths](./GettingStarted/url_paths.py)
    - debugging
    - variable
- [Higher Or Lower](./GettingStarted/higher_lower.py)
- [Rendering HTML](./GettingStarted/html_elements.py)
- [Custom Decorators](.GettingStarted/custom_decorators.py)
- [Flask App: Jinja Templating]()
    - Using Jinja to Produce Dynamic HTML Pages
    - Combining Jinja Templating with APIs
    - Multiline Statements
    - for loop 
    - if statement
    - URL Building with Flask(`url_for`)
- [Make POST Requests with Flask and HTML Forms](./flaskApp/server.py)
- [Forms](./contactFormFlaskApp/server.py)
- [WTForms](./WTFForms/server.py)
- [Bootstrap Flask WTFoms](./Bootstrap-Flask-WTForms/main.py)
- [DB Integration with SQLAlchemy](./DBFlaskSQLAlchemy/README.md)
- [Flask Authentication]()
- []()
- []()


### Flask Docs
- [Flask PYPI Package](https://pypi.org/project/Flask/)
- [Quick Start Docs](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Routing](https://flask.palletsprojects.com/en/stable/quickstart/#routing)
- [Variables Rules](https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules)
- [Debug Mode](https://flask.palletsprojects.com/en/stable/quickstart/#debug-mode)
- [Rendering Templates](https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates)
    - For templates you can use the full power of [Jinja Templates](https://jinja.palletsprojects.com/en/stable/templates/)



To add {% include "menu.html" %} as literal text on an HTML page, rather than having it processed as a template include, you need to escape the special characters. This involves replacing the < and > characters with their corresponding HTML entities.
Here's how to do it:
Code

- `<p>&lbrace;&percnt; include &quot;menu.html&quot; &percnt;&rbrace;</p>`
###### Explanation of Entities:
- &lbrace; represents {
- &percnt; represents %
- &quot; represents "
- &rbrace; represents }
**By using these HTML entities, the browser will render the text literally, displaying {% include "menu.html" %} instead of attempting to process it as a template directive.**