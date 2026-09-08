from nltk.util import ngrams
from nltk.tokenize import word_tokenize

text = "I love natural language processing"

words = word_tokenize(text)

# Bigram
bigrams = list(ngrams(words, 2))

# Trigram
trigrams = list(ngrams(words, 3))

print("Bigrams:")
print(bigrams)

print("\nTrigrams:")
print(trigrams)
