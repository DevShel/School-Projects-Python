# This a trivia game
import random
question_num = 0
correct = 0
x = "not_used"

def get_question(num_for_question):
  #Opening file
  with open("questions.txt") as file:
    lines = file.readlines()
    print("\n")
    #Using random number to import a question from text file
    for i in range((num_for_question)*10-1,(num_for_question)*10+4):
      printed_line = (lines[i])
      #Printing the imported question without the last 7 letters 
      if printed_line[-8:-1] == "CORRECT":
        print (printed_line[:-8])
      else:
        print (printed_line)


def find_where_correct(num_for_question):
  #Opening file
  with open("questions.txt") as file:
    lines = file.readlines()
    #Using random number to import a question from text file
    for i in range((num_for_question)*10-1,(num_for_question)*10+4):
        line_check = lines[i]
         #Detecting if the last 7 characters are correct, to determine the line index of right answer
        if line_check[-8:-1] == "CORRECT":
          return i
          
          
#Checks if correct
def check_if_correct(num_for_question,correct_answer_placement,answer):
  #Opening file
  with open("questions.txt") as file:
    lines = file.readlines()
    #Using random number to import a question from text file
    for i in range((num_for_question)*10,(num_for_question)*10+4):
      line_check_for_first_letter = lines[i]
      if (line_check_for_first_letter[0]) == answer:
        if i == correct_answer_placement:
          print ("Correct")
          return(1)
        else :
          print ("Incorrect")
          return(0)




      
        


print("Welcome to QUESTION GAMESHOW, get to the eleventh level to win, here is your first question! \n")
#While the user hasn't completed 10 questions correctly
while question_num<=10:
  correct = 0
  print "Remember, you can type x to skip the question if you are stuck. THIS IS A ONE TIME USE POWERUP. IF YOU TRY TO USE IT TWICE YOU WILL BE KICKED OUT."
  print ("-------------------------------- \n")
  
  #Gets number that the question will be based on
  num_for_question = random.randint(1,20)
  get_question(num_for_question)
  correct_answer_placement = find_where_correct(num_for_question)
  answer = raw_input("What is your choice?: ")
  answer = answer.lower()
  # If the user inputs anything other than the five possible choices, they are declined 
  if answer == "a" or answer == "b" or answer == "c" or answer == "d" or answer=="x":
    #This deals with the use of the powerup "x"
    if answer == "x":
      if x=="used":
        print "X is used"
        correct = 2
        break
      if x == "not_used":
        correct = 1
        x = "used"
    else:
      #If the user doesn't select x then the program uses the check function to see if the user answered correctly
      correct = check_if_correct(num_for_question,correct_answer_placement,answer)
  else:
    print ("Invalid Input")
    break
  if correct == 0:
    #If user gets it wrong
    print "You lose"
    break
  if correct == 1:
    #If user gets it right
    question_num = question_num + 1
    print ("Question number : " + str(question_num))
  if correct == 2:
    #If user uses x powerup
    question_num = question_num

if question_num>10:
    print ("You have made it to the 11th level, you are an expert at trivia.")
else :
    print ("Goodbye")










