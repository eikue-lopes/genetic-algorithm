# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:06:51 2020

@author: eikue
"""
import pygame
from globals import *
import sys
from time import sleep
from functions import start_graphics,execute_order_jelly,load_best_dna_saved,draw_graphics_test,update_test
from jelly import Jelly
    
if __name__ == "__main__":

   

    if ENABLE_GRAPHICS:
        start_graphics()
        
    years = int(sys.argv[1])
    generation = int(sys.argv[2])


    while generation <= int(sys.argv[3]):
        
        best_dna = load_best_dna_saved(generation)
        jelly = Jelly()
        jelly.set_dna(best_dna)

        print("\nGENERATION",generation)
    
        year = 1    
 
        while year <= years:
            print("\nYEAR",year)
        
            if ENABLE_GRAPHICS:
                draw_graphics_test(jelly,generation,year)
                
            update_test(jelly)

            year += 1
           
            if ENABLE_GRAPHICS:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                        exit(0)

            sleep(0.5)
        
        print("\n\nJELLY HERITAGE IN GENERATION",generation,"(FITNESS):",jelly.fitness())
        print("AMOUNT GOLDS JELLY:",jelly.golds)
        print("AMOUNT HORSES JELLY:",jelly.horses)

        generation += 1
            
        sleep(1)
