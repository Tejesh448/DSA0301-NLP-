def parse_cfg(sentence):
    words = sentence.lower().split()

    # Grammar validation
    if len(words) != 5:
        return "Invalid Sentence"

    det = ["the", "a"]
    nouns = ["dog", "cat", "bone"]
    verbs = ["chased", "found"]

    # Check grammar: S -> NP VP
    # NP -> Det N
    # VP -> V NP

    if (words[0] in det and
        words[1] in nouns and
        words[2] in verbs and
        words[3] in det and
        words[4] in nouns):

        # Parse tree
        tree = f"""
S
├── NP
│   ├── Det → {words[0]}
│   └── N → {words[1]}
└── VP
    ├── V → {words[2]}
    └── NP
        ├── Det → {words[3]}
        └── N → {words[4]}
"""

        return tree

    return "Invalid Sentence"


# Test cases
sentences = [
    "the dog chased a cat",
    "a cat found the bone",
    "dog chased cat",
    "the bone found a dog",
    "chased the dog bone"
]

for sentence in sentences:
    print("Sentence:", sentence)
    print(parse_cfg(sentence))
    print("-" * 40)
