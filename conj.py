from mlconjug3 import Conjugator
from difflib import SequenceMatcher, Differ, ndiff
import difflib as dl
from pprint import pprint
import sys
import random
import json

# constants
# difficulty = "normal"
# irregular_verb_probability = 0.4
# regular_verb_probability = 0.6
studying=True

correct=0
wrong=0

congratulations = [
    "Dix points pour Griffondor! 🧙",
    "Vous êtes quoi, un natif? 👀",
    "+1 😌",
    "+1 ✔️",
    "+1 🔥",
]

mistakes = [
    "Noup",
    "Noo",
]

# pprint(result)
# https://towardsdatascience.com/find-the-difference-in-python-68bbd000e513
# https://docs.python.org/3/library/difflib.html#difflib.Differ


def check_input(input: str) -> float:
    print('TODO NOT YET IMPLEMENTED')
    return

def choose_tense() -> [str, str, str]:
    """
        chooses a
    """
    return ["Indicatif", "Présent", "je"]

def choose_next_verb() -> str:
    return random.choice(irregular_verbs)

def congratulate():
    print(random.choice(congratulations))

def mistake():
    print(random.choice(mistakes))

def hello():
    print('Bienvenue dans conjugue-moi! 🇫🇷')

if __name__ == "__main__":
    with open('irregular_verbs.json', 'r', encoding='utf-8') as file:
        irregular_verbs = json.load(file)
        # regular_verbs = ["manger", "parler"] # TODO
    
    hello()
    
    conjugator = Conjugator(language='fr')

    while(studying):
        # TODO choose a verb
        chosen_verb = choose_next_verb()
        print(chosen_verb)
        verb = conjugator.conjugate(chosen_verb)

        # Choose tense
        chosen_tense = choose_tense()

        user_input=""
        while not user_input:
            user_input = input(f"{chosen_tense} : ")
            
        correct_verb = verb[chosen_tense]

        if user_input == correct_verb:
            congratulate()
            correct = correct + 1
        elif not user_input:
            print('this doesnt exist')
        else:
            mistake()
            wrong = wrong + 1

            text1 = list()
            text2 = list()
            
            text1.append(correct_verb)
            text2.append(user_input)

            differ = dl.Differ()
            result = list(differ.compare(text1, text2))

            for line in result:
                lines = line.split('\n')
                for i, l in enumerate(lines):
                    sys.stdout.write(l)
                    if i < len(lines) - 1:
                        sys.stdout.write('\n')
                sys.stdout.write('\n')  # Add a new line after each comparison