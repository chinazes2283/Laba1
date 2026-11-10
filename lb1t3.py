text = """
Hello World! Test text
Test text to check the program's operation
"""

import string

clean_text = text.lower()
for p in string.punctuation + "«»—…\n":
    clean_text = clean_text.replace(p, " ")

words = clean_text.split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print("Повний словник частот (несортований):")
print(word_counts)

print("\nСортування за ключем (алфавітом):")
for k in sorted(word_counts.keys()):
    print(f"{k}: {word_counts[k]}")

print("\nСортування за спаданням частоти:")
sorted_by_freq = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
for k, v in sorted_by_freq:
    print(f"{k}: {v}")

threshold = 2
frequent_words = {k: v for k, v in word_counts.items() if v >= threshold}

print(f"\nПохідний словник (слова з частотою не менше {threshold}):")
print(frequent_words)
