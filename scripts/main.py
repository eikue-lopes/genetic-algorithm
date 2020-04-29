# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:17:10 2020

@author: eikue
"""
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

    ga = GeneticAlgorithm(class_individual=Jelly,range_alels_individuals=range(1,5+1),size_population=size_population,mutation_rate=mutation_rate,elitism=elitism)
    
    ga.create_initial_population()

    all_fitness = ga.evaluation()
    
    best_jelly , biggest_fitness = ga.return_best_individual_and_biggest_fitness(all_fitness)

    generation = 1

    while biggest_fitness < fitness_goal:

        print("GENERATION",generation)
        
        year = 0
  
        average_fitness = ga.return_average_fitness(all_fitness)
        best_jelly , biggest_fitness = ga.return_best_individual_and_biggest_fitness(all_fitness)
         
        while year < years:
            print("YEAR",year)
           
            if ENABLE_GRAPHICS:
                draw_graphics_evolve(ga,generation,year,biggest_fitness,average_fitness)
            
            
            update_evolve(ga,year)
            year += 1
            
            if ENABLE_GRAPHICS:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                        exit(0)        
     
        #STEPS TO EVOLVE
        
        all_fitness = ga.evaluation()

        couple_selecteds = ga.selection(all_fitness=all_fitness , method='pick-one')

        ga.crossover(all_fitness=all_fitness , selecteds=couple_selecteds)       

        ga.mutation()
    
        generation += 1
    
    
    save_best_dna(best_jelly.get_dna())   
    

    

