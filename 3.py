# Question 3
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
            random_string = generate(10, 15)
            file.write(random_string + '\n')
            written_bytes += len(random_string.encode())

if __name__ == "__main__":
    num_files = 10
    target_size_bytes = 5 * 1024 * 1024  # 5 MB

    for i in range(1, num_files + 1):
        file_name = f"Q3_{i}.txt"
        create(file_name, target_size_bytes)
        actual_size_mb = os.path.getsize(file_name) / (1024 * 1024)
        print(f"File '{file_name}' with size ~{actual_size_mb:.2f} MB has been created.")
