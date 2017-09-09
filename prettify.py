#!/usr/bin/env python3
# coding=utf-8

import fileinput

def prettify(original_code):

    # Read from transformations file
    direct_translations = {}
    mask_aliases = {}
    char_masks = []
    with open('transformations.txt', 'r') as myfile:
        lines = myfile.readlines()
        mask_lines = lines[1:lines.index('direct:\n')]
        mask_lines = [line.strip() for line in mask_lines]
        mask_lines = [line for line in mask_lines if line != '']
        direct_translation_lines = lines[lines.index('direct:\n')+1:]
        direct_translation_lines = [line.strip() for line in direct_translation_lines]
        direct_translation_lines = [line for line in direct_translation_lines if line != '']

        for line in direct_translation_lines:
            from_char, to_char = line.split(',')
            direct_translations[from_char] = to_char


        while len(mask_lines) > 0:
            line = mask_lines.pop(0)
            if line.startswith('alias'):
                char = line.split(' ')[1]
                mask_aliases[char] = []
                while len(mask_lines[0]) == 1:
                    line = mask_lines.pop(0)
                    mask_aliases[char].append(line)
            elif line.startswith('def'):
                char = line.split(' ')[1]
                masks = []
                current_mask = []
                while len(mask_lines)>0:
                    if mask_lines[0].startswith('def'):
                        break
                    line = mask_lines.pop(0)
                    current_mask.append(line)
                    if len(current_mask) >= 3:
                        masks.append(current_mask)
                        current_mask = []
                char_masks.append((char, masks))

    directly_translated_code = ''
    for char in original_code:
        if char in direct_translations:
            directly_translated_code += direct_translations[char]
        else:
            directly_translated_code += char


    directly_translated_code_lines = directly_translated_code.split('\n')

    max_line_length = max([len(line) for line in directly_translated_code_lines]) + 1

    text_grid = []
    text_grid.append(' '*max_line_length+'\n')
    for line in directly_translated_code_lines:
        text_grid.append(' '+line.ljust(max_line_length)+'\n')
    text_grid.append(' '*max_line_length+'\n')

    # print(''.join(text_grid))

    def matches(char, mask_char):
        if char == mask_char:
            return True
        elif mask_char == 'p':
            return char in '-|+/\\tT╬╗╔║═↙↘v^<>⇓⇑⇐⇒*⁕╫╚╝'
        elif mask_char == 'h':
            return char in '-+/\\tT╬╗╔═↙↘<>⇐⇒⇓⇑*⁕╚╝'
        elif mask_char == 'v':
            return char in '|+/\\tT╬╗╔║↙↘v^⇐⇒⇓⇑*⁕╫╚╝'
        elif mask_char == 'w':
            return char in '.+/\\tT┆┄╯╰╮╭┼↙↘:!╫*'
        elif mask_char == '_':
            return True
        else:
            return False

    def transform_text_grid(text_grid, done_chars, char, masks):
        output = []
        for y in range(1, len(text_grid)-2):
            line = []
            for x in range(1, len(text_grid[y])-2):
                match_found = False
                for mask in masks:
                    valid = not done_chars[y][x]
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            # print(text_grid[y+dy][x+dx], mask[1+dy][1+dx])
                            if not matches(text_grid[y+dy][x+dx], mask[1+dy][1+dx]):
                                valid = False
                                break
                        if not valid:
                            break
                    if valid:
                        match_found = True
                        done_chars[y][x] = True
                        line.append(char)
                        break
                if not match_found:
                    line.append(text_grid[y][x])

            output.append(line)

        max_line_length = max([len(line) for line in output])
        padded_output = []
        padded_output.append(' '+' '*max_line_length+'\n')
        for line in output:
            padded_output.append(' '+''.join(line).ljust(max_line_length+1)+'\n')
        padded_output.append(' '+' '*max_line_length+'\n')
        padded_output.append(' '+' '*max_line_length+'\n')
        return padded_output, done_chars

    done_chars = [[False for _ in line] for line in text_grid]

    for char_mask in char_masks:
        char, masks = char_mask
        text_grid, done_chars = transform_text_grid(text_grid, done_chars, char, masks)

    return ''.join(text_grid)

if __name__ == '__main__':
    original_code = ''.join(fileinput.input())
    print(prettify(original_code))
