import networkx as nx
import matplotlib.pyplot as plt
import requests
import json
from flask import Flask



controller_param ={
    'controller_ip' : "192.168.200.101",
    'controller_port' : '8181',
    'controller_uname' : 'admin',
    'controller_pass' : 'admin'
}

print('Requesting Topology...')
adapter_url= 'http://192.168.0.109:5001/get_full_topo'
response = requests.get(adapter_url, params=controller_param)
link_list=json.loads(response.content)
links = [tuple(link) for link in link_list]
print(links)

print('Building Graph...')
g = nx.Graph()
g.add_edges_from(links)
nx.draw(g, with_labels=True)
plt.savefig('source_codes\\topo.png')
plt.show()
