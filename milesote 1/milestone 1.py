score = 0 
print("Welcome to the cricket quize")
print("Test what you know about cricket")


user_answer = input ("Who has scored the fastest t20 century? ")
A1 = "Sahil Chauhan"
print ("Your answer is  " + user_answer.upper())
if user_answer.upper() == A1.upper():
    print ("Correct! The fastest T20 century was scored by Sahil Chauhan of Estonia, who reached his century in just 27 balls.")
    score += 5
    print ("Well done, you have ", score, " points.")
else:
    print("Incorrect! Better luck next time")


user_answer = input ("Who has the most test wickets? ")
A2 = "Muttiah Muralitharan"
print ("Your answer is  " + user_answer.upper())
if user_answer.upper() == A1.upper():
    print ("Correct! Muttiah Muralitharan has taken the highest number of wickets in Test cricket, he has 800 wicket.")
    score += 5
    print ("Well done, you have ", score, " points.")
else:
    print("Incorrect! Better luck next time")


user_answer = input ("Who won the last world cup? ")
A3 = "Austraila"
print ("Your answer is  " + user_answer.upper())
if user_answer.upper() == A1.upper():
    print ("Correct! Austraila won the last world in 2023")
    score += 5
    print ("Well done, you have ", score, " points.")
else:
    print("Incorrect! Better luck next time")


user_answer = input ("What is the New Zealand Men's cricket team know as? ")
A4 = "Blackcaps"
print ("Your answer is  " + user_answer.upper())
if user_answer.upper() == A1.upper():
    print ("Correct! The New Zealand Men's team is know as the Blackcaps")
    score += 5
    print ("Well done, you have ", score, " points.")
else:
    print("Incorrect! Better luck next time")



user_answer = input ("What is the highist score scored by an individual in test cricket? ")
A5 = "Brian Lara"
print ("Your answer is  " + user_answer.upper())
if user_answer.upper() == A1.upper():
    print ("Correct! The highest individual score in Test cricket is 400 not out by Brian Lara of the West Indies. He achieved this incredible feat against England in April 2004.")
    score += 5
    print ("Well done, you have ", score, " points.")
else:
    print("Incorrect! Better luck next time") 

# Decision
# Total score

# The End 
# "Thank for having a go."
# "Want to have another go?"