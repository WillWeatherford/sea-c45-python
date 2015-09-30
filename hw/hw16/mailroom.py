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

Thank you so much for your kind donation of {amount}. We here at the Foundation
for Homeless Whales greatly appreciate it. Your money will go towards creating
new oceans on the moon for whales to live in.

Thanks again,

Jim Grant

Director, F.H.W.

'''
ENTER_TO_CONTINUE = '\n\nPress enter to continue.'

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
                    return result
        else:
            return


def main_menu(user_input):
    '''
    Main menu validator;
    Redirects to sub-menus.
    Returns None with successful use, or an Invalid message.
    '''
    if user_input in ('t', 'T'):
        repl(T_MENU_PROMPT, t_menu)
    elif user_input in ('r', 'R'):
        report()
    else:
        return 'Invalid command.'


def t_menu(user_input):
    '''
    Validator for "Send a Thank You Letter" menu
    redirects through to name and amount validators.
    Eventually returns a formatted letter or an invalid message.
    '''
    if user_input == 'list':
        print list_donor_names()
        return repl(ENTER_TO_CONTINUE)
    else:
        name = user_input
        if is_valid_name(name):
            amount = repl(AMOUNT_PROMPT, is_valid_amount)
            if amount:
                add_to_data(name, amount)
                letter = LETTER_TEMPLATE.format(name=name,
                                                amount=format_amount(amount))
                print letter
                return repl(ENTER_TO_CONTINUE)
        else:
            return 'Invalid Name.'


def list_donor_names():
    '''
    returns a list of all donor names in data, one per line.
    '''
    global data
    return '\n'.join(data.keys())


def is_valid_name(name):
    '''
    Checks for valid name: two capitalized words, all alphabetical
    characters.
    '''
    names = name.split(' ')
    if len(names) < 2:
        return False
    for n in names:
        if not n.isalpha() or not n.istitle():
            return False
    return True


def is_valid_amount(user_input):
    '''
    Validator for donation amount.
    Returns the float of the given number, or an invalid message
    '''
    try:
        return round(float(user_input), 2)
    except ValueError:
        return 'Invalid Amount'


def format_amount(amount):
    '''
    Returns a neatly formatted dollar amount string from a given int
    or float.
    '''
    return '$%.2f'%amount


def report():
    '''
    Gathers the current data and formats it into neat rows, then prints.
    '''
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

    print '\n'.join(row_list)
    return repl(ENTER_TO_CONTINUE)


def get_report_header():
    '''
    Returns neatly formatted column headers for the data report.
    '''
    header = ['\n']
    header.append(get_report_cells(['Name', 'Total', '#', 'Average']))
    header.append('-' * (sum(CELL_WIDTHS) + (3 * len(CELL_WIDTHS))))
    return header


def get_report_cells(row):
    '''
    Formats each row of donor data into neatly spaced cells, based on
    the CELL_WIDTHS constant.
    returns a single string formatted row
    '''
    formatted_row = []
    for i, c in enumerate(row):
        spaces = ' ' * (CELL_WIDTHS[i] - len(c))
        formatted_row.append('{}{}'.format(spaces, c))
    return ' | '.join(formatted_row)


def add_to_data(name, amount):
    '''
    Adds a given name and amount to the global data. Returns None.
    '''
    global data
    if name not in data.keys():
        data[name] = []
    data[name].append(amount)


if __name__ == '__main__':
    repl(MAIN_MENU_PROMPT, main_menu)
