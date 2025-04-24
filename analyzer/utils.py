import math
from collections import Counter

def calculate_tfidf(text):
    words = [word.lower() for word in text.split() if word.isalpha()]
    total_docs = 1  # только один документ

    tf_counter = Counter(words)
    total_words = sum(tf_counter.values())

    tfidf_list = []

    for word, count in tf_counter.items():
        tf = count
        idf = math.log((1 + total_docs) / (1 + (1 if count > 0 else 0))) + 1
        tfidf_list.append((word, tf, round(idf, 4)))

    tfidf_list.sort(key=lambda x: x[2], reverse=True)
    return tfidf_list[:50]
