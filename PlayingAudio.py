from pygame import mixer

file = 'faisu.mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()
# infinite loop
while True:

    print("Press 'p' to pause, 'u' to unpause, 's' to start again")
    print("Press 'e' to exit the program")
    query = input()

    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'u':

        # Resuming the music
        mixer.music.unpause()
    elif query=='s':
        mixer.music.play()
    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break
    else:
        print("Invalid input\nPlease try again from the options given below.")