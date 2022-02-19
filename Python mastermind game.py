import random

colour_list = ["red", "blue", "green", "yellow"]
#random colour list with 4 variable
colour_list = random.choices(colour_list, k=4)



# to conduct a new list
def newList(list):
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i])

    return new_list

def instruction():
    print("----------------------------------------MasterMindGame----------------------------------------\n")
    print("\t\t\t\t\t---Game Rule---")
    print("\n\t\t1) Pls choose the colour red , green , blue , yellow as answer.")
    print("\n\t\t2) Input answer should be in lower case")
    print("\n\t\t3) Make sure that have spacing in between the answer")
    print("\n\t\t4) Colour may be repeated")
    print("\n\t\t\t*For example: green blue red yellow\n")
    print("---------------------------------Its your turn now! Good Luck ---------------------------------")

def errorinstruction():
    print("\n------------------------------------------<EROR 404>------------------------------------------\n")
    print("\n\t\t" + str(userInput) + " is Eror Input pls input according to the instruction below")
    print("\n\t\t1) Pls input according to the instruction")
    print("\n\t\t2) In lowercase & spacing in between")
    print("\n\t\t3) Make sure only accept this 4 colour as input [red, green, yellow, blue]")
    print("\n\t\t\t*Example: green blue red yellow")

def wingame():
    print("\n---------------------------------------Congratulations---------------------------------------\n")
    print("\n\t\t\t\tCongratulations! You Win The Game")
    print("\n\t\t\tWith Attempt of: ", str(attempt))
    print("\n\t\t\t*Fire cracking sound ^_^ ")
    print("\n\t\t\tThank You for playing Master Mind Game ＼（Ｔ∇Ｔ ）／")

instruction()
corColcorPlace = 0 
corColwrongPlace = 0
attempt = 0

#loop eliminate when correct colour place is == 4
while (corColcorPlace < 4):
    #conduct a new list base on colour list
    temp_colour_list = newList(colour_list)
    Error = False
    #user input
    userInput = input ("\nPls enter your input: ")

    userInput = userInput.split(" ")
    #checking error for user input
    for i in range (len(userInput)):
        if userInput[i] == "red":
            pass
        elif userInput[i] == "yellow":
            pass
        elif userInput[i] == "blue":
            pass
        elif userInput[i] == "green":
            pass
        else:
            Error = True
            errorinstruction()
            break

   #when no error on user input 
    if Error != True:
        temp_corColcorPlace = 0
        temp_corColwrongPlace = 0

        
        #check for the first time for the correct colour correct place
        for i in range (len(userInput)):
            if userInput[i] == temp_colour_list[i]:
                temp_corColcorPlace += 1
                temp_colour_list[i] = "checked"
                userInput[i] = "userchecked"

        corColcorPlace = temp_corColcorPlace 
        #check for the second time for the correct colour wrong place
        for i in range (len(userInput)):
            for j in range( len(temp_colour_list)):
                if userInput[i] == temp_colour_list[j]:
                    temp_corColwrongPlace += 1
                    temp_colour_list[j] = "checked"
                    userInput[i] = "userchecked"

        #print out the value of
        print("\nCorrect colour correct place: " +str(temp_corColcorPlace) +"\tCorrect colour wrong place: " +str(temp_corColwrongPlace))
    #add 1 when 1 attempt has made
    attempt+=1
#print out from define wingame above
wingame()