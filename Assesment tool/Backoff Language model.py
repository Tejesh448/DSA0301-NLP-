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
bigrams = []

for s in corpus:
    t = s.split()
    words.extend(t)

    for i in range(len(t)-1):
        bigrams.append((t[i], t[i+1]))

uni = Counter(words)
bi = Counter(bigrams)

total = len(words)

w1 = input("First word: ")
w2 = input("Second word: ")

if (w1,w2) in bi:
    prob = bi[(w1,w2)] / uni[w1]
    print("Bigram Probability =", prob)
else:
    prob = uni[w2] / total
    print("Backoff Unigram Probability =", prob)
