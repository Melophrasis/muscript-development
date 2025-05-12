def note_to_index(note):

    note_index = {
        48 : 2,
        49 : 4,
        50 : 6,
        51 : 8,
        52 : 10,
        53 : 14,
        54 : 16,
        55 : 18,
        56 : 20,
        57 : 22,
        58 : 24,
        59 : 26,
        60 : 30,
        61 : 32,
        62 : 34,
        63 : 36,
        64 : 38,
        65 : 42,
        66 : 44,
        67 : 46,
        68 : 48,
        69 : 50,
        70 : 52,
        71 : 54,
    }

    return note_index[note]

def base_model():
    
    return """
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
  C   D   E   F   G   A   B   C   D   E   F   G   A   B  
""".lstrip()

def single_note(note):
    base = base_model()
        # Position of note on Diagram
    n_index = note_to_index(note)
        # Flag to stop at bottom of key-drawing
    end_flag = False
        # Newlines to separate from input / previous
    new_model = '\n\n\n\n\n\n\n\n\n\n'

    # This should be generalised to a drawing function:

        # Break string into lists for modification
    for raw_line in base.splitlines():
        line_list = list(raw_line)

        if line_list[n_index] == '_':
            end_flag = True

        elif end_flag == False:
            # Draws active note
            line_list[n_index] = 'x'

            # Rebuild string
        line_list.append('\n')
        new_line = ''.join(line_list)

        new_model += new_line

    return(new_model)

def multi_note(note):

    # Instead of taking the base-model as input
    # Take the output of the last note generation as input
    pass


### For isolated testing :

#if __name__ == '__main__':
#    while True:
#        note = input('Enter Note: ')
#        single_note(note.upper())



