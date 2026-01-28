def connection_string(protocol, host, port):
    return f'{protocol}://{host}:{port}'

connection_string('https','server1','443')
def show_connection(connection_string):
    print(connection_string)
show_connection(connection_string('https','server1','443'))