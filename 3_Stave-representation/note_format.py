"""
Converts between note formats:
    1. keyboard letters --> Note Values

Development: 
    1. This module should also interpret the [raw midi input from a controller]
"""


def char_to_note(char):
    char_note = {
        'z': 'C',
        's': 'C#',
        'x': 'D',
        'd': 'D#',
        'c': 'E',
        'v': 'F',
        'g': 'F#',
        'b': 'G',
        'h': 'G#',
        'n': 'A',
        'j': 'A#',
        'm': 'B',
        ',': 'C',
        'l': 'C#',
        '.': 'D',
        ';': 'D#',
        '/': 'E'
    }
    
    if char in char_note:
        return char_note[char]

    else:
        return KeyError 