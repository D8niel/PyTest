from tkinter.constants import RAISED

import psycopg2
from flask_sqlalchemy import SQLAlchemy


def getVersion():
    conn = psycopg2.connect(
        'postgres://avnadmin:AVNS_6BzdMfayzfNaDSkLPYy@pg-281907f9-pytest001.f.aivencloud.com:17050/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    return version


def createDataBase(app, db):
    raise ValueError("Database must be created manually.")
    print("Database must be created manually")


def createAllTables(app, db):
    with app.app_context():
        db.create_all()


def addData(db: SQLAlchemy, db_models):
    UserClass = db_models["User"]
    user_test = UserClass(username='John', email='jd@example.com', message='This is added by the app.')
    try:
        db.session.add(user_test)
        db.session.commit()
    except Exception as e:
        print("Exception raised: \n", e, "\nEnd of Exception")


def dropData(db: SQLAlchemy, db_models):
    UserClass = db_models["User"]
    UserClass.query.filter(UserClass.username == "John").delete()
    db.session.commit()


def deleteAllTables(app, db: SQLAlchemy):
    with app.app_context():
        db.drop_all()