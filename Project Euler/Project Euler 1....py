# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 22:50:46 2021

Project Name: Euler

@author: Shreyas Om
"""
def sum_of_3_and_5(Enter_limit):
    x=Enter_limit
    s=0
    for i in range(x):
        if i%3==0 or i%5==0:
            s+=i
            
    return(s)

def even_fibbonacci(Enter_limit):
    x=Enter_limit
    s=0
    i=1
    prev=0
    temp=0
    while i<x:
        temp=i
        i+=prev
        prev=temp
        if i%2==0:
            s+=i
    return(s)

def large_prime(Enter_Number):       
    x=Enter_Number
    i=int(x**(1/2))
    while i>1:
        if x%i==0 and check_prime(i)==True:
            return(i)
        else:
            i-=1
            
def check_prime(n):
    if type(n)!=int:
        return False
    t=True
    i=2
    while i<=n**(1/2):
        if n%i==0:
            t=False
        if i==2:
            i=i+1
        else:
            i=i+2
    return(t)

def factors(x):
    l=[]
    i=2
    while i<=x:
        if x%i==0 and check_prime(i)==True:
            l.append(i)
            i=i+1
        else:
            i=i+1
    return(l)
            

def smallest_multiple(x):
    l=[]
    for i in range(x):
        l=l+factors(x)
    s=set(l)
    return(s)
