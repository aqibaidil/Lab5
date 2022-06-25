from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.249.4',  #Your Server IP
    'username': 'aqib', #your Server Username
    'password': 'aidil', #your server password
    'port' : '24',
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('uname -a')
print(output)

