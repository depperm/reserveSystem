from __future__ import print_function
from flask import Flask
from flask import render_template
import sys, os,yaml
import simplejson as json

TESTBEDS=[]
TESTBED_JSON=[]

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
def hello():
    return render_template('example.html',testbeds=TESTBEDS)
    #return "Hello World!"

@app.route('/reserve/<testbed>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Testbed %s' % username

if __name__ == "__main__":
    jsonParse('sampleReservedJson.json')
    app.run()