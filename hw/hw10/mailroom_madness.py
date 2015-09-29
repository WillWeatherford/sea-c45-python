



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
    try:
        main_menu()
    except Exception as e:
        print 'ERROR IN MAIN LOOP'
        raise e
