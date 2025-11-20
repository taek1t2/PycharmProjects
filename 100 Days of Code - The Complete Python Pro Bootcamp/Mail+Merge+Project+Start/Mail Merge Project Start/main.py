#TODO: Create a letter using starting_letter.txt

to_letter = open("Input/Letters/starting_letter.txt", "r")

friend_invite = []
invited = open("Input/Names/invited_names.txt", "r")

#for each name in invited_names.txt
for name in invited:
    friend_invite.append(name)

#Replace the [name] placeholder with the actual name.


#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp