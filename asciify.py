#!/usr/bin/env python3
# coding=utf-8

import fileinput

transformations = {
    '╬': '+',
    '╗': '\\',
    '╔': '/',
    '╚': '\\',
    '╝': '/',
    '┼': '+',
    '╭': '.',
    '╮': '.',
    '╯': '.',
    '╰': '.',
    '┄': '.',
    '┆': '.',
    '↘': 't',
    '↙': 'T',
    '═': '-',
    '║': '|',
    '⇓': 'v',
    '⇑': '^',
    '⇒': '>',
    '⇐': '<',
}

original_code = ''.join(fileinput.input())
transformed_code = ''
for char in original_code:
    if char in transformations:
        transformed_code += transformations[char]
    else:
        transformed_code += char

print(transformed_code)
