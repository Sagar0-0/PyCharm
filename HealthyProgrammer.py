from pygame import mixer
from datetime import datetime
from time import time


def musciOnLoop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    water_time = 60
    while True:
        if time() - init_water > water_time:
            print("Time to Drink water. Type 'drank' to stop the alarm")
            musciOnLoop('faisu.mp3', 'drank')
            init_water = time()
            log_now('Drank water at')

# started playing music
# file = 'faisu.mp3'
# mixer.init()
# mixer.music.load(file)
# mixer.music.play()
#
# # getting current time
# now = datetime.now()
# start_time = now.strftime("%S")
#
# input = input("Press 'e' to exit the loop")
# if input == 'e':
#
# lis = [start_time]
# # infinite loop
# while True:
#     t = datetime.now()
#     current_time = t.strftime("%S")
#     if abs(int(start_time) - int(current_time)) > 10:
#         mixer.music.play()
#         start_time = current_time
