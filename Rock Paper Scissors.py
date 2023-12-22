def start():
    print("This is my Elephant Mouse Cat Game!")
    Player_One = "Mary"
    Player_Two = "Lynn"

    def choices(Player_One_Choice, Player_Two_Choice):
        if Player_One_Choice == "Elephant" and Player_Two_Choice == "Mouse":
            return("Mouse covers Elephant! " + Player_Two + " wins!")
        elif Player_One_Choice == "Mouse" and Player_Two_Choice == "Elephant":
            return("Mouse covers Elephant! " + Player_One + " wins!") 
        elif Player_One_Choice == "Cat" and Player_Two_Choice == "Mouse":
            return("Cat cuts Mouse! " + Player_One + " wins!")
        elif Player_Two_Choice == "Cat" and Player_One_Choice == "Mouse":
            return("Cat cuts Mouse! " + Player_Two + " wins!")
        elif Player_One_Choice == "Cat" and Player_Two_Choice == "Elephant":
            return("Elephant smashes Cat! " + Player_One + " wins!")
        elif Player_Two_Choice == "Cat" and Player_One_Choice == "Elephant":
            return("Elephant smashes Cat! " + Player_Two + " wins!")
        elif Player_One_Choice == Player_Two_Choice:
            return(" Mary and Lynn tied!")
        else:
            return("Please type Elephant, Mouse or Cat!")
    Player_One_Choice = input("Does " + Player_One + " chose Elephant, Mouse, or Cat? ").lower()
    Player_Two_Choice = input("Does " + Player_Two + " chose Elephant, Mouse, or Cat? ").lower()

    print(choices(Player_One_Choice, Player_Two_Choice))


    def Play_Again():
        Again = input("World you like to play the game again?").lower()
        if Again == "No".lower():
            quit()
        if Again == "Yes".lower():
            start()
        else:
            print("Please enter Yes or No. Thank you!")
            Play_Again()
    Play_Again()
start()