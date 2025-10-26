from flask_sqlalchemy import SQLAlchemy

def initModels(db: SQLAlchemy):
    returnValue = dict()
    class User(db.Model):
        __tablename__ = "User"
        __table_args__ = {"schema": "pytest_schema"}
        # A specific schema, pytest_schema was set up manually in the database otherwise drop_all does not work.
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120))
        message = db.Column(db.String(120))

        def __repr__(self):
            return f'<User {self.username}>'
    returnValue["User"] = User

    class Book(db.Model):
        __tablename__ = "Book"
        __table_args__ = {"schema": "pytest_schema"}
        # A specific schema, pytest_schema was set up manually in the database otherwise drop_all does not work.
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(80), unique=True, nullable=False)
        author = db.Column(db.String(120))
        description = db.Column(db.String(120))

        def __repr__(self):
            return f'<User {self.title}>'
    returnValue["Book"] = Book

    return returnValue
