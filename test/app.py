from flask import Flask,render_template,request,stream_with_context,make_response,jsonify
import numpy as np
import csv
from flask_socketio import SocketIO, send
from flask import Response
from flask_cors import CORS
import pandas as pd
import os
import json
from time import sleep
app = Flask(__name__)


@app.route('/ilk')
def final():

    enlem=[]
    boylam=[]
    with open("20210318_irkit_test_1.txt") as file:

        csv_reader = csv.DictReader(file)

        for i in csv_reader:
            enlem.append(i['LATITUDE'])
            boylam.append(i['LONGITUDE'])
    
    return render_template("plotly.html",enlem=enlem,boylam=boylam)

@app.route('/')
def deneme():
   return render_template('test2.html')





@app.route('/deneme3', methods=["GET", "POST"])
def deneme3():  
    while True:
        enlem=[]
        boylam=[]
        with open("20210318_irkit_test_1.txt") as file:

            csv_reader = csv.DictReader(file)

            for i in csv_reader:
                enlem.append(i['LATITUDE'])
                boylam.append(i['LONGITUDE'])
        data=[enlem,boylam]
        #response=make_response(json.dumps({'enlem':enlem, 'boylam':boylam}))
        response=make_response(json.dumps(data))
        response.content_type='application/json'

        return response


if __name__ == '__main__':
    app.debug = True
    app.env = 'development'
    app.run(host='localhost', port=7777)