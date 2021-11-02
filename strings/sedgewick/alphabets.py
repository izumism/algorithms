ALPH2INDEX = {chr(ord('a')+i): i for i in range(26)}


def alph2ids(alphabets):
    return [ALPH2INDEX[alph] for alph in alphabets]


INDEX2ALPH = {i: ch for ch, i in ALPH2INDEX.items()}


def ids2alph(ids):
    return ''.join(INDEX2ALPH[i] for i in ids)
