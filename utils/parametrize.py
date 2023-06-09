import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

import json

def get_input(test_name):
    """ Parses JSON file (filename) and returns the list of inputs for the specified test case (test_name) """
    data_file = os.path.join(project_path, "utils", "testdata.json") # TODO improve
    with open(data_file) as fn:
        for td in json.load(fn):
            if td["tc_name"] == test_name:
                return list(td["inputs"])