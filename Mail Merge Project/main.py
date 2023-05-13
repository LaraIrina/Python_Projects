#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open ("/Users/laraquitte/Library/CloudStorage/Dropbox/Python_Projects/Mail Merge Project/Input/Names/invited_names.txt") as data:
    names = data.readlines()
list_of_names = []
for name in names:
    name = name.strip("\n")
    list_of_names.append(name)

with open ("/Users/laraquitte/Library/CloudStorage/Dropbox/Python_Projects/Mail Merge Project/Input/Letters/starting_letter.txt") as letter:
    letter_base = letter.read()
    for i in range (len(list_of_names)-1): 
        letter_finished = letter_base.replace("[name]", list_of_names[i])
        with open (f"/Users/laraquitte/Library/CloudStorage/Dropbox/Python_Projects/Mail Merge Project/Output/letter_for_{list_of_names[i]}", mode="w") as letter_to_write:
            letter_individual = letter_to_write.write(letter_finished)
