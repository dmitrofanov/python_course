"""
У тебя есть словарь, где ключ — пост, значение — множество поставивших лайк.
Для каждого поста выведи количество лайков и список имён.
"""
likes = {
    "post_1": {"Анна", "Иван", "Мария"},
    "post_2": {"Иван", "Петр"},
    "post_3": {"Анна", "Мария", "Ольга", "Сергей"},
    "post_4": set(),
}

for post, users in likes.items():
    likes_count = len(users)
    if users:
        names = ",".join(users)
    else:
        names = "лайков нет"

    print(f"{post} :{likes_count} - {names}")