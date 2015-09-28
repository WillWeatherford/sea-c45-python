data = {
    'Bill Gates': [1.00, 10.00, 100.00],
    'Elon Musk': [8.00, 888.00, 8888.00],
    'Paul Allen': [1200.00]
}


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

quit - Return to main menu.
'''
AMOUNT_PROMPT = '''
Please enter a donation amount or 'quit':
'''
LETTER_TEMPLATE = '''
Dear {name},

Thank you so much for your kind donation of ${amount}. We here at the Foundation
for Homeless Whales greatly appreciate it. Your money will go towards creating
new oceans on the moon for whales to live in.

Thanks again,

Jim Grant

Director, F.H.W.

Press enter to continue.
'''

CELL_WIDTHS = [20, 8, 3, 8]


def repl(prompt, validator=None):
    """request input from the user with `prompt` and return the result

    optionally, validate the input with a function `validator` which must
    take one argument, the input from the user and must return the input if
    valid, and None if not valid
    """
    while True:
        user_input = raw_input(prompt)
        if user_input in ('q', 'Q', 'quit'):
            print 'Quitting...'
            return
        if validator:
            result = validator(user_input)
            if result:
                if 'Invalid' in str(result):
                    print result
                else:
                    print result
                    return result
        else:
            return


def main_menu(user_input):
    '''
    main program loop;
    can redirect to sub-loops
    '''
    if user_input in ('t', 'T'):
        repl(T_MENU_PROMPT, t_menu)
    elif user_input in ('r', 'R'):
        repl('', r_menu)
    else:
        return 'Invalid command.'


def t_menu(user_input):
    if user_input == 'list':
        l = list_donor_names()
        return repl(l)
    else:
        name = user_input
        if is_valid_name(name):
            amount = repl(AMOUNT_PROMPT, is_valid_amount)
            if amount:
                add_to_data(name, amount)
                letter = LETTER_TEMPLATE.format(name=name,
                                                amount=format_amount(amount))
                return repl(letter)
        else:
            return 'Invalid Name.'


def list_donor_names():
    global data
    names = '\n'.join(data.keys())
    names += '\n\nPress enter to continue.'
    return names


def is_valid_name(name):
    names = name.split(' ')
    if len(names) < 2:
        return False
    for n in names:
        if not n.isalpha() or not n.istitle():
            return False
    return True


def is_valid_amount(user_input):
    try:
        return round(float(user_input), 2)
    except ValueError:
        return 'Invalid Amount'


def format_amount(amount):
    return '$%.2f'%amount


def r_menu(user_input):
    global data

    donor_list = data.keys()
    donor_list.sort()
    row_list = get_report_header()

    for d in donor_list:
        donations = data[d]
        total = sum(donations)
        num = len(donations)
        avg = total / num
        row = [d, format_amount(total), str(num), format_amount(avg)]
        row_list.append(get_report_cells(row))

    return '\n'.join(row_list)


def get_report_header():
    header = []
    header.append(get_report_cells(['Name', 'Total', '#', 'Average']))
    header.append('-' * (sum(CELL_WIDTHS) + (3 * len(CELL_WIDTHS))))
    return header


def get_report_cells(row):
    formatted_row = []
    for i, c in enumerate(row):
        spaces = ' ' * (CELL_WIDTHS[i] - len(c))
        formatted_row.append('{}{}'.format(spaces, c))
    return ' | '.join(formatted_row)


def add_to_data(name, amount):
    global data
    if name not in data.keys():
        data[name] = []
    data[name].append(amount)


if __name__ == '__main__':
    repl(MAIN_MENU_PROMPT, main_menu)


#######################
# PSEUDO VERSION
# def main_menu():
#     '''
#     main program loop;
#     can redirect to sub-loops

#     '''

#     donor_data = {}
#     while True:
#         print 'Choose a comand:'
#         print "T: Send a thank you note."
#         print "R: Print report."
#         print "Q: Quit."
#         user_input = input('Your command:')

#         if user_input == 'Q':
#             print 'Quitting...'
#             return

#         elif user_input == 'T':
#             t_menu()
#         elif user_input == 'R':
#             report(donor_data)
#         else:
#             print 'Invalid command.'


# def t_menu():
#     '''
#     Send Thank You menu loop
#     '''
#     while True:
#         print list of options:
#         print "L: see a list of donor names"
#         print "Q: quit to main menu"
#         print "Or type a donor's full name"
#         user_input = input('Your Command:')

#         if user_input == 'Q':
#             break and return

#         elif user_input == 'L':
#             print_list and return
#         else:
#             if is_valid_name(user_input):
#                 name = fetch_from_data(user_input)
#                 if not name:
#                     add_to_data(user_input)

#                 amount = input('Enter Amount:')

#                 if is_valid_amount(amount):
#                     add_to_data(name, amount)
#                     write_formatted_email(name, amount)
#                         break and return
#                 else:
#                     print 'invalid donation amount'
#             else:
#                 print 'invalid donor name'


# def report(donor_data):
#     '''
#     print one super neatly formatted row per donor
#     '''
#     print 'Report Table Header'
#     sorted_list = donor_data.keys().sort()
#     for donor in sorted_list:
#         donations = donor_data[donor]
#         num = len(donations)
#         total = sum(donations)
#         avg = num / total

#         '{} super neat format {} {} {}'.format(donor, num, total, avg)

#     return



