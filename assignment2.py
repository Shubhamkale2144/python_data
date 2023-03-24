# -*- coding: utf-8 -*-
"""
Create a Vehicle class which has the following instance attributes: color(string), 
type_of_vehicle(string), year_of_market_release(int) and the following class attributes: wheels(int) , 
no_of_doors(int) and the following methods: changeColor, describeVehicle(print all the attributes), 
brakeCar(print the attributes along with “braking”) and startCar (print the attributes along with “starting”)
"""
class Vehicle:
    wheels = 4
    no_of_doors = 4
    def __init__(self, color, type_of_vehicle, year_of_market_release):
        self.color = color
        self.type_of_vehicle = type_of_vehicle
        self.year_of_market_release = year_of_market_release
        
        
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        if color == 'White':
            self.color=color
            print('\tColor changed')
        else:
            print('\tNot allowed')
            
    def describeVehicle(self):
        print(self.color,'\t', self.type_of_vehicle,'\t', self.year_of_market_release, '\t', self.wheels, '\t', self.no_of_doors)

    def brakeCar(self):
        self.describeVehicle()
        print('\tBraking')
        
    def startCar(self):
        self.describeVehicle()
        print('\tStarting')
        
veh1=Vehicle("black","car",2011)
veh1.describeVehicle()
veh1.brakeCar()
veh1.startCar()
veh2=Vehicle('White','Car',2010)
veh2.describeVehicle()
veh2.set_color('White')
veh2.brakeCar()
veh2.startCar()   

    

"""
Create a dictionary for Vehicle objects in which the objects having the same value for 
“year_of_market_release” are grouped together with the key being the year_of_market_release and the value being 
the list of objects having the attribute year_of_market_release equal
"""
v1 = Vehicle("Red", "BMW", 2012)
v2 = Vehicle("blue", "audi", 2013)
v3 = Vehicle("yellow", "honda", 2012)
v4 = Vehicle("black", "ford", 2013)
list1 = [v1,v2,v3,v4]
dict1={}
for i in list1:
    #print(i.year_of_market_release)
    if i.year_of_market_release in dict1.keys():
        dict1[i.year_of_market_release].append(i)
    else:
        dict1[i.year_of_market_release]=[i]
for key,value in dict1.items():
    print("\n",key," : ",end = " ")
    for item in value:
        print(item.type_of_vehicle, end =" ")

"""
Create a class Plate that has a method called add_to_plate(), remove_from_plate() and
display_items_on_plate(). The Plate object will initially be empty and have an attribute called items_on_plate which should 
be a list and whenever add_to_plate() is called with an item argument which is a string, add that item to the items_on_plate, 
similarly if remove_from_plate() is called with an item, if that item is present in items_on_plate remove it, else print “Item
not on plate” and whenever display_items_on_plate() is called, print the list items_on_plate.

"""
print("\n")
class plate:
    def __init__(self):
        self.items_on_plate =[]
    def add_to_plate(self,item):
        self.items_on_plate.append(item)
    def remove_from_plate(self,item):
        self.items_on_plate.remove(item)
    def display_items_on_plate(self):
        print(self.items_on_plate)

p= plate()
p.add_to_plate("palak_paneer")
p.display_items_on_plate()
p.remove_from_plate("palak_paneer")
p.display_items_on_plate()