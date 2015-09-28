
MAIN_MENU_PROMPT = '''
Welcome to Mailroom Madness

Choose from the following:

T - Send a (T)hank You

R - Create a (R)eport

quit - Quit the program
'''
T_MENU_PROMPT = '''
Please enter a name, or choose from the following:

list - Print a list of previous donors

quit - Return to main menur's full name.
'''
AMOUNT_PROMPT = '''
Please enter a donation amount or 'quit':
'''


def repl(data, prompt, validator=None):
    """request input from the user with `prompt` and return the result

    optionally, validate the input with a function `validator` which must
    take one argument, the input from the user and must return the input if
    valid, and None if not valid
    """
    while True:
        user_input = input(prompt)
        if validator:
            result = validator(data, user_input)
            if result:
                if result in ('Q','quit'):
                    print 'Quitting...'
                    return
                elif 'Invalid' in result:
                    print result
                else:
                    print result
                    return result


def main_menu(data, user_input):
    '''
    main program loop;
    can redirect to sub-loops

    '''
    if user_input == 'quit':
        return user_input
    elif user_input == 'T':
        repl(data, T_MENU_PROMPT, t_menu)
    elif user_input == 'R':
        repl(data, '', r_menu)
    else:
        return 'Invalid command.'


def t_menu(data, user_input):
    if user_input == 'list':
        #################
        return
    elif user_input == 'quit':
        return user_input
    else:
        name = user_input
        if is_valid_name(name):
            amount = repl(data, AMOUNT_PROMPT, is_valid_amount)
            data = add_to_data(data, name, amount)
        else:
            return 'Invalid Name.'


def is_valid_name(name):
    names = name.split(' ')
    if len(names) < 2:
        return False
    for n in names:
        if not n.isalpha() or not n.istitle():
            return False
    return True


def is_valid_amount(data, user_input):
    try:
        return round(float(user_input), 2)
    except ValueError:
        return 'Invalid Amount'


def r_menu(data, user_input):
    pass


def add_to_data(data, name, amount):
    if name not in data.keys():
        data[name] = []
    data[name].append(amount)
    return data


#######################
# PSEUDO VERSION
def main_menu():
    '''
    main program loop;
    can redirect to sub-loops

    '''

    donor_data = {}
    while True:
        print 'Choose a comand:'
        print "T: Send a thank you note."
        print "R: Print report."
        print "Q: Quit."
        user_input = input('Your command:')

        if user_input == 'Q':
            print 'Quitting...'
            return

        elif user_input == 'T':
            t_menu()
        elif user_input == 'R':
            report(donor_data)
        else:
            print 'Invalid command.'


def t_menu():
    '''
    Send Thank You menu loop
    '''
    while True:
        print list of options:
        print "L: see a list of donor names"
        print "Q: quit to main menu"
        print "Or type a donor's full name"
        user_input = input('Your Command:')

        if user_input == 'Q':
            break and return

        elif user_input == 'L':
            print_list and return
        else:
            if is_valid_name(user_input):
                name = fetch_from_data(user_input)
                if not name:
                    add_to_data(user_input)

                amount = input('Enter Amount:')

                if is_valid_amount(amount):
                    add_to_data(name, amount)
                    write_formatted_email(name, amount)
                        break and return
                else:
                    print 'invalid donation amount'
            else:
                print 'invalid donor name'


def report(donor_data):
    '''
    print one super neatly formatted row per donor
    '''
    print 'Report Table Header'
    sorted_list = donor_data.keys().sort()
    for donor in sorted_list:
        donations = donor_data[donor]
        num = len(donations)
        total = sum(donations)
        avg = num / total

        '{} super neat format {} {} {}'.format(donor, num, total, avg)

    return


if __name__ == '__main__':
    data = {}
    try:
        repl(data, MAIN_MENU_PROMPT, main_menu)
    except Exception as e:
        print 'ERROR IN MAIN LOOP'
        raise e
