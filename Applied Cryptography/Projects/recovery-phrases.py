import random
import nltk
nltk.download("words")
from nltk.corpus import words

word_list = words.words()

def generate_recovery_phrase(num_words):

    if num_words % 3 != 0:
        raise ValueError("Number of words in the recovery phrase must be a multiple of 3.")

    recovery_phrase = []
    for word in range(num_words):
        word_index = random.randint(0, len(word_list) - 1)
        recovery_phrase.append(word_list[word_index])

    return " ".join(recovery_phrase)

def check_recovery_phrase(input_phrase, generated_phrase):
    return input_phrase.strip() == generated_phrase.strip()

if __name__ == "__main__":

    num_words = 9 
    generated_phrase = generate_recovery_phrase(num_words)
    print()
    print("--------------------------")
    print("| Recovery Phrase System |")
    print("--------------------------")
    print("Your Recovery Phrases: ", generated_phrase)

    input_phrase = input("Enter Recovery Phrases: ")
    print()

    if check_recovery_phrase(input_phrase, generated_phrase):
        print("Correct recovery phrases. Access granted.")
        print()
    else:
        print("Incorrect recovery phrases. Access denied.")
        print()
