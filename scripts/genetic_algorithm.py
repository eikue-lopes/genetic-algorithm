# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:33:50 2020

@author: eikue
"""

from random import randrange
       
class GeneticAlgorithm:
    def __init__(self,class_individual,range_alels_individuals,size_population,mutation_rate,elitism):
        self.range_alels_individuals = range_alels_individuals
        self.class_individual = class_individual
        self.size_population = size_population
        self.mutation_rate = mutation_rate
        self.elitism = elitism
        self.population = []
    
    def create_initial_population(self):
        self.population = [self.class_individual() for i in range(self.size_population)]
        
        
    def __accept_reject(self,all_fitness,biggest_fitness):
        one_selected = False
        exp = 4
        while one_selected == False:
            r1 = randrange((biggest_fitness ** exp))
            index = randrange(len(all_fitness))
            prob = all_fitness[index][1] ** exp
            if r1 < prob:
                one_selected = True
                return all_fitness[index][0], index

    def __select_two_parents(self,all_fitness,biggest_fitness):
        
        dad,index_dad = self.__accept_reject(all_fitness,biggest_fitness)
        
        while True:
            mom,index_mom = self.__accept_reject(all_fitness,biggest_fitness)
          
            if index_mom != index_dad:
                break

        return dad,mom        
        
         
    def crossover(self):
        new_population = []
        print("CROSSOVER")
        all_fitness = [( individual , individual.fitness() ) for individual in self.population]
        
        best_individual , biggest_fitness = self.return_best_individual_and_biggest_fitness()
        
        if self.elitism == True:
            new_population.append(best_individual)
            index_start = 1
        else:
            index_start = 0

        for i in range(index_start,self.size_population):
            dad,mom = self.__select_two_parents(all_fitness , biggest_fitness)
            dad_dna = dad.get_dna()
            mom_dna = mom.get_dna()
            
            slice_point = len(dad_dna) // 2

            son = self.class_individual()
            
            crossed_genes = dad_dna[:slice_point] + mom_dna[slice_point:]
            son.set_dna(crossed_genes)
            
            new_population.append(son)
            
        self.population = list(new_population)
        #print("END CROSSOVER")
    def mutation(self):
        for i in range(self.size_population):
            number_drawn = randrange(100)
            
            if number_drawn <= int(self.mutation_rate * 100):
                
                if self.elitism == True:
                    individual_index_drawn = randrange(1,self.size_population)
                else:
                    individual_index_drawn = randrange(0,self.size_population)
                
                dna = self.population[ individual_index_drawn ].get_dna()
                
                dna_index_drawn_start = randrange(len(dna) // 2)
                dna_index_drawn_end = randrange(len(dna) // 2 , len(dna))
                
                for index in range(dna_index_drawn_start,dna_index_drawn_end):
                    random_alel =  self.range_alels_individuals[ randrange( len(self.range_alels_individuals) ) ]
                    dna[index] = random_alel
                
                self.population[ individual_index_drawn ].set_dna(dna) 
                print("MUTATION IN",individual_index_drawn,"!")
    
    def return_average_fitness(self):
        #print("AVERAGE")
        all_fitness = [( individual , individual.fitness() ) for individual in self.population]
        average_fitness = sum([ fitness[1] for fitness in all_fitness ]) / self.size_population
        #print("END AVERAGE")
        return average_fitness
        
    def return_best_individual_and_biggest_fitness(self):
        #print("BIGGESTBEST")
        all_fitness = [( individual , individual.fitness() ) for individual in self.population]

        biggest_fitness = all_fitness[0]
        
        for fitness in all_fitness:
            if biggest_fitness[1] < fitness[1]:
                biggest_fitness = fitness
                
        #print("END BIGGESTBEST")
        return biggest_fitness[0] , biggest_fitness[1] 
    
