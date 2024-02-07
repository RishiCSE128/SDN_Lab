import requests 
from pprint import PrettyPrinter
import json

pp=PrettyPrinter(indent=2)
controller_param ={
    'ip' : "192.168.200.101",
    'port' : 8181,
    'username' : 'admin',
    'password' : 'admin'
}

session = requests.Session()
session.auth = (controller_param['username'], controller_param['password'])
req_str=f"http://{controller_param['ip']}:{controller_param['port']}/restconf/operational/network-topology:network-topology"
response = session.get(req_str)
raw_topo_json=bytes.decode(response.content)
raw_topo = json.loads(raw_topo_json)
#print(raw_topo_json)

# ## topo post process
links = raw_topo['network-topology']['topology'][0]['link']
link_list=[]
for link in links:
    source_node=link['source']['source-node']
    destination_node=link['destination']['dest-node']
    link_list.append((source_node,destination_node))
print(link_list)
