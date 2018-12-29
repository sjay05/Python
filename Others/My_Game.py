from time import sleep

game = raw_input("This is a lesson about coding. Before we start we will be asking you some math questions. You have to answer all the yes or no questions with Yes or No(case-sensitive). Are you ready to begin?")

if game == "Yes":
  print "Get ready!"
  sleep(1)
elif game == "No":
  print "Please play again later!"
  exit()

name = raw_input('What is your name?\n') 
print 'Hi, %s.' % name 
print "Let's code!"

x = raw_input("Are you a beginner?")

if x == "Yes":
  print "You suck!"
elif x == "No":
  print "You are not better than me! Ha!"
  
y = raw_input("Are you ready to learn?")

if y == "Yes":
  print "Stay Tuned!"
elif y == "No":
  print "What are you waiting for! Get out of my sight!"
  print "Ending lesson."
  sleep(2)
  print "Game Over!"
  exit()
  


r = raw_input("First we are going to learn about basic expressions. Have you learned about expressions before?")

if r == "Yes":
  print "Great!"
elif r == "No":
  print "I suggest you to go back to grade 1 to refresh your math skills"
  print "Ending lesson."
  sleep(2)
  print "Game Over!"
  exit()
  
v = raw_input("Okay. Well, what's 9+10")

if v == "19":
  print "Correct!"
elif v == "21":
  print "You stupid!"
  sleep(1)
  print "Game Over!"
  exit()
elif v != 19:
  print "WRONG!"
  print "Ending lesson"
  sleep(1)
  print "Game Over!"
  exit()
  
print "You won version 1 of this program"

y = raw_input("Do you want to continue to the second level?")

if y == "Yes":
  print "Now that we have refreshed your math skills let's get to the coding basics for python"
elif y == "No":
  print "Game Over"
  exit()
