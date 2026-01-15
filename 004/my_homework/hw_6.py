# 6) Объяснить что делает эта программа:
string = 'Hello from Saint-Petersburg'
index = 0
while index < len(string):
    if index % 2 == 0:
        print(string[index])
    index += 1