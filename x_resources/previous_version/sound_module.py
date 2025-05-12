import pygame 

pygame.mixer.init()

note_sounds = {
    'C' : pygame.mixer.Sound("sound_files/C.wav"),
    'C#' : pygame.mixer.Sound("sound_files/C#.wav"),
    'D' : pygame.mixer.Sound("sound_files/D.wav"),
    'D#' : pygame.mixer.Sound("sound_files/D#.wav"),
    'E' : pygame.mixer.Sound("sound_files/E.wav"),
    'F' : pygame.mixer.Sound("sound_files/F.wav"),
    'F#' : pygame.mixer.Sound("sound_files/F#.wav"),
    'G' : pygame.mixer.Sound("sound_files/G.wav"),
    'G#' : pygame.mixer.Sound("sound_files/G#.wav"),
    'A' : pygame.mixer.Sound("sound_files/A.wav"),
    'A#' : pygame.mixer.Sound("sound_files/A#.wav"),
    'B' : pygame.mixer.Sound("sound_files/B.wav"),
}

def play_note(note):

    if note in note_sounds:

        note_sounds[note].play()

