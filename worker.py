# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:10:56 2022

@author: Admin
"""

class Person ():
    
    def __init__(self, first_name, last_name, age, intership):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.intership = intership
        
    def user (self):
        return self.first_name, self.last_name
        

class Department ():
    
    def __init__ (self, dept_name):
        self.dept_name = dept_name

class Interest ():
    def __init__(self, interest):
        self.interest = interest


class Worker (Person, Department, Interest):
    
    def __init__ (self, first_name, last_name, age, intership, dept_name, interest):
        Person.__init__(self, first_name, last_name, age, intership)
        Department.__init__(self, dept_name)
        Interest.__init__(self, interest)
        
user1 = Worker('Jan', 'Kowalski', 30, 2,'Dział Jakosci', 'yoga')
        

print (user1.__dict__)



class favorite_food (Person):
    
    def like (self):
        
        print (f'Ulubione danie {self.first_name}a {self.last_name}ego to spaghetti')
        
        print (super().user())
        
user1 = favorite_food('Jan', 'Kowalski', 30, 2)

user1.like()

class total (Person):
    
    def __init__(self, first_name, last_name, age, intership, food):
        super().__init__(first_name, last_name, age, intership)
        self.food = food
    
user1 = total('Jan', 'Kowalski', 30, 2, 'spaghetti')

print (user1.__dict__)
   
    
