# Question 1
import random
import string

def generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def create(file_name, num_lines, string_length):
    with open(file_name, 'w') as file:
        for _ in range(num_lines):
            random_string = generate(string_length)
            file.write(random_string + '\n')

if __name__ == "__main__":
    file_name = "random_stringsQ1.txt"
    num_lines = 1000
    string_length = 10  
    create(file_name, num_lines, string_length)
    print(f"File '{file_name}' with {num_lines} random strings has been created.")
