# Keeping the active tab highlighting when navigating between pages
- pass a variable from your application's routes to the Jinja template and use a conditional statement to apply the active CSS class

### Steps
1. Set up your menu template
    - should contain the navigation links and if statements to check if the active_page variable passed from the application matches the current link's identifier
    - if statement to apply active class for each link in the menu
        - `<a href="{{ url_for('home') }}" class="nav-link {% if active_page == 'home' %}active{% endif %}">Jinja</a>`
2. Set up your base template
    - should contain the main structure of your application, including the navigation menu
    - this template is inherited by all other pages
3. Define the style for the active class
4. Pass the `active_page` variable from your routes
    - for each route in your application, you need to render the corresponding page and explicitly pass the `active_page` variable to your templates
        - `return render_template('home.html', active_page='home')`
5. Create individual page templates
    - these templates should extend base.html and provide content for the main block
    - thi way you don't need to repeat the menu structure for each template
    - `{% extends "base.html" %}`






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
