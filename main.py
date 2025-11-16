#! /usr/bin/python3

__production__ = True

import models
import postgresLib
import datetime
import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path="", static_folder="static")

SQLALCHEMY_DATABASE_URI \
    = ('postgresql://'+os.environ['DATAUSER'] + ':' + os.environ['DATAPWD'] + '@'
       + os.environ['DATAHOST'] + ':' + os.environ['DATAPORT'] + '/'+ os.environ['DATA1'] +'?sslmode=require')
# print(SQLALCHEMY_DATABASE_URI)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# Format of the URI is postgresql (not postgre): // Username: Password@HostName:Port/DatabaseName?sslmode=require
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Recommended for performance
db = SQLAlchemy(app)
dbModels = models.initModels(db)

@app.route("/", methods=['GET', 'POST'])
def inspiration():
    if request.method == "GET":
        return render_template('inspiration.html')
    elif request.method == "POST":
        if 'submitBtn' in request.form:
            button_value = request.form['submitBtn']
            if button_value == 'Submit Inspiration':
                inspirationTitle = request.form.get('inputTxtInspirationTitle')
                inspirationContent = request.form.get('textareaInspirationContent')
                outputString = "Your inspiration title is: " + inspirationTitle + "<br /><br />"
                outputString += "Your inspiration content is: " + inspirationContent + "<br><br />"
                print(outputString)
                outputString = outputString.replace('\n', '<br />')
        return render_template('inspiration.html', outputFieldContent=outputString)

@app.route("/hello")
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())


@app.route('/users/', methods=['GET', 'POST'])
def user():
    return render_template('user.html')


@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == "GET":
        return render_template('process.html')
    elif request.method == "POST":
        data = request.get_json()  # retrieve the data sent from JavaScript
        # process the data using Python code
        result = data['value'] * 2  # repeats it twice
        return jsonify(resultFromFlask=result)  # return the result to JavaScript


@app.route('/maps', methods=['GET', 'POST'])
def maps():
    if request.method == "GET":
        return render_template('maps.html')
    elif request.method == "POST":
        data = request.get_json()  # retrieve the data sent from JavaScript
        # process the data using Python code
        result = data['value'] * 2  # repeats it twice
        return jsonify(resultFromFlask=result)  # return the result to JavaScript

@app.route('/data', methods=['GET', 'POST'])
def dataMtd():
    outputString = ""
    if request.method == "GET":
        return render_template('dataFile.html')
    elif request.method == "POST":
        if 'tableBtns' in request.form:
            button_value = request.form['tableBtns']
            if button_value == 'Create All Tables':
                postgresLib.createAllTables(app, db)
                outputString = "All tables have been successfully created. <br>"

            elif button_value == 'Drop All Tables':
                postgresLib.deleteAllTables(app, db)
                outputString = "All tables deleted."

            elif button_value == 'Get Postgres Version':
                outputString = "Version: " + postgresLib.getVersion(SQLALCHEMY_DATABASE_URI)

            elif button_value == "Add Data":
                postgresLib.addData(db, dbModels)
                outputString = "Data added."

            elif button_value == "Drop Data":
                postgresLib.dropData(db, dbModels)
                outputString = "Data dropped."

        return render_template('dataFile.html', outputFieldContent=outputString)


@app.route('/forms', methods=['GET', 'POST'])
def formsMtd():
    outputString = ""
    if request.method == "GET":
        return render_template('formsFile.html')
    elif request.method == "POST":
        if 'particularsBtn' in request.form:
            button_value = request.form['particularsBtn']
            if button_value == 'Save':
                outputString += "Name: " + request.form['name'] + "<br>"
                outputString += "Email: " + request.form.get('email', '') + "<br>"
                outputString += "Message: " + request.form.get('message', '') + "<br>"  # .get() is safer for optional fields
            elif button_value == 'Delete':
                outputString += "Record is deleted."

        return render_template('formsFile.html', outputFieldContent=outputString)


def test():
    outputString = "Version: " + postgresLib.getVersion(SQLALCHEMY_DATABASE_URI)
    print(outputString)

if __name__ == "__main__":
    if not __production__:
        app.run(host='0.0.0.0', port=5000)
        # test()


