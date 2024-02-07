import requests 
import json

class Adapter:
    def __init__(self,controller_ip:str, controller_port:str, controller_uname:str, controller_pass:str):
        self.controller_ip=controller_ip
        self.controller_port=controller_port
        self.controller_uname=controller_uname
        self.controller_pass=controller_pass

    def fetch_full_topo(self) -> list:
        session = requests.Session()
        link_list=[]

        try:
            session.auth = (self.controller_uname, self.controller_pass)
            req_str=f"http://{self.controller_ip}:{self.controller_port}/restconf/operational/network-topology:network-topology"
            response = session.get(req_str)
            session.close()
            
            raw_topo_json=bytes.decode(response.content)
            raw_topo = json.loads(raw_topo_json)

            links = raw_topo['network-topology']['topology'][0]['link']

            for link in links:
                source_node=link['source']['source-node']
                destination_node=link['destination']['dest-node']
                link_list.append(tuple([source_node,destination_node]))
            return link_list
        except Exception as e:
            return {'Error':str(e)}
        
    def fetch_switch_topo(self) -> list:
        session = requests.Session()
        link_list=[]

        try:
            session.auth = (self.controller_uname, self.controller_pass)
            req_str=f"http://{self.controller_ip}:{self.controller_port}/restconf/operational/network-topology:network-topology"
            response = session.get(req_str)
            session.close()
            
            raw_topo_json=bytes.decode(response.content)
            raw_topo = json.loads(raw_topo_json)

            links = raw_topo['network-topology']['topology'][0]['link']

            for link in links:
                source_node=link['source']['source-node']
                destination_node=link['destination']['dest-node']
                if source_node.split(':')[0] == 'openflow' and destination_node.split(':')[0] == 'openflow':
                    link_list.append(tuple([source_node,destination_node]))
                    
            return link_list
        except Exception as e:
            return {'Error':str(e)}
        
        
            