with open("016/poem.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end='')  # end="" чтобы не было двойных переносов