def check_agreement(subject, verb):
    # Feature structure for subjects
    subjects = {
        "he": ("singular", "third"),
        "she": ("singular", "third"),
        "it": ("singular", "third"),
        "we": ("plural", "first")
    }

    # Feature structure for verbs
    verbs = {
        "eats": "singular",
        "sleeps": "singular",
        "eat": "plural",
        "sleep": "plural"
    }

    # Check whether subject and verb exist
    if subject not in subjects or verb not in verbs:
        return False

    # Compare Number
    subject_number = subjects[subject][0]
    verb_number = verbs[verb]

    return subject_number == verb_number


# Test cases
print("he eats:", check_agreement("he", "eats"))
print("he eat:", check_agreement("he", "eat"))
print("we eat:", check_agreement("we", "eat"))
print("we sleeps:", check_agreement("we", "sleeps"))
print("she sleeps:", check_agreement("she", "sleeps"))
