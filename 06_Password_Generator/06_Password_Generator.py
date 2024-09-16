import random


class PasswordGenerator:
    def __init__(self, password_length):
        self.len = password_length

    def generate(self):
        final_pwd = ''
        for _ in range(self.len):
            current_random_number = random.randint(33, 126)  # Getting only letters, numbers and special symbols
            final_pwd += chr(current_random_number)
        return final_pwd

    def main(self):
        print(self.generate())


if __name__ == '__main__':
    pwd_len = int(input('Enter password length: '))
    pwd = PasswordGenerator(pwd_len)
    pwd.main()
