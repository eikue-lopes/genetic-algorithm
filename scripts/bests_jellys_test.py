# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:06:51 2020

@author: eikue
"""
import pygame
from globals import *
from time import sleep
from functions import start_graphics,load_best_dna_saved,draw_graphics_test,update_test
from jelly import Jelly
    
if __name__ == "__main__":


    if ENABLE_GRAPHICS:
        start_graphics()
        
       
    best_dna = load_best_dna_saved()
    print(best_dna)
        
    jelly = Jelly()
    jelly.set_dna(best_dna)
    print("Jelly INFOS::",jelly.golds,jelly.horses)
    
    year = 0    
 
    while year < years:
        print("\nYEAR",year)
        
        if ENABLE_GRAPHICS:
            draw_graphics_test(jelly,year)
                
        update_test(jelly,year)

        year += 1
           
        if ENABLE_GRAPHICS:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

        sleep(0.5)
        
        print("\n\nJELLY HERITAGE (FITNESS):",jelly.fitness())
        print("AMOUNT GOLDS JELLY:",jelly.golds)
        print("AMOUNT HORSES JELLY:",jelly.horses)
        
        sleep(1)
