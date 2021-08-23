from time import strftime
import time
import datetime

# playsound library for play alarm sound
from playsound import playsound

# time setting input
t = input("Enter the time of alarm 'HH:MM:SS':")

# function of setting alarm
def alarm(t):
    alarmtime = f"{t[0:2]}:{t[3:5]}:{t[6:8]}"
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        if time_now == alarmtime:
            for i in range(5):
                playsound('E:/python-projects/Algorithms/pythonProject/alarm/audio.mp3')
            print("Wake Up Hurry !!")
            break

if __name__ == '__main__':
    alarm(t)




