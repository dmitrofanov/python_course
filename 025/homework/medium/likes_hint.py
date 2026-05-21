likes = {
    "post_1": {"Анна", "Иван", "Мария"},
    "post_2": {"Иван", "Петр"},
    "post_3": {"Анна", "Мария", "Ольга", "Сергей"},
    "post_4": set(),
}

print("Статистика лайков:")
for post, users in likes.items():
    count = len(users)
    if count == 0:
        print(f"  {post}: никто не лайкнул")
    elif count == 1:
        print(f"  {post}: {', '.join(users)} лайкнул(а)")
    else:
        print(f"  {post}: {count} лайков — {', '.join(users)}")