import sys
import time

yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
# true = ["T", "t", "True"]
# false = ["F", "f", "False"]
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
correct = 0


class Player:  # Creating a class player

    # initialization or constructor method
    def __init__(self):
        self.name = input('Enter your name: ')
        self.age = input('Enter Your Age: ')
        self.location = input('Enter your country name: ')

    # displayPlayer method of class Player
    def displayPlayer(self):
        print("Player Name:", self.name, "\nPlayer Age:", self.age, "\nPlayer Location:", self.location)


GamePlayer = Player()
GamePlayer.displayPlayer()
print("\nOK! let's start with introduction!")
print("\nYou must respond to a few questions in order to see your final score in this text-based game."
      "\nRemember that the correct answer to every question is from the given options only....")
print("\nAre you ready ? Please select [Y/N]")
choice = input("")
if choice in yes:
    print("Good Luck ! ")
    print("--------")
else:
    print("We will meet next time.")
    sys.exit()

# Multiple choice questions....
time.sleep(1)
print("\nWhat do you call a computer on a network that requests files from another computer?")
print("\n(A) A client \n(B) A host \n(C) A router \n(D) A web server")
choice = input("")
if choice in answer_A:
    correct += 1  # If answer is correct, the player will get one point
else:
    correct -= 1
time.sleep(0.5)
print("\nHow can you catch a computer virus?")
print(
    "\n(A) Sending e-mail messages \n(B) Using a laptop during the winter \n(C) Opening e-mail attachments \n(D) Shopping on-line")
choice = input("")
if choice in answer_C:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\nGoogle (www.google.com) is a:")
print("\n(A) Search Engine \n(B) Number in Math \n(C) Directory of images \n(D) Chat service on the web")
choice = input("")
if choice in answer_A:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\nWhich is not an Internet protocol?")
print("\n(A) HTTP \n(B) FTP \n(C) STP \n(D) IP")
choice = input("")
if choice in answer_C:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\nWhat does CPU stand for?")
print(
    "\n(A) Cute People United \n(B) Commonwealth Press Union \n(C) Computer Parts of USA \n(D) Central Processing Uni")
choice = input("")
if choice in answer_D:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\nAnother name for a computer chip is:")
print("\n(A) Execute \n(B) Micro chip \n(C) Microprocessor \n(D) Select")
choice = input("")
if choice in answer_B:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\n www stands for:")
print("\n(A) World Wide Web \n(B) World Wide Wares \n(C) World Wide Wait \n(D) World Wide War")
choice = input("")
if choice in answer_A:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\nWhich of the following is not a valid domain name?")
print("\n(A) www.yahoo.com \n(B) www.yahoo.co.uk \n(C) www.com.yahoo \n(D) www.yahoo.co.in")
choice = input("")
if choice in answer_C:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\n'.JPG' extension refers usually to what kind of file?")
print("\n(A) System file \n(B) Animation/movie file \n(C) MS Encarta document \n(D) Image file")
choice = input("")
if choice in answer_D:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\n'.TXT' extension refers usually to what kind of file?")
print("\n(A) Text File \n(B) Image file \n(C) Audio file \n(D) Adobe Acrobat file")
choice = input("")
if choice in answer_A:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\n'CD' computer abbreviation usually means?")
print("\n(A) Command Description \n(B) Change Data \n(C) Copy Density \n(D) Compact Disc")
choice = input("")
if choice in answer_D:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\nIn computer jargon, RAM refers to")
print("\n(A) Read Only Menu \n(B) Random Access Memory \n(C) Random Accent Memory \n(D) Read Access Memory")
choice = input("")
if choice in answer_B:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\nHow many bits is a byte?")
print("\n(A) 4 \n(B) 8 \n(C) 16 \n(D) 32")
choice = input("")
if choice in answer_B:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\nComputers calculate numbers in what mode?")
print("\n(A) Decimal \n(B) Octal \n(C) Binary \n(D) None of the above")
choice = input("")
if choice in answer_C:
    correct += 1
else:
    correct -= 1
time.sleep(0.5)
print("\nThe speed of your net access is defined in terms of:")
print("\n(A) RAM \n(B) MHz \n(C) Kbps \n(D) Megabytes")
choice = input("")
if choice in answer_C:
    correct += 1
else:
    correct -= 0
time.sleep(0.5)
print("You got", correct, "out of 15 correct.")
time.sleep(0.5)
if correct >= 10:
    print("Good")
else:
    print("Not a good score, Better Luck next time!")




