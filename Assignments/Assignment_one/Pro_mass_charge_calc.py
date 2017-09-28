
########################################################################################################################
########################################################################################################################
########################################################################################################################
###  Initialize various variables, list, dicts, etc.

#  Variables
pro_temp = ''
bad_letter = 0

#  List
sequence = []
good_seq = []
bad_seq = []
invalid_chr = []

#  Dictionaries
Amino_acid_dict = {'A': 71.03711360,
'C': 103.0091854,
'D': 115.0269428,
'E': 129.0425928,
'F': 147.0684136,
'G': 57.02146360,
'H': 137.0589116,
'I': 113.0840636,
'K': 128.0949626,
'L': 113.0840636,
'M': 131.0404854,
'N': 114.0429272,
'P': 97.05276360,
'Q': 128.0585772,
'R': 156.1011106,
'S': 87.03202820,
'T': 101.0476782,
'V': 99.06841360,
'W': 186.0793126,
'Y': 163.0633282,
'h2o': 18.010564684}
bad_dict = {}
list_of_protein_dicts = [{'seq': 'ACACIMED', 'ch': 2},
                         {'seq': 'ELEMYRATNE', 'ch': 1},
                         {'seq': 'wapwop', 'ch': 3},
                         {'seq': 'zeittsieg', 'ch': 2},
                         {'seq': 'DESFBIRC', 'ch': 1},
                         {'seq': 'altaatsiv', 'ch': 3},
                         {'seq': 'MEINWOHC', 'ch': 2}]
mass_charge = {}

#  booleans
hold = True
########################################################################################################################
# STEP 4.
# This function first calculates the total masses for each "verified" protein sequence and stores it in a dictionary as
# value and sequence as the key. Next, it pulls the charge for each protein sequence form the dictionary
# list_of_protein_dicts and stores only the charges of the verified sequences in a dictionary. Lastly, it takes the two
# newly created dictionaries (Mass and charges) and divides the two, then it returns a dictionary of the mass/charge
# ratio as the value and the protein sequence as the key. This function is called later in the program.

def Mass_charge_calc(good_seq):
    masses = {}                         # 'Set dictionary to store Protein:masses
    charges = {}                        # 'Set dictionary to store Protein:charges
    for protein in good_seq:            # 'For loop, pulls only valid protein sequences and mass into dict masses.
        mass = 0
        AA_len = ''
        for AA in protein:
            mass += Amino_acid_dict[AA]
            AA_len += AA
            if len(AA_len) == len(protein):     # 'Indicated I have read one sequence in full, now add water to mass.
                mass += Amino_acid_dict['h2o']
                masses[protein] = masses.get(protein, '') + str(mass)   # 'Add sequence (key) and mass (value) to dict.
    for value in list_of_protein_dicts:         # 'go through each item in the dict list_of_protein_dicts.
        value_ = list(value.values())[0].upper()    # 'Get all the sequences from the items (the value of the 1st key).
        if value_ in good_seq:              # 'If the sequence is in good_seq (valid), then get the charge value.
            charges[list(value.values())[0].upper()] = charges.get(list(value.values())[0].upper(), 0) + \
                                                       float(list(value.values())[1])
    for protein_a, mass_ in masses.items(): # 'Get key and value from masses dictionary
        for protein_b, charge_ in charges.items():  # 'Get key and value from charges dict
            if protein_a == protein_b:      # 'If the sequences match then calculate the mass/charge, into a dict.
                mass_charge[protein_a] = mass_charge.get(protein_a, 0) + float(mass)/float(charge_)
    return mass_charge                      # 'Send the dictionary back out.

########################################################################################################################
# STEP 1. This for loop is used to get the protein sequences out of the defined dictionary: list_of_protein_dicts.

for value in list_of_protein_dicts: # 'Get the keys and values
    prin = 1            # I use this to count, thus I only pull out every other key, which is the protein sequence.
    for protein in value.values():  # 'Loop, get the values (sequence and charge).
        if prin % 2 != 0:           # if "prin" is not even, then pull out that value
            sequence.append(protein.upper())  # 'Put the protein sequence into a list, and uppercase it.
            prin += 1               # 'Count up one.
        else:
            prin += 1

########################################################################################################################
# STEP 2. This loop checks the validity of the sequences and put good and bad sequences into two separate lists.

for protein_calc in sequence:           # 'Get the sequences in the list.
    for AA in protein_calc:             # 'Read through each sequence one amino acid at a time.
        pro_temp += AA                  # 'Store the amino acid in a temporary string.
        if AA not in Amino_acid_dict:   # 'If the the amino acid is not one of the 20, then execute the block
            bad_letter += 1                 # 'If the amino acid was bad, give the sequence a "score"
            invalid_chr += AA               # 'Keep track of the amino acid that was wrong, for the sequence.
        if len(pro_temp) == len(protein_calc):  # 'Once it has read the entire sequence, execute the block.
            if bad_letter >= 1:         # 'If the sequence had a bad character, store it in a list of bad sequences.
                bad_letter = 0          # 'Reset the counter value.
                bad_seq.append(pro_temp)    # 'Store the sequence in the list "bad_seq"
                bad_dict[pro_temp] = bad_dict.get(pro_temp, '') + str(invalid_chr)  # add the sequence and invalid AA
                invalid_chr = []        # Reset the list
                pro_temp = ''           # Reset the temporary string
            else:
                good_seq.append(pro_temp)   # 'If the sequence is good, add it the list "good_seq"
                pro_temp = ''               # 'Reset the variables
                bad_letter = 0

########################################################################################################################
# STEP 3. This while loop either goes ahead and executes the mass/charge calculation or notices if there are bad
# sequences and prompts the user if the would like to still continue.
ask = 0
while hold:
    if bad_seq != []:
        if ask == 0:
            print('Looks like there are some invalid sequences:')
            for key, value in bad_dict.items():
                print('\tSequence: {} Amino Acid: {}'.format(str(key), str(value)))
        usr = input('\nWould you like to continue and calculate only the valid sequences, Y/N? ')
        if usr not in 'YyNn':
            ask += 1
            pass
        elif usr in 'Yy':
            Mass_charge_calc(good_seq)
            hold = False
        elif usr in 'Nn':
            hold = False
            exit()
    else:
        Mass_charge_calc(good_seq)
        hold = False
########################################################################################################################
# STEP 5. Print the results.
print('\nHere are the protein mass - charge ratios\n')
for protein, mass_charge in mass_charge.items():
    print('\tProtein: {}, mass/charge: {}'.format(protein, round(mass_charge, 5)))



