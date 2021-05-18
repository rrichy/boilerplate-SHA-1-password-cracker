import hashlib

def crack_sha1_hash(hash, use_salts=False):
    password_list = []
    with open('top-10000-passwords.txt', 'r') as f:
        password_list = f.readlines()

    salts = []
    with open('known-salts.txt', 'r') as f:
        salts = f.readlines()

    if use_salts is not True:
        for password in password_list:
            if hashlib.sha1(password.strip().encode()).hexdigest() == hash:
                return password.strip()
    else:
        for salt in salts:
            for password in password_list:
                if hashlib.sha1((salt.strip() + password.strip()).encode()).hexdigest() == hash:
                    return password.strip()
                if hashlib.sha1((password.strip() + salt.strip()).encode()).hexdigest() == hash:
                    return password.strip()

    return 'PASSWORD NOT IN DATABASE'