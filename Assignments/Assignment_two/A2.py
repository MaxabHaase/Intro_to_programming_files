# Pseudo-code
# 1. Read the tsv file and save the contents in a nested list of rows
# 2. Using ‘map’ function, create a dictionary for each row
# 3. Filter the list of  dictionaries so that any rows with TRYP or BOVIN in the most common protein string are removed
# 4. Use a ‘reduce’ function to reduce the filtered list of dictionaries down to a single dictionary containing counts
# for each taxon grouped by year

from datetime import datetime
from functools import reduce

def get_items(string_line):
    header = ['date', 'taxon', 'mcp']
    tmp = string_line.strip().split('\t')
    tmp_ = list((tmp[1], tmp[22], tmp[6]))
    taxon = tmp_[1].strip().split(',')
    if len(taxon) > 1:
        taxon_ = []
        for taxa in taxon:
            taxon_.append(taxa.strip())
        tmp_[1] = taxon_
    if len(taxon) == 1:
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


def year_count(dict_b, dict_a):
    if dict_a['date'] not in dict_b:
        dict_b[dict_a['date']] = dict_b.get(dict_a['date'], {})
    for taxa in dict_a['taxon']:
        dict_b[dict_a['date']][taxa] = dict_b[dict_a['date']].get(taxa, 0) + 1
    return dict_b


def most_common(dict_a):
    for year, info in dict_a.items():
        previous_freq = 0
        for taxa, freq in info.items():
            if freq > previous_freq:
                previous_freq = freq
                most_freq_taxa = taxa
        print('The most common species in {} was {}, which appeared {} times'.format(year,
                                                                                     most_freq_taxa, previous_freq))

fh = open('cleaned_GPMDB_table.tsv', 'r')
print('Program is running...')
list_of_dicts = map(get_items, fh.readlines()[1:])
filtered_dictionary_list = filter(filter_, list_of_dicts)
counted_taxa = reduce(year_count, filtered_dictionary_list, {})
most_common(counted_taxa)
fh.close()


