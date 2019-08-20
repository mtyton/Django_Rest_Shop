# Django_Rest_Shop
Simple shop website based on Django Rest Framework
# Available paths:
### items/
### admin/
### api-auth
# Quick Start
Simply clone this repository in the directory with venv
More about venv creation:
- https://docs.python.org/3/library/venv.html<br>

To make it work you need to install<br>
#### Django
#### Django Rest Framework
to install first activate virtual environment:
### For Linux
```source /{venv}/bin/activate ```
### For Windows
```{venv}/Scipts/activate ```<br>
After activation simply install using pip, for example:<br>
```pip install Django```

# Views
Made using viewsets
## CategoryView
Category view shows us items and subcategories for every category, it allows us to easy download neccesarry data
for example:
```
{
            "url": "http://localhost:8000/items/categories/1/",
            "subcategories": [
                "Computers",
                "Mobile Phones"
            ],
            "belonging_items": [
                "Nokia 3310"
            ],
            "name": "Electronics",
            "pid": null
        }
```
## ItemView
Item View gives us information about Items which belgons to categories.
Item belgonging is showed by ManyToMany field "categories"
Example:
```
"count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "categories": [
                "http://localhost:8000/items/categories/1/",
                "http://localhost:8000/items/categories/3/"
            ],
            "name": "Nokia 3310",
            "price": 550.0,
            "available": true
```
