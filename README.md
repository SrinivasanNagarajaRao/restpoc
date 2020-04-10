#**RestPOC**

###**Step 1:** 
To install required packages
```pip install -r requirements.txt```

###**Step 2:** 
**constants.py** file have api url that receives the response and has data path that saves the data

###**Step 3:** 
Schedule rest_call.py using cron, so that it keeps pulling the data from the rest endpoint and keep the data upto date.
```python rest_call.py```

**__init__** method reads the data from the requested API
**write_response** save it in the data folder as csv file

```import csv
import requests
import constants
from pprint import pprint as p


class runner(object):
    """Whole runner class to schedule it in cronjob"""

    def __init__(self, url):
        """Get response data from the url and save it locally"""
        self.response_dict = requests.get(url).json()
        # p(self.response_dict['data'])
        self.data = self.response_dict['data']
        self.header_field = list(self.response_dict['data'][0].keys())

    def write_response(self, path):
        """write the returned data into a csv file to release as API"""
        with open(path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=self.header_field)
            writer.writeheader()
            writer.writerows(self.data)
        return "Success"


help(runner)
print(runner(constants.url).write_response(constants.data_path))
```

###**Step 3:** 
Run release_api.py to read the updated data and release it as an api.
``python release_api.py``

Reading and Exposing the data as api in "/" path : localhost:5000/ it'll be response as json
**release** method reads csv files and exposes it as json data, sends 200 status to the api

```import csv
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
```