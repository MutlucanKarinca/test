from flask import Flask,render_template,request
import numpy as np
import csv
from flask_socketio import SocketIO 
app = Flask(__name__)


@app.route('/')
def final():

    enlem=[]
    boylam=[]
    with open("20210318_irkit_test_1.txt") as file:

        csv_reader = csv.DictReader(file)

        for i in csv_reader:
            enlem.append(i['LATITUDE'])
            boylam.append(i['LONGITUDE'])
    
    return render_template("plotly.html",enlem=enlem,boylam=boylam)


if __name__=="__main__":
    app.run(debug=True)