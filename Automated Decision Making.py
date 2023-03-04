import random 
import numpy

print("Hello!")
print("We have some movies that you might be interested in watching!")



happy = ['50 First Dates', 'Happy Gilmore', 'Lego Movie']
sad = ['Field of Dreams', 'Toy Story 3', 'Marley and Me']
fun = ['Die Hard', 'Fast and Furious', 'Avengers']
adventurous = ['Pirates of the Caribbean', 'The Little Prince', 'Howls Moving Castle']


moodChoice = input("Are you in a happy, sad, fun, or adventurous mood? ")


# mood automation to determin which mood they're in
if moodChoice.lower() == "happy":
    results = happy.pop(0)
    print(results)

if moodChoice.lower() == "sad":
    results = sad.pop(0)
    print(results)
    

if moodChoice.lower() == "fun":
    results = fun.pop(0)
    print(results)

if moodChoice.lower() == "adventurous":
    results = adventurous.pop(0)
    print(results)


# Confirm if this is what they want to watch if they choose sad
def sadConf(array):
    sadChoice = ""
    sadChoice = input("Would you like to watch this? ")
    if sadChoice == "yes":
        quit("We'll pull that movie up for you!")
    else:
        print("Okay, we'll find you another movie. ")  

    print(sad.pop(0))
    
    sadChoice = input("How about this? ")
    if sadChoice == "yes":
        print("We'll get that started!")
    else:
        print("We have one more option.")
    print(sad.pop(0))
    sadChoice = input("Are you interested?")
    if sadChoice == "yes":
        print("We'll get that started for you!")
    else:
        quit("We don't have any more movies!")
    
if moodChoice.lower() == "sad":
    sadConf(sad)

#if user selects happy
def happyConf(array):
    happyChoice = ""
    happyChoice = input("Would you like to watch this? ")
    if happyChoice == "yes":
        quit("We'll pull that movie up for you!")
    else:
        print("Okay, we'll find you another movie. ")  

    print(happy.pop(0))
    happyChoice = input("How about this? ")
    if happyChoice == "yes":
        print("We'll get that started!")
    else:
        print("We have one more option.")
    print(happy.pop(0))
    happyChoice = input("Are you interested?")
    if happyChoice == "yes":
        print("We'll get that started for you!")
    else:
        quit("We don't have any more movies!")
    
if moodChoice.lower() == "happy":
    happyConf(happy)


#if user selects fun
def funConf(array):
    funChoice = ""
    funChoice = input("Would you like to watch this? ")
    if funChoice == "yes":
        quit("We'll pull that movie up for you!")
    else:
        print("Okay, we'll find you another movie. ")  

    print(fun.pop(0))
    funChoice = input("How about this? ")
    if funChoice == "yes":
        print("We'll get that started!")
    else:
        print("We have one more option.")
    print(fun.pop(0))
    funChoice = input("Are you interested?")
    if funChoice == "yes":
        print("We'll get that started for you!")
    else:
        quit("We don't have any more movies!")

if moodChoice.lower() == "fun":
    funConf(fun)


#if user selects adventurous
def adventurousConf(array):
    adventurousChoice = ""
    adventurousChoice = input("Would you like to watch this? ")
    if adventurousChoice == "yes":
        quit("We'll pull that movie up for you!")
    else:
        print("Okay, we'll find you another movie. ")  

    print(adventurous.pop(0))
    adventurousChoice = input("How about this? ")
    if adventurousChoice == "yes":
        print("We'll get that started!")
    else:
        print("We have one more option.")
    print(adventurous.pop(0))
    adventurousChoice = input("Are you interested?")
    if adventurousChoice == "yes":
        print("We'll get that started for you!")
    else:
        quit("We don't have any more movies!")

if moodChoice.lower() == "adventurous":
    adventurousConf(adventurous)


######### below is code I tried but it wasn't working. I'll leave it here to show my thought process *****************

    #results = random.choice(sad)
    #print(results)
    #print("Are you interested in this one? ")
    #if confChoice == "yes":
        #print("We'll put that up for you! ")
  #  else:
  #      print("We have one more movie for you.")

    
    

#print(resultsSad)

#confChoice = input("Would you be interested in this? ")
#if confChoice == "yes":
 #   print("We'll pull your movie up!")
#else: 
 #   print("Okay, we have one more option.")

#print(results)

#if confChoice == "yes":
 #   quit("We'll pull your movie up!")
#else:
   # print("We have one more movie choice available.")

#confChoice = input("Would you like to see which movie it is? ")
#if confChoice == "yes":
  #  results = random.choices(happy)
   # quit(results)

#confChoice = input("Would you like to watch this? ")

#if confChoice == "yes":
 #   quit("We'll start it right away!")
#else:
   # quit("We're all out of movies")




    
#else:
 #   print("Okay, we'll find you another movie")

  #  results = random.choices(happy)
   # print(results)
   # print("Would you like to watch this? ")
 


#if moodChoice == "sad":
 #   results = random.choices(sad)
  #  print(results)


#if moodChoice == "yes":
 #   print("We'll pull that movie up for you!")
#else:
   # print("Okay, we'll find you another movie")
    #results = random.choices(sad)
    #print("How about this? ")
   # results = random.choices(sad)
   # print(results)
   # quit()






    


