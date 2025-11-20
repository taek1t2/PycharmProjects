#TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt", "r") as letter:
    letter_contents = letter.read()

friend_invite = []
with open("Input/Names/invited_names.txt", "r") as friends_name:
    names = friends_name.readlines()
    print(names)

#for each name in invited_names.txt
for name in names:
    friend_invite.append(name)


#Replace the [name] placeholder with the actual name.


#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp