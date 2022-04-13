from app_package import app, db
from app_package.models import User, Post


# Used to preimport modules during the 'flask shell' command.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run(debug=True)
