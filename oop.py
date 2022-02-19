# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:05:19 2022

@author: Amlan Ghosh
"""

class Student:
    
    '''class variable'''
    full_marks = 100
    
    '''instance variable'''
    def __init__(self,subject_1,subject_2):
        self.subject_1 = subject_1
        self.subject_2 = subject_2
        
    '''instance method: using instance variables'''
    def total_marks(self):
        print (self.subject_1 + self.subject_2)
        return self.subject_1 + self.subject_2
    
    '''class method: using class/static variables'''
    @classmethod
    def get_full_marks(cls):
        return cls.full_marks
    
    def percentage(self):
        print (self.total_marks()/Student.full_marks*50)
    
    '''static method: no need of instance or class variables'''
    @staticmethod
    def remarks():
        print ('Should Have Done Better')

amlan = Student(82,96)
ayon = Student(85,95)

amlan.total_marks()
ayon.total_marks()

print ('Amlan ' + str(amlan.full_marks))
print ('Ayon ' + str(ayon.full_marks))

amlan.percentage()
ayon.percentage()

amlan.remarks()
ayon.remarks()
