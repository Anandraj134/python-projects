from datetime import datetime
from playsound import playsound

# alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
# print("Enter the time in 12 hour format")
# alarm_hour=alarm_time[0:2]
# alarm_minute=alarm_time[3:5]
# alarm_seconds=alarm_time[6:8]
# alarm_period = alarm_time[9:11].upper()
j = 1
alarm_hour = input("Enter Hour :- ")
alarm_minute = input("Enter Minute :- ")
alarm_seconds = input("Enter Second :- ")
alarm_period = input("Enter AM/PM :- ")

list1 = ['alarm_clock', 'morning_flower', 'nirvana']
print("")
for i in list1:
    print("{0}. {1}".format(j, i))
    j += 1
idx = int(input("\nChoose your alarm tone :- "))

print("=" * 40)
print("Alarm is set for {0}:{1}:{2} {3}".format(alarm_hour, alarm_minute, alarm_seconds, alarm_period))
print("=" * 40)
print('Your alarm tone is {}'.format(str(list1[idx - 1])) + '.mp3')
print("=" * 40)

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    print("Wake Up!")
                    playsound('{}'.format(str(list1[idx - 1])) + '.mp3')
                    break
