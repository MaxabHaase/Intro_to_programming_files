# Pseudo-code
# 1. Read the tsv file and save the contents in a nested list of rows
# 2. Using ‘map’ function, create a dictionary for each row
# 3. Filter the list of  dictionaries so that any rows with TRYP or BOVIN in the most common protein string are removed
# 4. Use a ‘reduce’ function to reduce the filtered list of dictionaries down to a single dictionary containing counts
# for each taxon grouped by year

from datetime import datetime
from functools import reduce
from collections import defaultdict

def get_items(string_line):
    header = ['date', 'taxon', 'mcp']
    tmp = string_line.strip().split('\t')
    tmp_ = list((tmp[1], tmp[22], tmp[6]))
    taxon = tmp_[1].strip().split(',')
    if len(taxon) > 1:
        tmp_[1] = taxon
    tmp_ = list(tmp_)
    date = str(datetime.strptime(tmp_[0], '%Y:%m:%d:%H:%M:%S'))[:4]
    tmp_[0] = date
    dictionary = dict(zip(header, tmp_))
    return dictionary


def filter_(dictionary):
    if 'BOVIN' in dictionary['mcp']:
        return
    elif 'TRYP' in dictionary['mcp']:
        return
    else:
        return dictionary


def year_count(empty, dictionary):
    # check if date in dict
    # if not make empty dict for that date
    # for each taxa if it is in dict for the date increment + 1, else add
    
    return empty


fh = open('cleaned_GPMDB_table_test.tsv', 'r')
list_of_dicts = map(get_items, fh.readlines()[1:])
filtered_dictionary_list = filter(filter_, list_of_dicts)
print(list(filtered_dictionary_list))
reduced_dict = reduce(year_count, filtered_dictionary_list, {})
print(reduced_dict)
