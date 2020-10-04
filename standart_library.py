import sys
import re
from collections import Counter
from itertools import product


# -*- coding: utf-8 -*-
def test_dict_memory():
    dictionary = dict()
    old_size = sys.getsizeof(dictionary)
    for i in range(1000):
        dictionary[i] = i
        if sys.getsizeof(dictionary) > old_size:
            print(f'iteration {i:>4}: {old_size:>5} -> {sys.getsizeof(dictionary)}')
            old_size = sys.getsizeof(dictionary)


def most_popular_words(text, count=1):
    text = re.sub(r'[^a-zA-Zа-яА-Я ]', '', text.lower())
    text_split = re.split(r'[ ]+', text)
    sorted_words = sorted(Counter(text_split).items(), key=lambda a: a[1], reverse=True)
    return sorted_words[:count]


def most_popular_symbol(text, count=1):
    text = re.sub(r'[^a-zA-Zа-яА-Я]', '', text.lower())
    text_split = list(re.split(r'[ ]+', text)[0])
    sorted_words = sorted(Counter(text_split).items(), key=lambda a: a[1], reverse=True)
    return sorted_words[:count]


def count_mean_letter_in_words(text, letter):
    text = re.sub(r'[^a-zA-Zа-яА-Я ]', '', text.lower())
    text_split = re.split(r'[ ]+', text)
    return text.count(letter) / len(text_split)


def print_pairs(array, preffix=''):
    return '\n'.join([f'{preffix}"{element[0]}": {element[1]}' for element in array])


def process_text(filename='data/test_text'):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    print(print_pairs(most_popular_words(text), preffix='Слово '))
    print(print_pairs(most_popular_symbol(text), preffix='Буква '))
    letter = most_popular_symbol(text)[0][0]
    print(f'Среднее вхождение буквы "{letter}" в слово из текста: {count_mean_letter_in_words(text, letter)}')


def string_is_palindrome(string):
    size = len(string)
    return string[:size // 2] == string[::-1][:size // 2]


def generate_palindromes(n=5, characters=''):
    array = []
    for size in range(n+1):
        array += [''.join(element) for element in product(characters, repeat=size)]
    palindromes = [i for i in array if string_is_palindrome(i)]
    print(', '.join(palindromes))


if __name__ == '__main__':
    test_dict_memory()
    print('_'*80, '\n')
    process_text()
    print('_'*80, '\n')
    generate_palindromes(4, 'abc')
