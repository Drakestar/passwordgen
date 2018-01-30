import random


def main():
    characterlist = []
    file = open("chars.txt", 'r')
    for line in file.readlines():
        for i in line:
            characterlist.append(i)
    file.close()
    while True:
        password = []
        for x in range(0, 32):
            password.append(random.choice(characterlist))
        print(''.join(password))
        input("Hit enter for a new password")


if __name__ == "__main__":
    main()
