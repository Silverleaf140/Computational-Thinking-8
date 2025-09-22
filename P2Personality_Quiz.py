Outdoor_points = 0
Indoor_points = 0

print(" _   _      _ _       _ ")
print("| | | |    | | |     | |")
print("| |_| | ___| | | ___ | |")
print("|  _  |/ _ \ | |/ _ \| |")
print("| | | |  __/ | | (_) |_|")
print("\_| |_/\___|_|_|\___/(_)")
name = input("What is your name?") 

print(f"Hello {name} Today we are going to do a fun personality quiz to see if you are an indoor person or an outdoor person!")
print("let's start! ~enter to continue~")
input("")

answer = input("In your free time would you rather A) Go on a walk or B) Play video games with your friends?")
if answer == "A":
    Outdoor_points += 1
elif answer == "B":
    Indoor_points += 1

print("Cool! lets go to the next question. ~Enter to continue~ ")
input("")

answer = input("Do you A) Like to garden or B) Like to do arts and crafts?")
if answer == "A":
    Outdoor_points += 1
elif answer == "B": 
    Indoor_points += 1

print("Nice! now we are going to move on to the third question. ~Enter to continue~ ")
input("")

answer = input("Do you A) Like sports or do you B) like to play music?")
if answer == "A":
    Outdoor_points += 1
elif answer == "B":
    Indoor_points += 1

print("Perfect! halfway there! lets go to question four! ~Enter to continue~ ")
input("")


answer == input("Do you A) like coding class or do you B) like P.E? ")
if answer == "A": 
    Indoor_points += 1
elif answer == "B":
    Outdoor_points += 1

print("Good job! ~Enter to continue~") 
input("")


answer == input(" Do you like A) reading books or B) Like watching a movie or C) Like climbing a tree?")
if answer == "A" or "B":
    Indoor_points += 1
elif answer == "C":
    Outdoor_points += 1 

print("Nice! Next! ~Enter to continue~")
input("")

answer == input("Are you A) an early riser or B) a late sleeper?")
if answer == "A":
    Outdoor_points += 1
elif answer == "B":
    Indoor_points += 1


print("Great! now for the last question! ~Enter to continue~")
input("")


answer == input("Do you A) like dogs or do you B) like cats?")
if answer == "A":
    Outdoor_points += 1
elif answer == "B":
    Indoor_points += 1


print("Great! now lets see your results.")

if Outdoor_points > Indoor_points:
    print("You are an outdoor person!!!")
elif Indoor_points > Outdoor_points:
    print("You are a indoor person!")
elif Outdoor_points == 7 and Indoor_points == 0:
    print("You must really love the outdoors!")
elif Indoor_points == 7 and Outdoor_points == 0:
    print("You must really love the indoors ~Enter to continue~ !")

input("")
print("Thats all for today! Thank you and see you next time!")





