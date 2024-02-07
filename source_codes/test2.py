from adapter import Adapter


controller_param = {
    "controller_ip": "192.168.200.101",
    "controller_pass": "admin",
    "controller_port": "8181",
    "controller_uname": "admin"
}

adapter= Adapter(**controller_param)

topo = adapter.fetch_topo()

print(topo)