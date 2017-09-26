#  This is a program that will take a input DNA sequence and output the reverse compliment for you.
#  It will either accept a .fasta file or allows you to enter each sequence manually.
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################

#  Initialize variables used in the program

file_in = True
hold = True
duplicated_seq = {}
reverse_complement = {}
sequences = {}                                  # where we will store the output of the file reader loop
header = ''
seq = ''
ok_dna = ['a','A','t','T','g','G','c','C']      # Strings acceptable as a input
trans = str.maketrans('ATGCatgc', 'TACGtacg')   # The translation table between forward and reverse compliment strand.

########################################################################################################

# Define a function for parsing a .fasta file and extracting the DNA sequence. Test if sequence has acceptable -
# characters and checks to make sure no duplicated sequence headers are in the file.
# Sequences are pulled from the file one line at a time.

def fasta_file(file):
    for line in file:                       # Iterate through all lines of the fasta file and get headers and sequences
        if line.startswith('>'):            # This tests if the line starts with '>'. If so it is a new sequence.
            header = ''
            header += line.rstrip()         # Store the > line as a header, will be used as a key
            if header in sequences.keys():  # Check if header is duplicated, if it is exit
                print('File contains a duplicate header! Closing the program!', '\nProblematic header: ', header)
                print('Exiting program...')
                exit()
            seq = ''                        # If you start a new header, reset the stored seq to a empty value
        else:                               # If the line is not a header, store it in the seq variable
            seq = ''
            seq += line.rstrip()
        for sites in seq:                   # Test to see seq line only contains acceptable DNA letters
            if sites not in ok_dna:
                print('File contains non-DNA (AGTC) strings! Closing the program!')
                exit()
            else:
                continue
        else:                               # If all checks are good, add the header to the key and the seq to the value
            sequences[header] = sequences.get(header, '') + seq
    return sequences

########################################################################################################

# Define a function to take 'n' number of sequence entries from the user.

def manual_entry():
    number_seq = int(input('Enter the number of sequences you want to reverse complement: '))  # How many sequences
    key_me = 0                                      # Set a Key value for sequences to 0
    for seq_count in range(1, number_seq + 1):      # Set number of iterations to go through, how many seq. to ask for
        key_me += 1                                 # Adds +1 to the Key value for each new sequence.
        sequence_n = input('Paste in sequence %d: ' % key_me)
        for sites in sequence_n:                    # Test to se seq line only contains DNA letters
            if sites not in ok_dna:                 # Checks if sequences has only acceptable characters
                print('Sequence %d contains non-DNA (AGTC) strings! Closing the program!' % key_me)
                exit()
        sequences[key_me] = sequences.get(key_me, '') + sequence_n  # Append the Key and sequence to the dictionary
    return sequences

########################################################################################################

# While loop runs to prompt the user to decide if they would like to enter the sequence manually or type in the name of
# the fasta file. Once they decide the loop ends by either calling the manual_entry function or calling the fasta_file
# function. If the latter is chosen, it then will check to make sure the file exist in the working directory. If it is
# not present then the program exits. If it is present we call the fasta_file function and parse out the sequences.

while file_in:
    usr = input('Would you like to enter your sequences manually, Y/N? ')
    if usr == 'Y':
        manual_entry()
        file_in = False
    else:
        File_name = input("Enter the FASTA file name:  ")
        try:
            file = open(File_name)
            file_in = False
        except:
            print("file cannot be opened", File_name)
            exit()
        sequences = fasta_file(file)

########################################################################################################

# This for loop checks if any sequences (values) in the sequence dictionary are duplicated. If they are duplicated then
# it prompts the user is they'd like to continue.
for key, value in sequences.items():            # Get the Key and value for each item in the dictionary
    if value not in duplicated_seq:             # if the value is not in the duplicated_seq dictionary then go ahead.
        duplicated_seq.setdefault(value, set()).add(key) # swap the value to be the key and the key to be the value
    else:                                       # If the value is present in the duplicated_seq dict, then prompt user
        while hold:                             # Holds the program until the user decides to exit or continue
            print("There are duplicated DNA sequences, Sequence:%s," % key)
            Hold = input('Continue with the program, Y/N? ')
            if Hold == 'Y':
                hold = False
            else:
                exit()
        ###  Reverse complement the sequence  ###

########################################################################################################

# Lastly, the program takes the sequence and reverse complements it. Simply it takes the value of the sequence dict.
# and "translates" it using of translation table and then reverses the sequence by using the slicing notation.
# Then it adds the reversed complemented sequence to a value of the new dictionary with the original header.

for key, seq_rc in sequences.items():
    reverse_complement[key] = reverse_complement.get(key, '') + seq_rc.translate(trans)[::-1]

########################################################################################################

# The last step is to print out the results of the reverse complement for loop. It simply prints the header and then
# the value. Next it calculates the %GC content and the length of each sequence.
for ID, Seq_f in reverse_complement.items():
    print('\n>', ID, '\n', Seq_f)
    GC_seq = 0
    length_seq = 0
    percent_GC = 0
    for base in Seq_f:
        if base in ['g','G','c', 'C']:
            GC_seq += 1
    percent_GC = 100 * (GC_seq/len(Seq_f))
    length_seq = len(Seq_f)
    print('Some statistics: \n', '\tGC content: ', round(percent_GC, 2),'%GC\n', '\tSequence length: ', '%d bases'
          % length_seq)
