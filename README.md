# Django_Rest_Shop
Simple shop website based on Django Rest Framework
# Available paths:
### items/
### admin/
### api-auth
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
