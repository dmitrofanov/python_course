# 5) Даны следующие переменные
ip_addr = '192.168.20.43'
hostname = 'application-server-001'
# создай словарь с помощью функции dict и с помощью синтаксиса литерала, в котором значения будут взяты из этих переменных. Имена для ключей выбери сам (можно взять такие же как имена переменных).

server_l = {"ip_addr": ip_addr,"hostname": hostname}
server_d = dict(ip_addr = ip_addr,hostname = hostname)
print(server_l)
print(server_d)