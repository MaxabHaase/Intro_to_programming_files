
# Define the user rating dictionary and a empty dictionary to contain the item rating dictionary.

user_item_rating = {'user1': {'item1': 2.5, 'item2': 3.5, 'item3': 3.0, 'item4': 3.5, 'item5': 2.5, 'item6': 3.0},
                    'user2': {'item1': 3.0, 'item2': 3.5, 'item3': 1.5, 'item4': 5.0, 'item5': 3.5, 'item6': 3.0},
                    'user3': {'item1': 2.5, 'item2': 3.0, 'item4': 3.5, 'item6': 4.0},
                    'user4': {'item2': 3.5, 'item3': 3.0, 'item4': 4.0, 'item5': 2.5, 'item6': 4.5},
                    'user5': {'item1': 3.0, 'item2': 4.0, 'item3': 2.0, 'item4': 3.0, 'item5': 2.0, 'item6': 3.0},
                    'user6': {'item1': 3.0, 'item2': 4.0, 'item4': 5.0, 'item5': 3.5, 'item6': 3.0},
                    'user7': {'item2': 4.5, 'item4': 4.0, 'item5': 1.0}}
item_user_rating = {}

# Function is used to parse over the passed dictionary and calculate the Average of absolute difference in ratings
#   for common keys.
# First it creates a list of all the top-level keys
# Next, it iterates over each individual key in the top-level keys list
# Next, it iterates over a list of indices that corresponding to the index of the next key to the key of the last
#   in the list of top-level keys
# Next, it iterates over each sub - item in the passed dictionary at the given top - level key
# If the sub-key is present in the in the sub-dictionary of the next top-level key then calculate the absolute difference
#   between the rating values and add it to the total for that top - level key pair
# Lastly, after calculating the sum abs. differences for each sub-key rating it divides the summed value by the total
#   amount of sub-keys shared between the two top-level keys, then it adds the top-level key pair and the calculated
#   average of absolute difference to a dictionary.


def abs_dif_dict(dict):
    index_abs_dif_dict = {}
    list = []
    for key in dict:
        list.append(key)
    for index_ in list:
        for next_index in range(list.index(index_) + 1, len(list)):
            abs_difs = 0
            shared_items = 0
            for item, rating in dict[index_].items():
                if item in dict[list[next_index]]:
                    abs_difs += abs((rating - dict[list[next_index]][item]))
                    shared_items += 1
            ave_abs_dif = abs_difs/shared_items
            index_pair = index_ + '_' + list[next_index]
            index_abs_dif_dict[index_pair] = index_abs_dif_dict.get(index_pair, 0) + ave_abs_dif
    return index_abs_dif_dict


# function is used to calculated the minimum average of absolute difference of all the top-level key pairs
# First, it gets the largest value and uses it to find the smallest value
# After iterating over every value it will return the smallest value and its corresponding top-level key pair.


def most_similar(dict):
    for key, value in dict.items():
        if value >= value:
            value_ = value
    for key, value in dict.items():
        if value <= value_:
            value_ = value
            most_freq = key, value
    return most_freq


# Logic to create the item rating dictionary from the user rating dictionary.
# it will iterate over every user and every item that user rated and add the user and the rating to the value of the
# item, which is no a key
# Simply, it takes for the given key (user) what are the items and their corresponding ratings
# Next, it says if the item is not a key in the item rating dictionary add it as a key to a empty dictionary.
# Next, it says for the given item add the user and the rating as key : value pair to a sub - dictionary.

for user in user_item_rating:
    for item, rating in user_item_rating[user].items():
        if item not in item_user_rating:
            item_user_rating[item] = item_user_rating.get(item, {})
        item_user_rating[item][user] = item_user_rating[item].get(user, 0) + rating

# Block of statements calling the function abs_dif_dict() and then most_similar()

user_abs_dif_dict = abs_dif_dict(user_item_rating)
item_abs_dif_dict = abs_dif_dict(item_user_rating)
user_most_similar = most_similar(user_abs_dif_dict)
items_most_similar = most_similar(item_abs_dif_dict)

# Prints out a formatted sentence that states the most similar user pair and item pair.

print('The users most similar to each other are {} and {}, with a score of {}'
      .format(user_most_similar[0][:5], user_most_similar[0][6:], user_most_similar[1]))
print('The items most similar to each other are {} and {}, with a score of {}'
      .format(items_most_similar[0][:5], items_most_similar[0][6:], items_most_similar[1]))
