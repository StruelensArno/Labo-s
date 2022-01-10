#voorbeeld math
import math

#de waarde pi is niet standaard in python daarom haal je het uit een library zoals math
print(f"de waarde PI is {math.pi}")
#zo kan je zien wat allemaal extra meekomt me de library 'math'
print(dir(math))

#je kan ook specifieke zaken uit de library halen door from te gebruiken 
from math import pi

#voorbeeld versie python
from sys import version, version_info
print(version)
print(version_info)

#voorbeeld data
from datetime import date
print(date.today())