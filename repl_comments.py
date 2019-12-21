from hashlib import sha256


def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()


my_hashed_password = "8e20775010852c6e583e1d0510b50644011ebca66e6930cd14d848926a39070a"
comment_list = []

while True:
    comment = input('Please enter your comment: ')
    pw1 = input('Please enter your password: ')
    hsh1 = create_hash(pw1)
    if my_hashed_password == hsh1:
        comment_list.append(comment)
    else:
        print('I am sorry I can’t let you do that.')
    print("Previously entered comments: ")
    for i in range(len(comment_list)):
        print(comment_list[i])
