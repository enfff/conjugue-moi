from mlconjug3 import Conjugator
from difflib import SequenceMatcher, Differ, ndiff
import difflib as dl
from pprint import pprint
import sys
import random
import json
import constants_module as cm

# constants
# difficulty = "normal"
# irregular_verb_probability = 0.4
# regular_verb_probability = 0.6
studying = True
cheats = False # change this to 'True' to get the expected answer
correct = 0
wrong = 0

# load everything
moods_and_tenses = cm.moods_and_tenses
irregular_verbs = cm.irregular_verbs
msg_congratulations = cm.congratulations
msg_mistakes = cm.mistakes
msg_verb_doesnt_exist = cm.verb_doesnt_exist


def choose_tense() -> [str, str, str]:
    """
    Will return something like these
    ['Conditionnel', 'Présent', 'je']
    ['Conditionnel', 'Présent', 'vous']
    ['Subjonctif', 'Présent', 'que je']
    ['Conditionnel', 'Présent', 'tu']
    ['Conditionnel', 'Présent', 'nous']
    ['Subjonctif', 'Présent', 'que tu']
    ['Subjonctif', 'Imparfait', "qu'il (elle, on)"]
    ['Participe', 'Passé', 'masculin pluriel']
    ['Impératif', 'Présent']
    """

    chosen_tense = []
    mood, tense = random.choice(list(moods_and_tenses.items()))
    # mood is always a string
    # tense is always a dict
    chosen_tense.append(mood)

    if type(tense) == dict:
        key, val = random.choice(list(tense.items()))
        chosen_tense.append(key)
        if val:
            person = random.choice(val)
            chosen_tense.append(person)

        # Avoids a bug
        if key == 'Imperatif Présent':
            chosen_tense.append('')

    # print(chosen_tense)
    return chosen_tense


def choose_next_verb() -> str:
    return random.choice(irregular_verbs)


def congratulate():
    print(random.choice(msg_congratulations))


def mistake():
    print(random.choice(msg_mistakes))


def doesnt_exist():
    print(random.choice(msg_verb_doesnt_exist))


def hello():
    print('Bienvenue dans conjugue-moi! 🇫🇷')
    if cheats:
        print('🔥🔥🔥CHEATS ON!🔥🔥🔥')


if __name__ == "__main__":
    # __init__()
    hello()

    conjugator = Conjugator(language='fr')

    while (studying):
        # TODO choose a verb
        chosen_verb = choose_next_verb()
        print('next verb: ', chosen_verb)
        verb = conjugator.conjugate(chosen_verb)

        # Choose tense
        chosen_tense = choose_tense()
        print('next tense: ', chosen_tense)

        correct_verb = verb[chosen_tense]
        # if u wanna cheat
        if cheats:
            print('expected answer: ', correct_verb)

        user_input = ""

        while (not user_input) or (user_input == "help"):
            user_input = input(f"{chosen_tense} : ")

            if user_input == "help":
                # it works but it looks ugly
                print(conjugator.conjugate(chosen_verb).iterate())

        if user_input == correct_verb:
            congratulate()
            correct = correct + 1
        elif not correct_verb:
            print('not well implemented, but you didnt get any bad point !!!!')
            doesnt_exist()
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
