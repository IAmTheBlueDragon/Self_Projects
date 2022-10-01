# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:40:47 2021

@author: Lenovo
"""

class Account():
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def deposit(self,ammount):
        self.balance+=ammount 
    
    def withdraw(self,ammount):
        if ammount<=self.balance:
            self.balance-=ammount
            
        else:
            print("Insufficient Funds")
            
    