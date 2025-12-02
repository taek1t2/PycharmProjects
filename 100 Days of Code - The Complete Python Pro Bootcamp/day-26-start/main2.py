#Nato Alphabet Project
names = ["Ann", "Nara", "Suro", "Diana", "Hyesook", "Taeyeon"]
import pandas as pd

#TODO 1. create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_list = pd.DataFrame(df)
nato_dict = {row.letter:row.code for (_, row) in nato_list.iterrows()}
print(nato_dict)

#TODO Create a list of the phonetic code words from a word that the user inputs.
#enter a word: "Tae", ["Thomas", "Alpha", "Echo"]
