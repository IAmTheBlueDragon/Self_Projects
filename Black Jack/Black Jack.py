# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:42:03 2021

@author: Lenovo
"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':[1,11]}

#This class creates a deck of all cards with each card havinf there own values and attributes
class Deck():
    def __init__(self):
        self.all_cards = [] #A list to hold all the cards
        
        for suit in suits:
            for rank in ranks:
                #Create the card object
                created_card = Card(suit, rank)
                #append the card object into the all cards list
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards) #Shuffling all the cards
    
    def deal_one(self):
        return(self.all_cards.pop()) #To get the first card of the deck and remove from the list
    
    '''
        eg:
            new_deck=Deck()
            new_deck.shuffle()
            new_deck.deal_one()
    ''' 
    
#This class is to intialize or create card for the game
class Card():
    def __init__(self,suit,rank):
        self.suit=suit      #Suit of the card
        self.rank=rank      #Rank of the card
        self.value=values[rank] #Integer value of the card
        
    def __str__(self):
        return(self.rank+"of"+self.suit)    #Prints the identitiy of the card
        
    '''
    eg:
        two_of_hearts = Card("Hearts","Two")
    '''
    
#This is the class for the dealer for the game
class Computer():    
    def __init__(self):
        self.cards = []     #Initializes a list to the hand of cards existing
        
    def hit(self,card):
        self.cards.append(card)     #Add A card at the end of the cards in computers hand

    def hand_value(self):       #The value of total no. of the cards in the computers hand
        s=0
        for i in self.cards:
            if i.rank!='Ace':
                s+=i.value
            else:
                if 21-s>11:
                    s+=11
                else:
                    s+=1
        return(s)
    
    def show_hand_value(self):
        s=0
        for i in self.cards[:-1]:
            if i.rank!='Ace':
                s+=i.value
            else:
                if 21-s>11:
                    s+=11
                else:
                    s+=1
        return(s)
    
    
    def show_hand(self):
        l=[]
        for i in self.cards[:-1]:
            l.append(str(i))
            
        return(l)
    
    '''
        eg:
            computer=Computer()
    '''
    
#This is the class for the player which inherits many attribites from the computer class  
class Player(Computer):
    def __init__(self,balance):
        self.cards = []
        self.balance = balance
        self.bet = 0
        
    def betting(self,bet_amount):
        if bet_amount>self.balance:
            return("Insufficient Balance")
        else:
            self.bet+=bet_amount
            self.balance-=bet_amount
            
    '''
        eg:
            player_one=Player(10000)
    '''

new_deck=Deck()
new_deck.shuffle()
computer=Computer()
computer=Computer()
player_one=Player(10000)
bet=int(input("Enter the bet amount: "))
player_one.betting(bet)
if player_one.bet!=0:
    for i in range(2):
        player_one.hit(new_deck.deal_one())
        computer.hit(new_deck.deal_one())  
        
game_on=True

while game_on:          
        player_plays=True
        print("Computer Hand: ",computer.show_hand())
        while player_plays:
            print(player_one.hand_value())
            if player_one.hand_value()>21:
                print("Busted! Player looses")
                player_one.bet=0
                player_plays=False
                game_on=False
                break            
            else:
                move=input("Hit or Hold: ")
                if move=='Hold':
                    player_plays==False
                    break
                else:
                    player_one.hit(new_deck.deal_one())
        
        computer_plays=True
        while computer_plays and game_on:
            if computer.hand_value()>21:
                print("Busted! Player wins")
                player_one.balance+=(2*player_one.bet)
                player_one.bet=0
                computer_plays=False
                game_on=False
                break
            else:
                if computer.hand_value()<player_one.show_hand_value():
                    computer.hit(new_deck.deal_one())
                else:
                    computer_plays=False
                    break
                
        if game_on:
            if player_one.hand_value()<computer.hand_value():
                print("Player:",str(player_one.hand_value()),"Computer:",str(computer.hand_value()))
                print("Player looses!")
                player_one.bet=0
                game_on=False
                break
            elif player_one.hand_value()>computer.hand_value():
                print("Player:",str(player_one.hand_value()),"Computer:",str(computer.hand_value()))
                print("Player wins!")
                player_one.balance+=(2*player_one.bet)
                player_one.bet=0
                game_on=False
                break
            else:
                print(f"Player:{player_one.hand_value()} Computer:{computer.hand_value()}")
                print("Draw")
                player_one.balance+=(player_one.bet)
                player_one.bet=0
                game_on=False
                break

print(f'Player Balance is {player_one.balance}')