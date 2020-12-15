import random
from os import listdir
from os.path import isfile, join


substitute_words = {"are":"we", "and":"or", "never":"always", "because":"why"}
words_to_replace = list(substitute_words.keys())

directory = r'C:\Users\karol\Desktop\Python_zajecia\text_files\computer'

print('Reading files from directory... ' + directory)

files_from_directory = [f for f in listdir(directory) if isfile(join(directory, f))]


seed_number = random.randint(0, (len(files_from_directory)-5))

for i in range(seed_number, seed_number+4):
    print('Reading file: ' + files_from_directory[i])
    mod_files_from_directory = 'modified_replaced_' + files_from_directory[i]
    with open(directory + '\\' + files_from_directory[i]) as in_file, open(directory + '\\' + mod_files_from_directory, "w+") as out_file:
        for line in in_file:
            if line != "\n":
                for word in words_to_replace:
                    line = line.replace(word, substitute_words[word])
            out_file.write(line)
    print('Save modifies file as: ' + mod_files_from_directory)