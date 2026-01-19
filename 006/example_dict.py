from pprint import pprint

host = '192.168.16.234'
name = 'Web-Server-001'
rps = 200
logs_volume = 300 * 1024 ** 2

stats = dict(name=name, rps=rps, logs_volume=logs_volume)
machines = {host: stats}

pprint(machines)

host = '192.168.200.53'
name = 'Application-Server-001'
rps = 3000
logs_volume = 5 * 1024 ** 3

machines[host] = {'name': name, 'rps': rps, 'logs_volume': logs_volume}
pprint(machines)