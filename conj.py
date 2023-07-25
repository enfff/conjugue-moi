from mlconjug3 import Conjugator
from difflib import SequenceMatcher, Differ, ndiff
import difflib as dl
from pprint import pprint
import sys

difficulty = "normal"
irregular_verb_probability = 0.4
regular_verb_probability = 0.6

##
# mlconjug3 -l fr -s pronoun 'aimer' 'être' 'aller'

# initialize the conjugator

# print all the conjugated forms as a list of tuples.
# print(verb.iterate())

# print(verb["Indicatif"]["Présent"])
# check if the form "je parle" is in the conjugated forms. Prints True.
# print("je suis" in verb)

# print(verb.conjug_info["Indicatif","Présent","1s"])
# print(verb["Indicatif", "Présent", "je"])

# pprint(result)
# https://towardsdatascience.com/find-the-difference-in-python-68bbd000e513
# https://docs.python.org/3/library/difflib.html#difflib.Differ


def check_input(input: str) -> float:
    return

def choose_next_verb() -> str:
    # TODO
    return 'être'

if __name__ == "__main__":
    conjugator = Conjugator(language='fr')

    irregular_verbs = ["être", "avoir", "aller"]
    regular_verbs = ["manger", "parler"]

    # TODO choose a verb
    chosen_verb = choose_next_verb()

    verb = conjugator.conjugate(chosen_verb)

    text1 = list()
    text2 = list()

    text1.append(verb["Indicatif", "Présent", "je"])
    text2.append(input('Indicatif Présent, 1s: '))

    differ = dl.Differ()
    result = list(differ.compare(text1, text2))

    for line in result:
        lines = line.split('\n')
        for i, l in enumerate(lines):
            sys.stdout.write(l)
            if i < len(lines) - 1:
                sys.stdout.write('\n')
        sys.stdout.write('\n')  # Add a new line after each comparison