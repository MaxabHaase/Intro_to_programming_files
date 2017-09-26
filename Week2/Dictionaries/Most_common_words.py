import string
        ####  Import File ####
File_name = input("Enter the file name:  ")
try:
    file = open(File_name)
except:
    print("file cannot be opened", File_name)
    exit()
        ####  Count the words  ####
counts = dict()
for line in file:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        #### Sort by the dictionary value  ####
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst[:20]:
    print(key, val)