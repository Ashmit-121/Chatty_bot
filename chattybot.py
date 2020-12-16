def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input('>> ')
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me know your age.')
    print('What is your date of birth')

    age = input('>> ')
    print(2020 - int(age))


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("""Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.""")
    while input('>> ') != "2":
        print("Please, try again.")
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Bot', '2020')  # change it as you need
remind_name()
guess_age()
test()
end()
