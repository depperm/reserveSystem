from __future__ import print_function
from flask import Flask,render_template, request, url_for, redirect
import sys, os,yaml
import simplejson as json

TESTBEDS=[]
TESTBED_JSON=[]
SELECTED_VIEW=''

def jsonParse(file_name):
    global TESTBEDS,TESTBED_JSON
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_data = os.path.join(SITE_ROOT,file_name)
    print(json_data, file=sys.stderr)
    data = yaml.safe_load(open(json_data))
    print(json.dumps(data), file=sys.stderr)
    print(data.keys(), file=sys.stderr)
    for testbed in data['children']:
        TESTBEDS.append(testbed['text'])
        TESTBED_JSON.append(testbed)


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def main():
    global SELECTED_VIEW
    if request.method == 'POST':
        SELECTED_VIEW = request.form.get('testbed_select')
    if SELECTED_VIEW == '':
        SELECTED_VIEW = TESTBEDS[0]
    t = None
    for test in TESTBED_JSON:
        if test['text'] == SELECTED_VIEW:
            t=test
    if t == None:
        t = {'text':'Failed to Load JSON'}
    print(t, file=sys.stderr)

    return render_template('example.html',testbeds=TESTBEDS,current_testbed=SELECTED_VIEW,testbed_data=json.dumps(t['children']))

@app.route('/reserve/<testbed>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Testbed %s' % username

if __name__ == "__main__":
    jsonParse('sampleReservedJson.json')
    app.run()