#Создать функцию, принимающую имя, город и возраст и возвращающую словарь, в котором представлены эти данные.
def show_profile(name,city,age):
    return dict(name=name,city=city,age=age)
print(show_profile('Pavel','Moscow','36'))