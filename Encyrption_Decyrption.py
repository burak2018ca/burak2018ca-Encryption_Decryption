# %***********************************************************************%
# %                                                                       %
# %                          PROGRAM HEADER                               %
# %***********************************************************************%
# %***********************************************************************%
# %                                                                       %
# % PROGRAMMER'S NAME:    Burak Yildirim                                  %
# %                                                                       %
# % DATE:                 Tuesday 19/May/2020                             %
# %                                                                       %
# % PROGRAM NAME:         Encyription_Decyription                         %
# %                                                                       %
# % CLASS:                TEJ3M1                                          %
# %                                                                       %
# % ASSIGNMENT:           Assignment 2                                    %
# %                                                                       %
# % TEACHER:              Mr. Henrich                                     %
# %                                                                       %
# % DUE DATE:             Tuesday, 19/May/2020                            %
# %                                                                       %
# %***********************************************************************%
# %                                                                       %
# % WHAT THE PROGRAM DOES                                                 %
# %                                                                       %
# % This program can Encyripts and Decyripts user's text in 3 differen    %                    
# % style 1)ROTn 2)XOR 3)Vingenere                                        %
# %                                                                       %
# %                                                                       %
# %                                                                       %
# %***********************************************************************%
# %                                                                       %
# % PROCEDURES                                                            %
# %                                                                       %
# % One procedure is used within this program:                            %
# % gui:            get clear text from user                              %
# %                 get key word from user                                %
# %                 Return Encyripted word                                %
# %***********************************************************************%
# %                                                                       %
# % ERROR HANDLING                                                        %
# %                                                                       %
# % This program does not have any type of error handling routines, as the%
# % user can only interact with the program via the mouse.                %
# %                                                                       %
# %***********************************************************************%
# %                                                                       %
# % PROGRAM LIMITATIONS                                                   %
# %                                                                       %
# % This program will only Encyript and Decyript in 3 styles              %
# %                                                                       %
# %***********************************************************************%
# %                                                                       %
# % EXTENSIONS AND IMPROVEMENTS                                           %
# % This program could be improved in a variety of ways:                  %
# % 1. Allow user to encyript in more styles                              %
# % 2. Allow user to decyript in more styles                              %
# %***********************************************************************%

Main_menu = "1)ROTn \n2)XOR \n3)Vigenere \n4)Exit\n"
Sub_menu = "\n\n1)Encyrption \n2)Decytption \n3)Exit"

def Vigenere_Encyription(word, key):
    Ency_word = " "
    key = (key + " ") * len(word) 

    for x in range(0, len(word)):
        letter = ord(word[x])
        key_letter = ord(key[x])
        difference = ord(key[x]) - 96

        if (letter > 122 or letter < 97):
            Ency_word += word[x]
        elif (key_letter > 122 or key_letter < 97):
            Ency_word += word[x]
        elif (123 > (letter + difference)):
            Ency_letter = letter + difference
            Ency_word += chr(Ency_letter)
        else:
            difference = (difference + letter) - 122
            Ency_word += chr(96 + difference)

    print (f"\n\n\nEncyripted word is {Ency_word}")  


def Vigenere_Decyription(word, key):
    Decy_word = " "
    key = (key + " ")*len(word)
    print (key)

    for x in range(0, len(word)):
        letter = ord(word[x])
        key_letter = ord(key[x])
        difference = ord(key[x]) - 96

        if (letter > 122 or letter < 97):
            Decy_word += word[x]
        elif (key_letter > 122 or key_letter < 97):
            Decy_word += word[x]
        elif (97 <= (letter - difference)):
            Decy_letter = letter - difference
            Decy_word += chr(Decy_letter)
        else:
            difference = difference  - (letter - 96)  
            Decy_word += chr(122 - difference)

    print (f"\n\n\nDecyripted word is {Decy_word}")
        

def Vigenere(menu):
    user_Input = " "

    while (user_Input != "3"):
        print(menu)
        user_Input = input ("Please select a number: ")
        
        if (user_Input ==  "1"):
            word = input("\n\n\nPlease type the word you want to encyript \n\n===> ")
            key = input("\n\n\nPlease type a key word  \n\n===> ")

            Vigenere_Encyription(word.lower(), key)
        elif(user_Input == "2"):
            word = input("\n\n\nPlease type the word you want to decyript \n\n===> ")
            key = input("\n\n\nPlease type the key word  \n\n===> ")

            Vigenere_Decyription(word.lower(), key)


