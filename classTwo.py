#Function to conpute the area of a triangle
def AreaOfTriangle(base,height):
	area=(1.0/2)*base*height
	return area 

a1=AreaOfTriangle(3,8)
print a1

#Function that convert faranheight to celcius
def faranheightTocelsius(faranheight):
	celcius= (5.0/9)*(faranheight-32)
	return celcius
c1=faranheightTocelsius(32)
print c1

#Function to convert from celciustokelvin
def fareinhihttokelvin(faranheight):
	celcius=faranheightTocelsius(faranheight)
	kelvin=celcius+273.15
	return kelvin
k1=fareinhihttokelvin(212)
print k1

#Function to print hello world
def hello():
	print "hello world"

#Function to print my name
def hello():
	print "hello world"

hello()
import math
#import simplegui
import random 
a=math.pi 
print "the value of pi is "+ str(a) #convert the value of pi to strings, so that it can be concatinated
