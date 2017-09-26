import string

File_name = input("Enter the file name:  ")
try:
    file = open(File_name)
except:
    print("file cannot be opened", File_name)
    exit()
print(file)
Word_counts = {}
for line in file:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        Word_counts[word] = Word_counts.get(word, 0) + 1
lst = list(Word_counts.keys())
lst.sort()
for key in lst:
    print(key, Word_counts[key])
