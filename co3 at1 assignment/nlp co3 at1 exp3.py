def sentence_probability(sentence):
    words = sentence.lower().split()

    # PCFG probabilities
    np_prob = {
        "tom": 0.7,
        "ann": 0.3
    }

    vp_prob = {
        "sings": 0.4,
        "dances": 0.6
    }

    # Sentence must contain exactly 2 words
    if len(words) != 2:
        return 0.00

    subject = words[0]
    verb = words[1]

    # Check whether sentence can be generated
    if subject not in np_prob or verb not in vp_prob:
        return 0.00

    # S -> NP VP has probability 1.0
    probability = 1.0 * np_prob[subject] * vp_prob[verb]

    return probability


# Test cases
print("Tom sings:", sentence_probability("Tom sings"))
print("Tom dances:", sentence_probability("Tom dances"))
print("Ann sings:", sentence_probability("Ann sings"))
print("Ann dances:", sentence_probability("Ann dances"))
print("Sam sings:", sentence_probability("Sam sings"))
