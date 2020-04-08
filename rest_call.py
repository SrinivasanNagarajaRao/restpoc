import csv
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
