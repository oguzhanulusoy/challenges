import random
import string

def get_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range (int(length)))

if __name__ == "__main__":
    size = input("Enter size: ")
    for_what = input("For what: ")
    new_file = open(for_what + ".txt", "w")
    password = get_random_string(size)
    new_file.write(password)
    new_file.close()
    print("Generated password is v0+" + password)
