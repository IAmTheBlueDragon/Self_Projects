# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 17:27:40 2022

@author: Lenovo
"""
'''
Q1)
Chef has recently been playing a lot of chess in preparation for the ICCT (International Chef Chess Tournament).

Since putting in long hours is not an easy task, Chef's mind wanders elsewhere. He starts counting the number of squares with odd side length on his chessboard..

However, Chef is not satisfied. He wants to know the number of squares of odd side length on a generic N*NN∗N chessboard.
'''
def pcj18b():
    t= int(input())
    for i in range(t):
        n=int(input())
        s=0
        j=1
        while j<=n:
            s+=(n-j+1)**2
            j+=2
        print(s)

'''
Q2)
In an attempt to reduce the growing population, Archer was asked to come up with a plan. Archer being as intelligent as he is, came up with the following plan:

If NN children, with names C_{1}, C_{2}, ... , C_{N}C 
1
​
 ,C 
2
​
 ,...,C 
N
​
 , are born to parents with names AA and BB, and you consider CC to be the concatenation of all the names of the children, i.e. C = C_{1} + C_{2} + ... + C_{N}C=C 
1
​
 +C 
2
​
 +...+C 
N
​
  (where ++ is concatenation operator), then CC should be a substring of one of the permutations of A + BA+B.

You are given the task to verify whether the names parents propose to give their children are in fact permissible by Archer's plan or not.
'''
def name1():
    t=int(input())
    for i in range(t):
        l=list(input())
        l.remove(" ")
        n=int(input())
        bol=0
        for j in range(n):
            tl=l
            nl=list(input())
            bol=0
            for k in nl:
                if bol==0:
                    if k in tl:
                        tl.remove(k)
                    else:
                        bol+=1
                        break
                else:
                    break
        if bol==0:
            print("YES")
        else:
            print("NO")
        

from itertools import combinations
t=int(input())
for i in range(t):
    l=list(map(int,input().split(" ")))
    n=[]
    for j in range(l[0],l[1]+1):
        n.append(j)
    print(n)
    s=[n*2 for n in range(l[0],l[1]+1)]
    print(s)
    for i in list(combinations(n,2)):
        if sum(i) not in s:
            print(sum(i))
            s.append(sum(i))
    print(len(s))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    