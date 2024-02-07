from flask import Flask,request
from adapter import Adapter
import json

app = Flask(__name__)

@app.route('/')
def index():
    return('hello')

@app.route('/get_full_topo', methods=['GET'])
def get_full_topo():
    args = request.args
    adapter = Adapter(**args)
    link_list = adapter.fetch_full_topo()
    print(link_list)
    return(json.dumps(link_list))
    
@app.route('/get_switch_topo', methods=['GET'])
def get_switch_topo():
    args = request.args
    adapter = Adapter(**args)
    link_list = adapter.fetch_switch_topo()
    print(link_list)
    return(json.dumps(link_list))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)