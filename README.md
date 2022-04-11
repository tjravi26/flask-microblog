# Welcome to my Flask-Microblog!

### Flask commands in the terminal

- Don't forget to setup FLASK_APP in '.flaskenv' file.
- If the above point is ignored, use the following command:

```python
export FLASK_APP=microblog.py
```

- Import 'db' and database models.

### Database models

- Every table must have a 'primary_key'.
- To link one table to another type use 'db.ForeignKey'.

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
