# Question 5
import os
import random
import string

def generate(min_length, max_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(random.randint(min_length, max_length)))

def create(file_name, target_size_bytes):
    with open(file_name, 'w') as file:
        written_bytes = 0
        while written_bytes < target_size_bytes:
            random_string = generate(10, 100)  # Adjust the range of string lengths as needed
            file.write(random_string + '\n')
            written_bytes += len(random_string.encode())

def convert(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    
    with open(file_name, 'w') as file:
        file.write(content.upper())

if __name__ == "__main__":
    sizes_gb = [1, 2, 3, 4, 5]

    for size_gb in sizes_gb:
        target_size_bytes = size_gb * 1024 * 1024 * 1024
        file_name = f"Q4_{size_gb}GB.txt"
        create(file_name, target_size_bytes)

        print(f"File '{file_name}' created with size ~{size_gb} GB.")

        # Convert the content to uppercase
        convert(file_name)

        print(f"File '{file_name}' converted to uppercase.")
# These Questions took too long to excecute thats why full excecution has not been shown