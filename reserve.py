from __future__ import print_function
from flask import Flask,render_template, request, url_for, redirect, jsonify
import sys, os,yaml
import simplejson as json

TESTBEDS=[]
TESTBED_JSON=[]
SELECTED_VIEW=''

def jsonParse(file_name):
    global TESTBEDS,TESTBED_JSON
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_data = os.path.join(SITE_ROOT,file_name)
    #print(json_data, file=sys.stderr)
    data = yaml.safe_load(open(json_data))
    #print(json.dumps(data), file=sys.stderr)
    #print(data.keys(), file=sys.stderr)
    for testbed in data['children']:
        TESTBEDS.append(testbed['text'])
        TESTBED_JSON.append(testbed)


app = Flask(__name__)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route("/", methods=['GET','POST'])
def main():
    global SELECTED_VIEW
    if request.method == 'POST':
        SELECTED_VIEW = request.form.get('testbed_select')
    if SELECTED_VIEW == '' or SELECTED_VIEW == None:
        SELECTED_VIEW = TESTBEDS[0]
    t = None
    for test in TESTBED_JSON:
        if test['text'] == SELECTED_VIEW:
            t=test
    if t == None:
        t = {'text':'Failed to Load JSON'}
    #print(t, file=sys.stderr)

    return render_template('index.html',testbeds=TESTBEDS,current_testbed=SELECTED_VIEW,testbed_data=json.dumps(t['children']))

@app.route('/_reserve_component')
def reserve_component():
    user = request.args.get('user')
    time = request.args.get('time')
    duration = request.args.get('duration')
    email =request.args.get('email')
    print(user, file=sys.stderr)
    print(time, file=sys.stderr)
    print(duration, file=sys.stderr)
    print(email, file=sys.stderr)
    return 'done'

if __name__ == "__main__":
    jsonParse('sampleReservedJson.json')
    app.run()