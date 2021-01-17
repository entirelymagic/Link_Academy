import csv
from os import listdir
from os import getcwd
from os.path import isfile, join, abspath

# get the current directory of the file
mypath = getcwd()

# get all the files in the directory and put them in the list
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# create a list with all the absolute paths of the files present
file_path = [abspath(f) for f in onlyfiles]

# create a dictionary with the file names as key and filepaths as values
dict_file_path_and_names = {a: b for a, b in zip(onlyfiles, file_path)}

# write the data from the dictionary to a csv file
w = csv.writer(open("output.csv", "w"))

if __name__ == '__main__':
    for key, val in dict_file_path_and_names.items():
        w.writerow([key, val])
