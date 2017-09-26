import string
###  initialize a few variables  ###
ok_dna = ['a','A','t','T','g','G','c','C']
sequences = {} ###   where we will store the output of the file reader loop   ###
seq = ''
header = ''
###  Import a FASTA file  ###
File_name = input("Enter the FASTA file name:  ")
###  Try to open the file, if it cannot be opened, close the program  ###
try:
    file = open(File_name)
except:
    print("file cannot be opened", File_name)
    exit()
###  Loop through the file and remove individual sequences, with keys (fasta header) and values (sequences)  ###
###  Loop also checks the validity of the dna sequence  ###
for line in file:
    if line.startswith('>'):  # 'test if the line starts with '>'. if so it is a new sequence
        header = ''
        header += line.rstrip()  # ' store the > line as a header, will be used as a key
        if header in sequences.keys():  # ' Check if header is duplicated, if it is exit
            print('File contains duplicate Titled DNA sequences! Closing the program!', '\nProblematic header: ', header)
            print('Exiting program...')
            exit()
        seq = ''  # ' if you start a new header, reset the seq to nothing
    else:
        seq = ''
        seq += line.rstrip()  # ' if the line is not a header, store it in the seq variable
    for sites in seq:  # ' Test to se seq line only contains DNA letters
        if sites not in ok_dna:
            print('File contains non-DNA (AGTC) strings! Closing the program!')
            exit()
        else:
            continue
    else:
        sequences[header] = sequences.get(header, '') + seq

duplicated_seq = {}
for key, value in sequences.items():
    duplicated_seq.setdefault(value, set()).add(key)
hold = True
while hold:
    if [key for key, values in duplicated_seq.items() if len(values) > 1] != '':
        print("There are duplicated DNA sequences")
        Hold = input('Continue with the program, Y/N?')
        if Hold == 'Y':
            hold = False
        else:
            exit()
    #print(sequences)
        ###  Reverse complement the sequence  ###
reverse_complement = {}
trans = str.maketrans('ATGCatgc', 'TACGtacg')
for key, seq_rc in sequences.items():
    reverse_complement[key] = reverse_complement.get(key, '') + seq_rc.translate(trans)[::-1]
for ID, Seq_f in reverse_complement.items():
    print(ID,'\n',Seq_f)
    GC_seq = 0
    length_seq = 0
    percent_GC = 0
    for base in Seq_f:
        if base in ['g','G','c', 'C']:
            GC_seq += 1
    percent_GC = 100 * (GC_seq/len(Seq_f))
    length_seq = len(Seq_f)
    print('Some statistics: \n', '\tGC content: ', round(percent_GC, 2),'%GC\n', '\tSequence length: ', '%d bases' % length_seq)
