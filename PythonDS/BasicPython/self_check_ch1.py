#
# Author: James Ortiz
# File: self_check_ch1.py
# Self check problem 1
#

word_list = ['cat', 'dog', 'rabbit']
letter_list = []
for a_word in word_list:
    for a_letter in a_word:
        if a_letter not in letter_list: #If the letter is not alwready in the list, append the letter.
            letter_list.append(a_letter)
print(letter_list)
