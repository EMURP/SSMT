from flask import Blueprint,render_template
from flask import request
from flask.json import jsonify
import json
import requests
import datetime
import constants
from helper import helper

list_projects = Blueprint("list_projects",__name__)
util_object = helper.Helper()

@list_projects.route('/<project_name>')
def list_all_projects(project_name):
    period_start, period_end = util_object.getOneHour()
    url = constants.FLASK_APP_URL + '/list_projects/' + str(project_name) +'/'+ period_start + '/'+ period_end
    r = requests.get(url, verify=False)
    return r.text

@list_projects.route('/<project_name>/<period_start>/<period_end>')
def get_project_reports(project_name,period_start, period_end):
    headers = util_object.getRequestHeader()
    url = constants.METERING_ROUTE_LIST_ALL_PROJECTS
    r = requests.get(url, headers=headers, verify=False)
    input_json = r.text
    input_dict = json.loads(input_json)
    data = [x for x in input_dict if (x['period_start'] == period_start or x['period_end'] == period_end)]
    data = [x for x in data if x['namespace'] == project_name]
    if len(data) == 0:
        return "Report are not Generated. Please Wait until OpenShift Cluster Collect Metrics"
    else:
        return jsonify(data)
