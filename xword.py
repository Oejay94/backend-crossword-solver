#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Joey Brown"

# YOUR HELPER FUNCTION GOES HERE
import re


def word_finder(input_word, dictionary):
    regex = r'\w'

    new_word = input_word.replace(' ', regex)
    re_word = re.compile(new_word)

    for word in dictionary:
        if len(word) == len(input_word):

            if re.match(re_word, word):
                print(word)


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters:\
        ').lower()

    # YOUR ADDITIONAL CODE HERE
    word_finder(test_word, words)


if __name__ == '__main__':
    main()
