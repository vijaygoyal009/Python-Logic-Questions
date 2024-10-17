# Question ---->  This the word count like (l is 2 , l=2)


# input_str  = 'Hello'
# ans = 0
# search = 'o'

# for char in input_str:
#     if char == search:
#         ans = ans + 1

# print(f" {search} :- {ans}")


def word_count(input_string , search_word):
    ans = 0
    for char in input_string:
        if char == search_word:
            ans += 1
    return ans

input_string = "hello"
serach_word = 'l'
print(word_count(input_string,serach_word))
