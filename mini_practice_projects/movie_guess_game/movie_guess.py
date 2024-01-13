# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:08:45 2024

@author: 9429249905
"""

import pandas as pd
import numpy as np


def make_guesses(mov, points, blank_movie):
    while "_" in blank_movie and points>0:
        print(f"\nChances Left : {points}")
        print("\n", " ".join(blank_movie))
        guess = input("Guess the charecters of movie : ")

        if guess in mov:
            count  = mov.count(guess)
            
            while count:
                location = mov.index(guess)
                blank_movie[location] = guess
                mov[location] = "_"
                count -= 1
                
        else:
            print("Wrong guess.")
            points -= 1
    return points


def blank_list(movie):
    return list(["_" if char!=" " else " " for char in movie])
    

def play():
    player1 = input("\nPlayer 1 name : ")
    player2 = input("Player 2 name : ")
    p1_points = 0
    p2_points = 0
    turn = 0
    willing = True
    
    while willing:
        movie  = np.random.choice(movie_list).lower()
        chances = 10
        print(movie)
        
        
        if turn%2 == 0:
            print(f"\n{player1}, your turn.")
            mov = list(movie)
            blank_movie = blank_list(movie)
    
            chances = make_guesses(mov, chances, blank_movie)
            turn += 1
            print(f"\nMovie : {movie}")
            if chances>0:
                p1_points += 1
                print("\nYou win!")
                print(f"{player1} score : {p1_points}\n")
            else:
                print("\nYou lose.")
                
        else:
            print(f"\n{player2}, your turn.")
            mov = list(movie)     
            blank_movie = blank_list(movie)
    
            chances = make_guesses(mov, chances, blank_movie)
            turn += 1
            print(f"\nMovie : {movie}")
            if chances>0:
                p2_points += 1
                print("\nYou win!")
                print(f"{player2} score : {p2_points}\n")
            else:
                print("\nYou lose.")
        
                
        if int(input("Keep playing? type any key to continue or 0 to exit : ")) == 0:
            willing = False
            
    print(f"Final scoes.")
    print(f"{player1} : {p1_points}")
    print(f"{player2} : {p2_points}")


# Driver code
whole_data = np.array(pd.read_csv("C:/Users/91942/Downloads/BollywoodMovieDetail.csv"))
movie_list = (whole_data[0:-1, 1])

play()

