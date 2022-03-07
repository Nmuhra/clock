import os 
import datetime
from playsound import playsound
from AppKit import NSSoun
os. system("clear")
alarmH = int(input("Hour:\n"))
alarmM = int(input("Minute:\n"))
ampm = input("Am or Pm :\n").lower()
os. system("clear")
print("waiting for alarm...", alarmH, alarmM, ampm)
if (ampm == "pm"):
  alarmH = alarmH + 12
  while (1==1):
    if(alarmH == datetime.datetime.now().hour and 
    alarmM == datetime.datetime.now().minute ) :
    playsound(str("alarm/Buzzer.mp3"))
    stop_alarm = input("Stop: y/n").lower()
    if stop_alarm == "y":
     break
