def encryption(message):

    new = list(message)

    i = 0
    while i < len(new):


        
        if new[i].upper() == "A":
            new[i] = "V"
        elif new[i].upper() == "B":
            new[i] = "Z"
        elif new[i].upper() == "C":
            new[i] = "6"
        elif new[i].upper() == "D":
            new[i] = "F"
        elif new[i].upper() == "E":
            new[i] = "Q"
        elif new[i].upper() == "F":
            new[i] = "I"
        elif new[i].upper() == "G":
            new[i] = "N"
        elif new[i].upper() == "H":
            new[i] = "W"
        elif new[i].upper() == "I":
            new[i] = "1"
        elif new[i].upper() == "J":
            new[i] = "5"
        elif new[i].upper() == "K":
            new[i] = "8"
        elif new[i].upper() == "L":
            new[i] = "G"
        elif new[i].upper() == "M":
            new[i] = "S"
        elif new[i].upper() == "N":
            new[i] = "L"
        elif new[i].upper() == "O":
            new[i] = "Y"
        elif new[i].upper() == "P":
            new[i] = "9"
        elif new[i].upper() == "Q":
            new[i] = "A"
        elif new[i].upper() == "R":
            new[i] = "R"
        elif new[i].upper() == "S":
            new[i] = "2"
        elif new[i].upper() == "T":
            new[i] = "E"
        elif new[i].upper() == "U":
            new[i] = "D"
        elif new[i].upper() == "V":
            new[i] = "U"
        elif new[i].upper() == "W":
            new[i] = "7"
        elif new[i].upper() == "X":
            new[i] = "P"
        elif new[i].upper() == "Y":
            new[i] = "M"
        elif new[i].upper() == "Z":
            new[i] = "C"
        elif new[i].upper() == "0":
            new[i] = "4"
        elif new[i].upper() == "1":
            new[i] = "H"
        elif new[i].upper() == "2":
            new[i] = "J"
        elif new[i].upper() == "3":
            new[i] = "O"
        elif new[i].upper() == "4":
            new[i] = "3"
        elif new[i].upper() == "5":
            new[i] = "B"
        elif new[i].upper() == "6":
            new[i] = "T"
        elif new[i].upper() == "7":
            new[i] = "0"
        elif new[i].upper() == "8":
            new[i] = "K"
        elif new[i].upper() == "9":
            new[i] = "X"
            
        i += 1
    
    message = ''.join(new)
    return(message)





def decryption(message):

    new = list(message)

    i = 0
    while i < len(new):


        
        if new[i].upper() == "V":
            new[i] = "A"
        elif new[i].upper() == "Z":
            new[i] = "B"
        elif new[i].upper() == "6":
            new[i] = "C"
        elif new[i].upper() == "F":
            new[i] = "D"
        elif new[i].upper() == "Q":
            new[i] = "E"
        elif new[i].upper() == "I":
            new[i] = "F"
        elif new[i].upper() == "N":
            new[i] = "G"
        elif new[i].upper() == "W":
            new[i] = "H"
        elif new[i].upper() == "1":
            new[i] = "I"
        elif new[i].upper() == "5":
            new[i] = "J"
        elif new[i].upper() == "8":
            new[i] = "K"
        elif new[i].upper() == "G":
            new[i] = "L"
        elif new[i].upper() == "S":
            new[i] = "M"
        elif new[i].upper() == "L":
            new[i] = "N"
        elif new[i].upper() == "Y":
            new[i] = "O"
        elif new[i].upper() == "9":
            new[i] = "P"
        elif new[i].upper() == "A":
            new[i] = "Q"
        elif new[i].upper() == "R":
            new[i] = "R"
        elif new[i].upper() == "2":
            new[i] = "S"
        elif new[i].upper() == "E":
            new[i] = "T"
        elif new[i].upper() == "D":
            new[i] = "U"
        elif new[i].upper() == "U":
            new[i] = "V"
        elif new[i].upper() == "7":
            new[i] = "W"
        elif new[i].upper() == "P":
            new[i] = "X"
        elif new[i].upper() == "M":
            new[i] = "Y"
        elif new[i].upper() == "C":
            new[i] = "Z"
        elif new[i].upper() == "4":
            new[i] = "0"
        elif new[i].upper() == "H":
            new[i] = "1"
        elif new[i].upper() == "J":
            new[i] = "2"
        elif new[i].upper() == "O":
            new[i] = "3"
        elif new[i].upper() == "3":
            new[i] = "4"
        elif new[i].upper() == "B":
            new[i] = "5"
        elif new[i].upper() == "T":
            new[i] = "6"
        elif new[i].upper() == "0":
            new[i] = "7"
        elif new[i].upper() == "K":
            new[i] = "8"
        elif new[i].upper() == "X":
            new[i] = "9"
            
        i += 1
    
    message = ''.join(new)
    return(message)









