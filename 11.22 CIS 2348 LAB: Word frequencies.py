# luis Marroquin
# 1975448
# CIS-2348
# 11.22 CIS 2348 LAB: Word frequencies
words = input().split()

# Create an empty dictionary to store the word frequencies
word_freq = {}

# Iterate through the list of words and update the word frequencies in the dictionary
for word in words:
    word = word.lower()
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Output the word frequencies
for word in words:
    lower_word = word.lower()
    print(word, word_freq[lower_word])