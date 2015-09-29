import sys
import random

trigrams = {}

def repl(prompt, validator=None):
    while True:
        user_input = raw_input(prompt)
        if user_input in ('q', 'Q', 'quit', 'Quit'):
            print 'Quitting'
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
    try:
        textfile = open(filename, 'r')
    except:
        return 'Invalid Filename'

    lines = textfile.readlines()
    textfile.close()


def main(filename):
    textfile = open(filename, 'r')
    lines = textfile.readlines()
    textfile.close()

    words = []
    for l in lines:
        words.extend(l.split(' '))

    trigrams = {}
    for i, w in enumerate(words):
        if i + 2 < len(words):
            one = w.strip()
            two = words[i + 1].strip()
            three = words[i + 2].strip()

            onetwo = '{} {}'.format(one, two)
            if onetwo not in trigrams.keys():
                trigrams[onetwo] = []
            trigrams[onetwo].append(three)

    new_words = create_new_words(trigrams, 100)
    print ' '.join(new_words)


def create_new_words(trigrams, num, new_words=[]):
    if len(new_words) >= num:
        return new_words
    if not new_words:
        starting_two = random.choice(trigrams.keys())
        new_words.extend(starting_two.split(' '))
    if len(new_words) > 1:
        onetwo = '{} {}'.format(new_words[-2], new_words[-1])
        if onetwo not in trigrams.keys():
            onetwo = random.choice(trigrams.keys())
        three = random.choice(trigrams[onetwo])
        new_words.append(three)
        return create_new_words(trigrams, num, new_words)


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print 'No filename given.'
    else:
        filename = sys.argv[1]
        main(filename)
