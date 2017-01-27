from __future__ import print_function
from flask import Flask,render_template, request, url_for, redirect
import sys, os,yaml
import simplejson as json

TESTBEDS=[]
TESTBED_JSON=[]
SELECTED_VIEW='testbed_1'

def jsonParse(file_name):
    global TESTBEDS,TESTBED_JSON
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_data = os.path.join(SITE_ROOT,file_name)
    print(json_data, file=sys.stderr)
    data = yaml.safe_load(open(json_data))
    print(json.dumps(data), file=sys.stderr)
    print(data.keys(), file=sys.stderr)
    for testbed in data['children']:
        TESTBEDS.append(testbed['name'])
        TESTBED_JSON.append(testbed['children'])


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('example.html',testbeds=TESTBEDS,current_testbed=SELECTED_VIEW)
    #return "Hello World!"

@app.route('/change', methods=['POST'])
def change_testbed():
    global SELECTED_VIEW
    SELECTED_VIEW = request.form.get('testbed_select')
    print('hahahaha'+SELECTED_VIEW, file=sys.stderr)
    return url_for('main')

@app.route('/reserve/<testbed>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Testbed %s' % username

if __name__ == "__main__":
    jsonParse('sampleReservedJson.json')
    app.run()