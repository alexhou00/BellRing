from pygame import mixer
from datetime import datetime
from time import sleep

mixer.init()

mixer.music.load("./bell_LKJH.mp3")

times = (( 7,30), ( 8,15), ( 8,25), ( 9,10), ( 9,20), (10, 5), (10,15), (11,00), (11,10), (11,55),
         (12, 0), (12,20), (12,30), (13,10), (13,15), (14, 0), (14,10), (14,55), (15,10), (15,55))
print("\nProgram running...")
while True:
    h = datetime.now().time().hour
    m = datetime.now().time().minute
    if (h, m) in times and datetime.now().time().second==0:
        mixer.music.play()
        sleep(120)
