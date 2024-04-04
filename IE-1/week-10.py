from nltk.tokenize import word_tokenize, sent_tokenize, blankline_tokenize
from collections import Counter

file = open("data.txt")
text = file.read()
file.close()

word_tokens = word_tokenize(text)
print("Word Tokens:\n")
print(word_tokens)

sent_tokens = sent_tokenize(text)
print("\nSentence Tokens:\n")
print(sent_tokens)

# paragraphs = text.split('\n')
# print("\nParagraph Tokens:\n")
# print(paragraphs)

paragraphs = blankline_tokenize(text)
print("\nParagraph Tokens:\n")
print(paragraphs)

total_words = len(word_tokens)
print(f"\nTotal number of words: {total_words}")

distinct_words = len(set(word_tokens))
print(f"Total number of distinct words: {distinct_words}")

word_counts = Counter(word_tokens)
print("\nWord Counts:\n")
for word, count in word_counts.items():
    print(f"{word}: {count}")
