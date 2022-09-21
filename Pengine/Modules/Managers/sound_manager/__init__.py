from replit import audio

def replit_play_sound(file, volume):
    source = audio.play_file(file)
    source.volume = volume