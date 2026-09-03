from string import ascii_lowercase,ascii_uppercase, digits, punctuation
from secrets import choice

def generate_password(pass_len, use_special_symbols=False, ignore_similar_symbols=False):
    pool = set(ascii_lowercase+ascii_uppercase+digits+(punctuation if use_special_symbols else ""))
    similar_symbols = set("lI0O`|") if ignore_similar_symbols else set()

    pool = list(pool - similar_symbols)
    lowercase = list(set(ascii_lowercase) - similar_symbols)
    uppercase = list(set(ascii_uppercase) - similar_symbols)
    digs = list(set(digits) - similar_symbols)
    puncts = list(set(punctuation) - similar_symbols)

    password = [
        choice(lowercase),
        choice(uppercase),
        choice(digs),
        choice(puncts) if use_special_symbols else ""
    ]
    for _ in range(pass_len-len(password)):
        password.append(choice(pool))

    return("".join(password))

# generate_password(10, True, True)


