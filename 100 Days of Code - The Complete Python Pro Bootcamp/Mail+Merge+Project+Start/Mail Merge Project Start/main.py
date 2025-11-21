#TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", "r") as friends_name:
    names = friends_name.readlines()

#for each name in invited_names.txt
with open("Input/Letters/starting_letter.txt", "r") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter_for_each = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as complete_letter:
            complete_letter.write(new_letter_for_each)



#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp