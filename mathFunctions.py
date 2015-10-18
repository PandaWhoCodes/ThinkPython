""" If you run 10 Kilometer race in just 43 minutes and 30 seconds  what is your average time in
 miles per hour? Hint: 1.6 Kilometers=1 mile
"""
# speed= distance/time
distance = 10
# converting time into seconds
time = (43 * 60) + 30
# converting time into hours
time = time / 360
speed = distance / time
print("Speed in kiometers:" + str(speed))
Mspeed = speed / 1.6
print("Speed in Miles:" + str(Mspeed))
