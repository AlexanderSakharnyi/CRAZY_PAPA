#from inp16 import *

vyb = 1
ppr = 1

def rectangle1 ():
	global ppr, spr, vpr
	ppr = round(spr * vpr, 2)

if vyb == 1:
	print ("введите ширину прямоугольника: ")
	spr = float(input())
	print ("введите высоту прямоугольника: ")
	vpr = float(input())
	rectangle1 ()
	print ("S прямоугольника: " ,ppr)

print ("ZEU!")