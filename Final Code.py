your_name = input('Enter your name: ')
bot_name = 'Aid'
birth_year = '2020'
print('Hello! My name is ' + bot_name + '.')
print('I was created in ' + birth_year + '.')
print('Please, remind me your name.')
print('What a great name you have, ' + your_name +'!')
print('Let me guess your age.')
print('Say me remainders of dividing your age by 3, 5 and 7.')
remainder_3 = int(input('The remainder of your age divided by 3: '))
remainder_5 = int(input('The remainder of your age divided by 5: '))
remainder_7 = int(input('The remainder of your age divided by 7: '))
your_age = ((remainder_3 * 70 + remainder_5 * 21 + remainder_7 * 15) % 105)
print("Your age is " + str(your_age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')
your_number = int(input())
x = your_number
count = 0
if x <= your_number:
    print(str(x * 0) + ' !')
    while count < x:
        count += 1
        print(str(count) + ' !')
print("Let's test your programming knowledge.")
print('Why do we use methods?')
print("""1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
your_answer = int(input())
while your_answer <= 4:
    if your_answer == 1:
        print('Please, try again.')
        your_answer = int(input())
    elif your_answer == 3:
        print('Please, try again.')
        your_answer = int(input())
    elif your_answer == 4:
        print('Please, try again.')
        your_answer = int(input())
    elif your_answer == 2:
        print('Congratulations, have a nice day!')
        exit()
