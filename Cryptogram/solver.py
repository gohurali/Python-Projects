#-------------------------------------------------------------------------------
# Name:        Gohur Ali
# Purpose:
#
# Author:      s-gali
#
# Created:     09/12/2013
# Copyright:   (c) s-gali 2013
# Licence
#-------------------------------------------------------------------------------
#crypto_msg = input('Enter Message to encode:')
import string
input_string = "ALZ WVSFAQAXAQVS, VS ALQF LCIVALZFQF, QF O YZGZ ALQST VM EOD QS, ALZ LOSUF VM ALZ KXUQWQOGC,ELQWL ALZC YOC AEQFA OSU FLOIZ QSAV OSC MVGY ALZC IPZOFZ. ALVYOF KZMMZGFVS".lower()
#input_string = "aaabbc"

decoding = {}

def init_with_dash():
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",",","."," "]
    for i in range(0,len(alpha)):
        decoding[alpha[i]] = "-";

init_with_dash()

def decrypting():
    decrypted_s = ""
    for i in range(0,len(input_string)):
        decrypted_s += (decoding[input_string[i]])
    return decrypted_s

def print_Decoding():
    global decoding
    for key, value in decoding.items():
        print(key + "->" + value)

def add_Code (command):
    #take apart the command
    dash_index = command.find("-")
    p1 = command[2:dash_index]
    p2 = command[dash_index + 1:]

    print("P1:" + p1 + "P2:" + p2)
    #fill the decoding table
    global decoding
    for i in range(0,len(p1)):
        decoding[p1[i]] = p2[i]

    print_Decoding()
    return ""
#d a-x

#pe
def get_encrypt():
    return input_string

#pd
def get_decrypt():
    return decrypting()

#c
def update_Cryptogram(user_input):
    global input_string
    input_string = user_input
    return input_string


#Frequency Analysis
def frequency_analysis(s):
    s = s.lower().translate(s.maketrans("","",string.punctuation))

    frequency = [0 for i in range(26)] #List Comprehension creates 26 0s in the list
    alphabet = [i for i in string.ascii_lowercase]
    #print(frequency)

##    for i in alphabet:
##        print(ord(i) - 97)

    for i in string.ascii_lowercase:
        frequency[ord(i)-97] = s.count(i)
    return frequency


#-----
def input_freq(s):
    frequency = frequency_analysis(s)
    print(frequency)

    freq = ""
    for i in range(len(frequency)):
        freq += "{0}:{1} ".format(string.ascii_lowercase[i],frequency[i])

    return freq
#e
def average():
    return "e - 12.702%,t- 9.056%,a-8.167%,o-7.507%,i- 6.966%,n-6.749%,s-6.327%,h-6.094%,r-5.987%,d-4.253%,l-4.025%,u-2.758%,c-2.782%,m-2.406%,w-2.360%,\n\
f-2.228%,g-2.015%,y-1.974%,p-1.929%,b-1.492%,v-0.978%,k-0.772%,j-0.153%,x-0.150%,q-0.095%,z-0.074%\n"

#h
def cryptogram_helpp():
    return "\
############################### Cryptogram Help ###############################\n\
q =  quits\
h/? or any illegal command will print a help message\n\
p = print out decrypted cryptogram\n\
e = print the average frequency of letters in the English language\n\
r = reset the program\n\
c [cryptogram] = Gets cryptogram from user\n\
f [af] - print out a frequency analysis of the cryptogram\n\
         - a = sorts alphabetically\n\
        - f = sorts by frequency\n\
        default behavior sorts by alphabetically\n\
 d [code] - [key] = letters in key replace letters in code to decrypt string\n\
        - example: d a-c will substitute 'c' for 'a' every time 'a' appears in the cryptogram\n\
         - example: d cfd-the will substitute 't' for 'c', 'h' for 'f', and 'e' for 'd'\n\
############################### Cryptogram Help ###############################\n\
Hit any key to go back to the menu\n"


#get cryptogram from user
#run a frequency analysis
#determine which letters go to which letters
#print out decrypted string

# Commands Specification
# q - quits
# c [cryptogram]- cryptogram - gets cryptogram
# f [af] - print out a frequency analysis of the crytogram
#        - a - sorts alphabetically
#        - f - sorts by frequency
#        - default behavior sorts by aplhabetically
# p - print out decrypted cryptogram
# pe - print out encrypted cryptogram
# pd - print out decrypted cryptogram
# d [code/string] [key] - letters in key replace letters in code to decrypt string
#                       - example: d a-c will substitute "c" for "a" everytime it appear in the cryptogram
#                       - example: d cfd-the  will substitute "t" for "c", "h", for "f", and "e" for "d"
# e - print the average frequency of letters in the English language
# h/? - typing "h" or "?" or any illegal command will print a help message which describes each command
# r - resets the cryptogram
message = ""

while True:
    command = input(message).lower()
    show_help = False
    #These are the commands for the Program
    if command[0] == "p" and command[1] == "e":
        print(get_encrypt())
    elif command[0] == "p" and command[1] == "d":
        print(get_decrypt())
    elif command[0] == "q":
        break
    elif command[0] == "e":
        print(average())
    elif command[0] =="c":
        update_Cryptogram(command[2:])
    elif command[0] =="d":
        add_Code(command)
    else:
        show_help = True
    #These are the messages that come up in the input box
    if show_help == True:
        message = cryptogram_helpp()
    else:
        message = ""
        message += "Cryptogram:" + get_encrypt() + "\n"
        message += "Decoded:" + get_decrypt() + "\n"
        message += "Frequency:"+ "\n" + input_freq(input_string)






##message = cryptogram_helpp()
##while True:
##    command = input(message).lower()
##    if command[0] == "q":
##        break
##    elif command[0] == "h":
##        message = cryptogram_helpp()
##    elif command[0] == "?":
##        message = cryptogram_helpp()
##    elif command[0] == "x":
##        message = ""
##    elif command[0] == "p" and command[1] == "e":  # print out encrypted cryptogram
##        message = print_encrypt()
##    elif command[0] == "p" and command[1] == "d":
##        message = print_decrypt()
##    elif command[0] =="c": # Gets Cryptogram from user
##        message = update_Cryptogram(command[2:])
##    elif command[0] == "e":  # print the average frequency of letters in the English language
##        message = average()
##    elif command[0] =="d":  # d [code] - [key] - letters in key replace letters in code to decrypt string
##        #print(frequency_analysis_sweg(a,f))
##        message = add_Code(command)
##
##
###++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##    elif command[0] =="f":  # default behavior sorted by alphabetically
##        frequency_analysis(input_string)
##        print(sum)
##        for i in range(len(frequency)):
##            print("{0}:{1:.2f}%".format(string.ascii_lowercase[i],frequency[i]/sum),end="")
##    elif command[0] =="fa": # fa - print out a frequency analysis of the cryptogram sorted by alphabetically
##        print(frequency_analysis_sweg(a,f))
##    elif command[0] =="ff": # ff - print out a frequency analysis of the cryptogram sorted by frequency
##        print(frequency_analysis_sweg(a,f))
##    else: # print help message for any illegal command
##        cryptogram_helpp()
##
