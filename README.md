# Welcome to my Flask-Microblog!

---

### Flask commands in the terminal

- Don't forget to setup FLASK_APP in '.flaskenv' file.
- If the above point is ignored, use the following command:

```python
export FLASK_APP=microblog.py
```

- Import 'db' and other database models.

---

### SQLAlchemy

- It's an Object Relational Mapper.
- Used for simplifying sql queries.
- Has its own query methods like 'get(), filter_by(), all(), desc(), first()' etc.

---

### Database models

- Every table must have a 'primary_key'.
- To link one table to another type use 'db.ForeignKey'.

---

### Flask-Migrate

- To initiate flask-migration database:

```python
flask db init
```

- To tack a database change:

```python
flask db migrate -m "<some optional user message>"
```

- The above only screate a migration script of the changes in the database.
- To save the changes:

```python
flask db upgrade
```

- The above command also creates a database if none exists.

- To revert the changes:

```python
flask db downgrade
```

---

### Password Security

- Done using werkzeug security dependency which is preinstalled with flask.
- To implement:

```python
from werkzeug.security import generate_password_hash, check_password_hash
```

- Import and define the above modules in a User model in 'models.py'.

---

### Flask-Login

- To remember user login session.
- Import the follwing in 'models.py'.

```python
from flask_login import UserMixin
```

- Add the imported module to the User model class.
- Import and initiate the following in "_init_.py".

```python
from flask_login import LoginManager
```

- Pass the flask app through the login manager.

```python
login = LoginManager(app)
```

- Import and use 'url_for()' instead of relative paths for templates.

---

### User Registration Form

- Create a class RegistrationForm and import FlaskForm.
- import validators using wtforms.validators. Ex - DataRequired, ValidationError, EqualTo.
- A ValidationError is used to raise an error if the username or email address already exists.
