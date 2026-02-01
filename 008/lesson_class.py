class Server:
    def __init__(self, login, password, api_url):
        self.login = login
        self.password = password
        self.api_url = api_url
    



host1 = Server('login', 'password')
print(host1.login)

# 'https://api.restful-api.dev/objects'
# requests status_code, json()