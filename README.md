# Python-Flask-Todo-App

For getting app.db file at ->
python (in shell)
(inside interpreter run the below code):

```
from app import db, app

with app.app_context():
    db.create_all()

print("Database created successfully!")
```
