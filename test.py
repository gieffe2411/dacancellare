'''
import random

passwordLen = int(input("Enter the length of password to generate: "))

NOfPasswords = 5000

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

generated = ""

print("Generated Passwords:")
print("")

for _ in range(NOfPasswords):
	generated = ""
	for i in range(passwordLen):
		generated = generated + characters[random.randint(0, len(characters) - 1)]

	print(generated)
	print("")
'''


'''

	COSA 2

for i in range(5):
	print("*" * i)
'''


'''
	COSA 3

name = input("Enter your name: ")
print("*************")
print("*" + name + "*")
print("*************")

'''

'''

while True:

	n = int(input("Enter a number: "))

	# calc factorial

	factorial = 0
	for i in range(n):
		factorial += i
	print(factorial)

'''
import random
maxTentativi = 5
secretNumber = random.randint(1, 20)

for i in range(maxTentativi):
	guess = int(input("Enter your guess (between 1 and 20): "))
	if guess < secretNumber:
		print("Your guess is too low.")
	elif guess > secretNumber:
		print("Your guess is too high.")
	else:
		print("Congratulations! You guessed the number in", i + 1, "tries.")
		break
print("The secret number was:", secretNumber)





