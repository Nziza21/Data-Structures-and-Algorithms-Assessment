import string

def word_frequency(sentence):

# Remove punctuation and convert to lowercase
translator = str.maketrans("", "", string.punctuation)
sentence = sentence.translate(translator).lower()

# Split the sentence into words
words = sentence.split()

# Create a dictionary to store word frequencies
frequency_dict = {}

# Count the frequency of each word
for word in words:
    frequency_dict[word] = frequency_dict.get(word, 0) + 1

return frequency_dict
