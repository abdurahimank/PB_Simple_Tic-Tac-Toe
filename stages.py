# Stage 3/5: Guess the age
print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
rem_3 = int(input())
rem_5 = int(input())
rem_7 = int(input())
your_age = (rem_3 * 70 + rem_5 * 21 + rem_7 * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")
