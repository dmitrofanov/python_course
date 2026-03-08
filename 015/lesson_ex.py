my_list=[10, 4, 5, 45, -1, 9]
for _ in range(len(my_list)):
    for number in range(len(my_list) -1):
        if my_list[number] > my_list[number + 1]:
            my_list[number],my_list[number + 1] = my_list[number + 1],my_list[number]
    print(my_list)