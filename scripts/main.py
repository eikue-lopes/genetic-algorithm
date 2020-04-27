# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:06:51 2020

@author: eikue
"""
import pygame
from globals import *
from genetic_algorithm import GeneticAlgorithm
from jelly import Jelly
from functions import draw_graphics_evolve,calculate_economy_amount,update_evolve,start_graphics,save_best_dna
    
if __name__ == "__main__":

    if ENABLE_GRAPHICS:
        start_graphics()

    ga = GeneticAlgorithm(class_individual=Jelly,range_alels_individuals=range(-1000,1000),size_population=size_population,mutation_rate=mutation_rate,elitism=elitism)
    
    ga.create_initial_population()

    best_jelly , biggest_fitness = ga.return_best_individual_and_biggest_fitness()

    generation = 1

    while biggest_fitness < fitness_goal:

        print("GENERATION",generation)
        
        year = 1
    
        
        economy_amount = calculate_economy_amount(ga)
        
        average_fitness = ga.return_average_fitness()
        best_jelly , biggest_fitness = ga.return_best_individual_and_biggest_fitness()
              
        
        print("\nECONOMY AMOUNT IN GENERATION",generation,":",economy_amount)
        print("\nFITNESS AVERAGE IN GENERATION",generation,":",average_fitness)
        print("\nFITNESS BEST JELLY OF GENERATION",generation,"(JELLY HERITAGE):",biggest_fitness)
        print("\nAMOUNT GOLDS BEST JELLY OF GENERATION",generation,":",best_jelly.golds)
        print("AMOUNT HORSES BEST JELLY OF GENERATION",generation,":",best_jelly.horses)
        
    
        while year <= years:
            print("YEAR",year)
           
            if ENABLE_GRAPHICS:
                draw_graphics_evolve(ga,generation,year,biggest_fitness,average_fitness)
            
            
            update_evolve(ga)
            year += 1
            
            if ENABLE_GRAPHICS:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                        exit(0)        
    
    
        save_best_dna(generation,best_jelly.get_dna())

    
        ga.crossover()       
        ga.mutation()
    
        generation += 1
    
    

