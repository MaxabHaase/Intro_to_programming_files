from functools import reduce
dict_test = [{'date': '2004', 'taxon': ['human'], 'mcp': 'ENSP00000319713'}, {'date': '2004', 'taxon': ['human'], 'mcp': 'ENSP00000319713'}]


def year_count(dict_b, dict_a):
    # check if date in dict
    # if not make empty dict for that date
    # for each taxa if it is in dict for the date increment + 1, else add
    if dict_a['date'] not in dict_b:
        dict_b[dict_a['date']] = dict_b.get(dict_a['date'], {})
    for taxa in dict_a['taxon']:
        dict_b[dict_a['date']][taxa] = dict_b[dict_a['date']].get(taxa, 0) + 1
    return dict_b

reduced_dict = reduce(year_count, dict_test, {})
print(reduced_dict)

