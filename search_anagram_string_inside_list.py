# Question ----> search anagram of string inside list


a= ['eat', 'tea', 'ate', 'bat', 'atb', 'nat', 'tan']
# # output = [ ['eat','tea','ate'],['bat','atb'],['nat','nat'] ]

blank_dict = {}
for i in a:
    # c = ''.join(sorted(i))
    c = sorted(i)
    c = ''.join(c)
    if c not in blank_dict:
        blank_dict[c] = [i]
    else:
        blank_dict[c].append(i)

# print(blank_dict)
blank_list = []
for element in blank_dict:
    blank_list.append(blank_dict[element])

print(blank_list)




# from collections import defaultdict
# # check kar
# def group_anagrams(words):
#     grouped = defaultdict(list)
#     for word in words:
#         # Sort the word to create a key
#         sorted_word = ''.join(sorted(word))
#         # Add the original word to the list corresponding to the sorted key
#         grouped[sorted_word].append(word)
#     # Convert the result to a list of lists
#     return list(grouped.values())
# words = ['eat', 'tea', 'ate', 'bat', 'atb', 'nat', 'tan']
# print(group_anagrams(words))



