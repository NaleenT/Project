def start():
    people_dictionary = {"Brett":['Male', "Weight 175"], "Nancy" : ["Female","Weight 125"], "Patrick" : ["Male","Weight 195"], "Briar" : ["Male","Weight 115"], "Adam" : ["Male","Weight 215"]}
    print(people_dictionary)

    Name = input ("Please type in a name: ")
    print("You typed in the name " + Name.capitalize())

    try:
        Persons_data = people_dictionary[Name]
        print("Name: " + Name.capitalize())
        print(Persons_data[0])
        print("Weight: " + Persons_data[1])
        more()
    except:
        print("That name, (as written) was not found in the dictionary.")
        more()



def more():
    More = input("Would you like to search for another name?")
    if More == "No":
        quit()
    if More == "Yes":
        start()
    else:
        print("Please enter Yes or No.")
        more()
start()
