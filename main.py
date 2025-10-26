#! /usr/bin/python3

__production__ = False

import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path="", static_folder="static")


@app.route("/")
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


@app.route('/develop', methods=['GET', 'POST'])
def developMtd():
    if request.method == "GET":
        return render_template('developFile.html')
    elif request.method == "POST":
        if 'particularsBtn' in request.form:
            button_value = request.form['particularsBtn']
            if button_value == 'Save':
                name = request.form['name']
                email = request.form['email']
                message = request.form.get('message', '')  # .get() is safer for optional fields
            elif button_value == 'Delete':
                name = "Deleted"
                email = "Deleted"
                message = "Deleted"
            # Process the captured data (e.g., print, save to database, send email)
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Message: {message}")
        return render_template('developFile.html')

if __name__ == "__main__":
    if not __production__:
         app.run()
    # else:
    #     from waitress import serve
    #     serve(app, host='0.0.0.0', port=80)


