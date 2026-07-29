from collections import Counter

corpus = [
    "I love NLP",
    "I love Python",
    "I study NLP",
    "We study Python",
    "You love NLP",
    "I study Python"
]

words = []

for s in corpus:
    words.extend(s.split())

freq = Counter(words)

V = len(freq)
N = len(words)

word = input("Enter word: ")

mle = freq[word] / N

laplace = (freq[word] + 1) / (N + V)

print("MLE Probability =", mle)
print("Laplace Probability =", laplace)
