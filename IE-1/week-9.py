import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer, word_tokenize

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')

file = open("data.txt")
data = file.read()
file.close()

words_with_punctuations = word_tokenize(data)
words_without_punctuations = RegexpTokenizer(r'\w+').tokenize(data)

print("Words with punctuations:\n", words_with_punctuations)
print("\n\nWords without punctuations:\n", words_without_punctuations)

tags = nltk.pos_tag(words_without_punctuations)
print("\n\nParts of Speech:\n", tags)

stop_words = set(stopwords.words('english'))
filtered_data = [w for w in words_without_punctuations if not w.lower() in stop_words] 
print("\n\nRemoving stop words:\n", filtered_data)
