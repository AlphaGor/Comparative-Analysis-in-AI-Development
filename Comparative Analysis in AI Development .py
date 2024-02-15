mport os
import nltk
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
from nltk import word_tokenize, FreqDist, bigrams, ngrams
from nltk.corpus import stopwords
import string

document_paths = [
    "USA.txt",
    "CHINA.txt",
    "EU.txt"
]

# Read the custom stopwords from a file
with open("stopwords_en.txt", "r") as stopwords_file:
    custom_stopwords = set(stopwords_file.read().splitlines())

nltk.download('punkt')

# Preprocess and analyze text
for document_path in document_paths:
    print(f"Analyzing {os.path.basename(document_path)}")

    # Read the text from a TXT file
    with open(document_path, 'r', encoding='utf-8') as text_file:
        txt_text = text_file.read()

    # Tokenization
    tokens = word_tokenize(txt_text)

    # Lowercasing
    tokens = [token.lower() for token in tokens]

    # Custom stopword removal and punctuation removal
    tokens = [token for token in tokens if token not in custom_stopwords and token not in string.punctuation]

    # Generate and display a word cloud
    text = " ".join(tokens)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    # Calculate and display top words
    freq_dist = FreqDist(tokens)
    print("Top Words:")
    for word, frequency in freq_dist.most_common(10):
        print(f"{word}: {frequency}")

    # Calculate and display top bigrams
    bigram = list(bigrams(tokens))
    bigram_freq = FreqDist(bigram)
    print("Top Bigrams:")
    for bigram, frequency in bigram_freq.most_common(10):
        print(f"{bigram[0]} {bigram[1]}: {frequency}")

