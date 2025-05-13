import mido
from mido import Message
from note_format import char_to_note
import ascii_visualiser
import time
#from sound_module import play_note

def info():
    info = """
        '0 --> Info'
        '1 --> Keyboard Input'
        '2 --> String Input'
        '3 --> File Input'
            """
    print(info)

def key_press(key):
    # msg example : note_on channel=0 note=62 velocity=123 time=0

        # 1. Converts [midi] impulse to <note><str>

    try:
        note = key.note
        print(note)
    except:
        return None
    
        # 2. Shows the note on a piano-roll
    diagram = ascii_visualiser.single_note(note)

    # 2. Plays the note sound - inactive development    
    #play_note(note)
    print(f'{diagram}')

def key_release(key):

    # This should also send message to visualiser function but with
    # an additional argument to specify removal 
    # eg: diagram = keyb_visualizer.single_note(note, 'off')
    pass

def test_strings():

    print("----\nRunning test strings\n----")
    time.sleep(2)

    test_msgs = [
        Message('note_on', channel=0, note=62, velocity=123, time=100),
        Message('note_on', channel=0, note=63, velocity=123, time=100),
        Message('note_on', channel=0, note=64, velocity=123, time=100),
        Message('note_on', channel=0, note=65, velocity=123, time=100)
        ]
    
    for i in range(len(test_msgs)):
        key_press(test_msgs[i])
        
        time.sleep(3)


def keyboard_input():

            # 0.0 Detects + assigns hardware
    for device in mido.get_input_names():
        if 'LPK25' in device:
            keyboard = device
              
            # 1.0: Sets up the <Listener> in a [context manager]
    with mido.open_input(keyboard) as port:
        for msg in port:
            if msg.type == 'note_on':
                key_press(msg)

if __name__ == '__main__':

    info()

    mode = int(input('Enter Choice: '))

    if mode == 0:
        pass

    if mode == 1:
        keyboard_input()

    if mode == 2:
        test_strings()



