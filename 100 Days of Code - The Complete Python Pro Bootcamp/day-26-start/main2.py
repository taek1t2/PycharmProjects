#Nato Alphabet Project
names = ["Ann", "Nara", "Suro", "Diana", "Hyesook", "Taeyeon"]

#TODO 1. create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
with open("nato_phonetic_alphabet.csv") as n:
    split_word_letter = n.split()
    nato_list = {letter:nato for (letter, nato) in n}
    print(nato_list)

#TODO Create a list of the phonetic code words from a word that the user inputs.
#enter a word: "Tae", ["Thomas", "Alpha", "Echo"]
