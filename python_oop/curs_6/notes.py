"""
    Serializare= transformarea unui obiect ıntr-o secvent¸˘a de octet¸i, din care s˘a
    poat˘a fi ref˘acut ulterior obiectul original.
    Procesul invers, de citire a unui obiect
    serializat pentru a-i reface starea original˘a, se nume¸ste deserializare.

"""
import os

# get absolute path
ab_path = os.path.abspath("app/")
print(ab_path)


# get current working directory
current_dir = os.getcwd()
print(current_dir)

link_path = r"/python_oop"


#iterator prin folderul dat
def print_dirs(link_path):
    for root, directories, files in os.walk(link_path):
        for filenames in files:
            return filenames