from pynput import keyboard
from note_format import char_to_note
import keyb_visualizer
from sound_module import play_note


def key_press(key):

    # 1. Converts [keyboard input] character to <note>
    try:
        note = char_to_note(key.char)
    except:
        return None

    # 2. Plays the note sound     
    play_note(note)

    # 3. Shows the note on a piano-roll
    diagram = keyb_visualizer.single_note(note)

    print(f'{diagram}')

def key_release(key):

    # This should also send message to visualiser function but with
    # an additional argument to specify removal 
    # eg: diagram = keyb_visualizer.single_note(note, 'off')
    pass

if __name__ == '__main__':

            # 1.0: Sets up the <Listener> in a [context manager]
    with keyboard.Listener(on_press=key_press) as listener:

            # 2.0: Continues program running
        listener.join()