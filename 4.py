# Question 4
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
            random_string = generate(10, 11)
            file.write(random_string + '\n')
            written_bytes += len(random_string.encode())

if __name__ == "__main__":
    sizes_gb = [1, 2, 3, 4, 5]

    for size_gb in sizes_gb:
        target_size_bytes = size_gb * 1024 * 1024 * 1024
        file_name = f"Q4_{size_gb}GB.txt"
        create(file_name, target_size_bytes)
        actual_size_gb = os.path.getsize(file_name) / (1024 * 1024 * 1024)
        print(f"File '{file_name}' with size ~{actual_size_gb:.2f} GB has been created.")
# These Questions took too long to excecute thats why full excecution has not been shown