def XOR_Encyription(word, key):
    Ency_word = [ ]

    for x in range(0, len(key)):
        letter = ord(word[x])
        key_letter =  ord(key [x])
        Ency_letter = 0
        if (letter >= key_letter):
            Ency_letter = letter + key_letter
            Ency_word.append(Ency_letter)
        elif (key_letter > letter):
            Ency_letter = key_letter + letter
            Ency_word.append(Ency_letter)

    print ("\n\nEncyripted word is ===>", end = " ")

    for x in range(0, len(Ency_word)):
        print(f"|{Ency_word[x]}|", end=" ")


def XOR_Decyrption(word, key):
    Decy_word = " "

    for x in range(0, len(word)):
        letter = ord(word[x])
        key_letter = ord(key[x])

        if(letter >= key_letter):
            decy_letter = letter - key_letter
            Decy_word += chr(decy_letter)
        elif(key_letter > letter):
            decy_letter = key_letter - letter
            Decy_word += chr(decy_letter)

    print (f"\n\nDecyripted word is ===> {Decy_word}")


def XOR(menu):
    User_input = "0"
    while (User_input != "3"):
        print(menu)
        User_input = input ("\nPlease select menu number: ")

        #Ency
        if (User_input == "1"):
            word  = input("\nPlease enter the word you want to encyrpt \n===> ")
            Key_word = " "
            while(len(Key_word) !=  len(word)):
                Key_word = input("\nPlease enter a key word that has the same length as encyripted word\n===> ")
            XOR_Encyription(word, Key_word)

        #Decy    
        elif (User_input == "2"):
            Ency_letter = []

            byte = None
            check1 = False
            check2 = False 
            Key_word = " "
            counter = 1 

            while (check1 != True):
                byte = input(f"\n\n\nTo Exit press ==> 'Q' \n\nLetter: {counter} \nPlease enter the binary byte size \n===> ")
                counter += 1

                if (byte == "q" or byte == "Q"):
                    check1 = True
                    break

                Ency_letter.append(chr(int(byte)))

            while(check2 != True):

                Key_word = input("\n\n\nTo Exit press ==> 'Q' \nPlease type the key word and press ENTER to confim it \n\nnote:(key word has the same length as decyripted word) \n===> ")

                if (len(Key_word) ==  len(Ency_letter) or Key_word == "q" or Key_word == "Q"):
                    check2  = True

            XOR_Decyrption("".join(Ency_letter), Key_word)


def ROTn_Encyription(word, num):
    Ency_word = " "
    for x in range(0,len(word)):
        difference = 123 - ord(word[x]) 
        if (ord(word[x]) > 122 or ord(word[x]) < 97):
            Ency_word += (word[x])
        elif (difference > num):
            Ency_word += (chr(ord(word[x]) + num))
        else:
            difference = num - difference
            Ency_word += (chr(97 + difference))

    print (f"Encyripted word is {Ency_word}")


def ROTn_Decyrption(word, num):
    Decy_word = " "
    for x in range(0, len(word)):
        difference = ord(word[x]) - 97
        if (ord(word[x]) > 122 or ord(word[x]) < 97):
            Decy_word += (word[x])
        elif (difference >= num):
            Decy_word += (chr(ord(word[x]) - num))
        else:
            difference = num - difference
            Decy_word += (chr(123 - difference))
    
    print (f"Decyripted word is {Decy_word}")


def ROTn(menu):
    User_input = "0"
    num = 0
    while (User_input != "3" or (num > 0 and num > 26) ):
        print(menu)
        User_input = input ("\nPlease select menu number: ")
        if (User_input == "1"):
            word  = input("\nPlease enter the word you want to encyrpt \n===> ")
            num   = int(input ("\nPlease enter encyription number between 1-26: "))
            ROTn_Encyription(word.lower(), num)
        elif (User_input == "2"):
            word  = input("\nPlease enter the text you want to decyrpt \n===> ")
            num   = int(input ("\nPlease enter decyription number between 1-26: "))
            ROTn_Decyrption(word.lower(), num)



def Main(menu):
    User_input = "0"
    while (User_input != "4"):
        print(f"\n\n\n\n{menu}")
        User_input = input ("Please select menu number: ")

        if (User_input == "1"):
            ROTn(Sub_menu)  
        elif(User_input == "2"):
            XOR(Sub_menu)
        elif(User_input == "3"):
            Vigenere(Sub_menu) 

Main(Main_menu)