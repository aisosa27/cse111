import math
import datetime
now = datetime.datetime.now()
print (now.strftime("%y-%m-%d "))
#Do this for each of the variables we are to find int he shape/equation
width = float(input('Enter the width of the tire in mm (ex 205): '))
ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))
#split the equation into different lines to make it easier on yourself.
radical = (2540 * diameter + width * ratio)
radical_2 = (math.pi * width**2 * ratio)
volume = ((radical * radical_2) / 10000000000)
#This line round the decimal to the 2nd place so the don't have an extremely long number
volume = round(volume, 2)
print()
print(f'The approximate volume is {volume} liters.')
#I used a direct path to the file as the volumes.txt would not sync.
#The following code as the required data to the volumes.txt file.
with open('/Users/doubradaunemigha/Desktop/CSE 111/volumes.txt', 'at') as volumes_file:
    print(f'{now}, {width}, {ratio}, {diameter}, {volume}', file=volumes_file)