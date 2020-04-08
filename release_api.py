import csv
import json
import pandas
import constants
from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def release():
    '''read csv file and return as json response'''
    data = pandas.read_csv(filepath_or_buffer=constants.data_path)
    response_data = data.to_json(orient='records')
    return Response(status=200, response=response_data, mimetype='application/json')


if __name__ == '__main__':
    app.run()
