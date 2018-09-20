Python 3.7.0 ('_')
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> computerGuess=random.randint(0,100)
>>> while True:
	userGuess=int(input("Guess a number from 0 to 100: "))
	if userGuess>computerGuess:
		print("Guess lower:")
	elif userGuess<computerGuess:
		print("Guess higher:")
	else:
		print("Congratulations, you've guessed the 'Correct Number'")
		break

	
"""Guess a number from 0 to 100: 67
Guess lower:
Guess a number from 0 to 100: 50
Guess lower:
Guess a number from 0 to 100: 40
Guess lower:
Guess a number from 0 to 100: 30
Guess higher:
Guess a number from 0 to 100: 35
Guess lower:
Guess a number from 0 to 100: 33
Guess lower:
Guess a number from 0 to 100: 32
Guess lower:
Guess a number from 0 to 100: 31
Congratulations, you've guessed the 'Correct Number'"""
>>> 
