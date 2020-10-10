def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("Which of the following choices is the correct way of converting from string to integer?")
    print("1. a = abs(input())")
    print("2. a = input(abs())")
    print("3. a = int(input())")
    print("4. a = integer(input())")
    print("5. a = input(integer())")
    print("6. a = input(int())")
    u_input = int(input())
    if u_input == 3:
        print("Please, try again.")
    else:
        print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('T-X20', '2020.10')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
