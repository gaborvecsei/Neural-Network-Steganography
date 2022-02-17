import string
from pathlib import Path
import random


def generate_dummy_data(size_in_bytes: int):
    """
    Generate a file with random printable characters with the defined file size
    """

    size_in_bytes = int(size_in_bytes)
    chars = "".join([random.choice(string.printable) for _ in range(size_in_bytes)])
    return chars


def generate_dummy_data_to_file(file_path:Path, size_in_bytes: int):
    """
    Generate a file with random printable characters with the defined file size
    """

    chars = generate_dummy_data(size_in_bytes=size_in_bytes)
    with open(file_path, 'w') as f:
        f.write(chars)

