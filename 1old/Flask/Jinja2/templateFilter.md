# Jinja2 Template Filter
**The `|` (pipe symbol) applies a filter to transform a variable's value**


###### Example: `nav_item1|lower`
- `nav_item = "HTML"`
- `nav_item|lower`
    - Takes the value of nav_item variable, applies the lower filter to it and converts the text to lowercase
    - becomes `html`


### Common Jinja2 Filters
- **`|lower`:**onvert to lowercase
- **`|upper`:**onvert to uppercase
- **`|title`:**onvert to title case
- **`|length`:** get length of string/list
- **`|default('fallback')`:** povides default value
- **`|safe`:** mark as safe HTML (no escaping)
