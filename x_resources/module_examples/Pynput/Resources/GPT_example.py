from pynput import keyboard

key_to_midi = {
	'z': 60,  # C
    's': 61,  # C#
    'x': 62,  # D
    'd': 63,  # D#
    'c': 64,  # E
    'v': 65,  # F
    'g': 66,  # F#
    'b': 67,  # G
    'h': 68,  # G#
    'n': 69,  # A
    'j': 70,  # A#
    'm': 71   # B
}

key_to_note = {
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
    'm': 'B'
}




# Function to handle key presses
def on_press(key):
    try:
        # If a regular key is pressed, print its character
        if key.char in key_to_note:
        	note = key_to_note[key.char]        
        	print(f"Note: {note}")



    except AttributeError:
        # If an invalid key is pressed
        pass

# Define a function to handle key releases (optional)
def on_release(key):
    # If the 'Esc' key is pressed, stop the listener
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False

def main():

# Set up the listener for key presses and key releases
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

if __name__ == "__main__":
    main()