l1 = [ 1,   2,   3,   4]
l2 = ['a', 'b', 'c', 'd', 'e']
l3 = list('zxcvb')

for number, char, char2 in zip(l1, l2, l3):
    print(number, char, char2)

print(list(zip(l1, l2)))

mobile_phones = ['iPhone', 'samsung', 'xiaomi']
prices = [80000, 100000, 60000]
my_dict = {phone: price for phone, price in zip(mobile_phones, prices)}
print(my_dict)



servers = [{'name':'A', 'ip': '192.168.42.22'}, ...]
availability = [True, False, True, False]