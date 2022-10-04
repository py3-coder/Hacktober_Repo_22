r checking answers
Print statement – for printing outputs
print('Welcome to Quiz Game')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Do you follow Sourav? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What is the name of your favourite algo in Python?')
    if answer.lower()=='DFS':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
Output:

Welcome to Quiz
Are you ready to play the Quiz ? (yes/no) :yes
Question 1: What is your Favourite programming language?python
correct
Question 2: Do you follow Sourav? yes
correct
Question 3: What is the name of your favourite algo in Python?DFS
correct
Thankyou for Playing this small quiz game, you attempted 3 questions correctly!
Marks obtained: 100.0
BYE!
