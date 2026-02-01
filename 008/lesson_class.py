import requests

servers = [
    '192.168.10.43',
    '192.168.10.44',
    '192.168.10.45',
    '192.168.10.46',
]

class Server:
    def __init__(self, ip, login, password):
        self.ip = ip
        self.login = login
        self.password = password
        print(f'Initialized {ip}')

    def get_properties(self):
        print(f'Connecting to {self.ip} using {self.login}/{self.password}')
        response = requests.get('https://api.restful-api.dev/objects')
        item = response.json()[1]
        return dict(model=item['name'], serial=item['id'])



for ip in servers:
    server = Server(ip, 'SUPER_LOGIN', 'SUPER_PASSWORD')
    print(server.get_properties())