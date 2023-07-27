# Question 2
import random
import string
import os

def generate(min_length, max_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(random.randint(min_length, max_length)))

def create(file_name, target_size_in_bytes):
    with open(file_name, 'w') as file:
        written_bytes = 0
        while written_bytes < target_size_in_bytes:
            random_string = generate(10, 20)
            file.write(random_string + '\n')
            written_bytes += len(random_string.encode())

if __name__ == "__main__":
    file_name = "Question2_random.txt"
    target_size_bytes = 5 * 1024 * 1024  # 5 MB

    create(file_name, target_size_bytes)
    actual_size_mb = os.path.getsize(file_name) / (1024 * 1024)

    print(f"File '{file_name}' with size ~{actual_size_mb:.2f} MB has been created.")
