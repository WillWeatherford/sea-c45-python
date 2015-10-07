'''
Tests methods of trigrams.py
'''
import trigrams as tg

TEST_FILE = 'sherlock_small.txt'

TEST_NUMS = [0, 3, 10, 99, 100, 101]


def test_words_from_file():
    words = tg.words_from_file(TEST_FILE)
    assert len(words) == 186


def test_trigrams_from_words():
    words = []
    trigrams = tg.trigrams_from_words(words)
    assert trigrams == {}

    words = ['Word']
    trigrams = tg.trigrams_from_words(words)
    assert trigrams == {}

    words = ['This', 'is', 'a', 'test', 'sentence.']
    trigrams = tg.trigrams_from_words(words)
    assert trigrams == {'This is': ['a'],
                        'is a': ['test'],
                        'a test': ['sentence.']}


def test_story_from_trigrams():
    words = ['This', 'is', 'a', 'test', 'sentence.']
    trigrams = tg.trigrams_from_words(words)

    for n in TEST_NUMS:
        story = tg.story_from_trigrams(trigrams, n)
        assert len([s for s in story.split(' ') if s]) == n


def test_main():
    assert len([s for s in tg.main(TEST_FILE).split(' ') if s]) >= 100

if __name__ == '__main__':
    test_trigrams_from_words()
    test_story_from_trigrams()
