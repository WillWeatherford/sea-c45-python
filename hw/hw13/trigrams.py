import sys
import time
import random

# Hannah$ cd Documents/CodeFellows/sea-c45-python/hw/hw13


def main(filename, new_story_length=100):

    words = words_from_file(filename)

    trigrams = trigrams_from_words(words)

    output = story_from_trigrams(trigrams, new_story_length)

    print '-------------------------------------'
    return output


def words_from_file(filename):
    with open(filename, 'r') as textfile:
        return [word.strip('\n') for l in textfile.readlines()
                for word in l.split(' ')]


def trigrams_from_words(words):
    trigrams = {}
    for i, w in enumerate(words):
        if i + 2 < len(words):
            one = w.strip()
            two = words[i + 1].strip()
            three = words[i + 2].strip()
            onetwo = '{} {}'.format(one, two)
            trigrams.setdefault(onetwo, []).append(three)
    return trigrams


def story_from_trigrams(trigrams, num, new_words=[]):
    if len(new_words) >= int(num) or num < 3:
        return ' '.join(new_words)

    if not new_words:
        starting_two = random.choice(trigrams.keys())
        new_words.extend(starting_two.split(' '))

    if len(new_words) > 1:
        onetwo = '{} {}'.format(new_words[-2], new_words[-1])
        if onetwo not in trigrams.keys():
            onetwo = random.choice(trigrams.keys())
        three = random.choice(trigrams[onetwo])
        new_words.append(three)
        return story_from_trigrams(trigrams, num, new_words)


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        try:
            new_story_length = sys.argv[2]
        except IndexError:
            print('No new story length given; defaulting to new story length'
                  ' of 100 words')
            new_story_length = 100
        output = main(filename, new_story_length)
        print output
    except IndexError:
        print 'No filename given.'
