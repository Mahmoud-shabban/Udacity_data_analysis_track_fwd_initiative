#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


from random import shuffle


# In[3]:


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[4]:


class Card():
    
    def __init__(self,rank,suit):
        
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'
        


class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        for x in suits:
            for i in ranks:
                self.all_cards.append(Card(i , x))
    
    def length(self):
        return len(self.all_cards)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def del_card(self):
        return self.all_cards.pop()
    
    



def wining_check(ls):
    
    if len(ls) == 0 :
        return True
    else:
        return False



class Player():
    
    
    def __init__(self,name,player):
        self.name = name
        self.player = player
        
        if self.player == 'one':
            self.mycards1 = pocket1
        else:
            self.mycards2 = pocket2
    
    def __str__(self):
        return f'{self.name} is  player {slef.player}'
        
    def reveal(self):
        if self.player == 'one':
            return  self.mycards1.pop(0)
        else:
            return self.mycards2.pop(0)
            


# 
# # this is my war game completed and 100% working "my work_____with some cheating" !!!!!!!!!!!!!!!!!
# 
# 
# 

### this is my war game completed and 100% working "my work_____with some cheating" 


 ### this is my war game completed and 100% working "my work_____with some cheating" 


# this is the whole war game!!
                                               # the Game constants!


game_on = True

while game_on:
    
    print('Welcom to cards War Game')

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
                'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
    # the deck creat

    deck = Deck()
    deck.shuffle()

    # players pocket creat
    pocket2 = []
    pocket1 = []
    for x in range(26):
        pocket2.append(deck.del_card())
        pocket1.append(deck.del_card())

    


    play = True

    while play:

        player_1_name = input('player 1 Enter your name :  ')
        player_2_name = input('player 2 Enter your name:   ')

        player_one = Player(player_1_name,'one')
        player_1cards = player_one.mycards1

        player_two = Player(player_2_name,'two')
        player_2cards = player_two.mycards2

        rond = 0
        on = True

        while on:
 
            warlist = []
            war = False
            while not war:

                rond +=1
                print (f'round {rond}')

                to_check_1 = player_one.reveal()
                

                to_check_2 = player_two.reveal()
                   
                
                if to_check_1.value > to_check_2.value:
                    player_1cards.append(to_check_2)
                    player_1cards.append(to_check_1)
                    print('\nplayer One wins the round\n')

                    win = wining_check(player_2cards)
                    if win == True:
                        play = False
                        print('\nthis is the end!!  player "one" wins the Game!! \n')
                        on = False
                        break
                    else:
                        continue

                elif to_check_1.value < to_check_2.value:
                    player_2cards.append(to_check_1)
                    player_2cards.append(to_check_2)
                    print('\nplayer two wins the round\n')

                    win = wining_check(player_1cards)
                    if win == True:
                        play = False
                        print('\nthis is the end!!  player "Two" wins the Game !! \n')
                        on = False
                        break
                    else:
                        continue


                else:
                    print('\nthis is war\n')
                    
                    warlist.append(to_check_1)
                    warlist.append(to_check_2)
                    war = True
                    continue
                break

                                   # while War!!!!!!!!!!!!!!!!!!

            while war:

                win = wining_check(player_1cards)
                if win == True:
                    play = False
                    print('player 1 can"t complete the war \n this game ends at war \n player 2 wins the game!!!!')
                    on = False
                    break
                
                win = wining_check(player_2cards)
                if win == True:
                    play = False
                    print('player 2 can"t complete the war \n this game ends at war \n player 1 wins the game!!!!')
                    on = False
                    break
                else:
                    pass
                        
                to_check_1 = player_one.reveal()
                to_check_2 = player_two.reveal()

                # if player One wins the war

                if to_check_1.value > to_check_2.value:
                    print('\nthis is the end of war !!  player "one" wins the war!!\n ')
                    warlist.append(to_check_1)
                    warlist.append(to_check_2)
                    player_1cards.extend(warlist)
                    warlist = []

                    win = wining_check(player_2cards)
                    if win == True:
                        play = False
                        print('\nthis is the end !!  player "one" wins the Game!! \n')
                        on = False
                        play = False
                        break
                    else:
                        war = False
                        continue

                    # if player Two wins the war

                elif to_check_1.value < to_check_2.value:
                    print('\nthis is the end of war!!  player "two" wins the war!! \n')
                    warlist.append(to_check_1)
                    warlist.append(to_check_2)
                    player_2cards.extend(warlist)
                    warlist = []

                    win = wining_check(player_1cards)
                    if win == True:
                        play = False
                        on = False
                        print('\nthis is the end!!  player "one" wins the Game!!\n ')
                        break
                    else:
                        war = False
                        continue


                else:
                    print('\nthis war continues !!\n')
                    warlist.append(to_check_1)
                    warlist.append(to_check_2)
                    continue

    cont = input('you want to replay? Y/N : ')
    if cont == 'y':
        game_on = True
        continue
    else:
        game_on =False
    
    