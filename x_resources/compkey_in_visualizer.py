def note_to_index(note):

    note_index = {
        'C' : 2,
        'C#' : 4,
        'D' : 6,
        'D#' : 8,
        'E' : 10,
        'F' : 14,
        'F#' : 16,
        'G' : 18,
        'G#' : 20,
        'A' : 22,
        'A#' : 24,
        'B' : 26,
    }

    return note_index[note]

def base_model():
    
    return """
|  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |
|  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|
  C   D   E   F   G   A   B  
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



