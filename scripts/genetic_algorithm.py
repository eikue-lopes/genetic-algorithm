# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:33:50 2020

@author: eikue
"""

from random import randrange,random
       
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

        while one_selected == False:
            r1 = randrange((biggest_fitness))
            index = randrange(len(all_fitness))
            prob = all_fitness[index][1]
            if r1 < prob:
                one_selected = True
                return all_fitness[index][0], index
   
    def __matting_pool(self,all_fitness,biggest_fitness):
        times100 = False
        
        if biggest_fitness < 1:
            times100 = True
            
        bucket = []
        for fitness in all_fitness:
            if times100 == True:
                fit_value = fitness[1] * 100.00
            else:
                fit_value = fitness[1]
                
            bucket = bucket + [fitness[0]] * fit_value
            
        random_index = randrange(len(bucket))
        return bucket[random_index] , random_index
   
    def __pick_one(self,all_fitness,biggest_fitness):
        normalize = False
        
        if biggest_fitness > 1.0:
            normalize = True
            
        index = 0
        
        if normalize == True:
            sum_fitness = sum([f[1] for f in all_fitness])
            
        probabilitie = random()

        while probabilitie > 0.0:

            if normalize == True:
                fit_value = all_fitness[index][1] / sum_fitness
           
            else:
                fit_value = all_fitness[index][1]
            
            probabilitie = probabilitie - fit_value
            index += 1
            
        index -= 1
        return all_fitness[index][0] , index
            
    def __select_two_parents(self,all_fitness,biggest_fitness,method='pick-one'):
        dad = None
        mom = None
        
        if method == 'accept-reject':        
            dad,index_dad = self.__accept_reject(all_fitness,biggest_fitness)
        
            while True:
                mom,index_mom = self.__accept_reject(all_fitness,biggest_fitness)
          
                if index_mom != index_dad:
                    break
       
        elif method == 'matting-pool':
            dad,index_dad = self.__matting_pool(all_fitness,biggest_fitness)
        
            while True:
                mom,index_mom = self.__matting_pool(all_fitness,biggest_fitness)
          
                if index_mom != index_dad:
                    break 
        else:
            dad,index_dad = self.__pick_one(all_fitness,biggest_fitness)
        
            while True:
                mom,index_mom = self.__pick_one(all_fitness,biggest_fitness)
          
                if index_mom != index_dad:
                    break             
       
        return dad,mom
                
    def evaluation(self):
        all_fitness = [( individual , individual.fitness() ) for individual in self.population]
        return all_fitness
        
    def selection(self,all_fitness,method='pick-one'):
        selecteds = []

        _ , biggest_fitness = self.return_best_individual_and_biggest_fitness(all_fitness)

        num_couples = self.size_population
       
        if self.elitism == True:
            num_couples -= 1
 
        for i in range(num_couples):
            dad,mom = self.__select_two_parents(all_fitness , biggest_fitness,method=method)
            selecteds.append( (dad , mom) )
            
        return selecteds
            
    def crossover(self,all_fitness,selecteds):
        new_population = []
        print("CROSSOVER")
        
        best_individual , _ = self.return_best_individual_and_biggest_fitness(all_fitness)
        
        if self.elitism == True:
            dna_best = best_individual.get_dna()
            best = self.class_individual()
            best.set_dna(dna_best)
            new_population.append(best)

        for couple_selected in selecteds:
            dad,mom = couple_selected[0] , couple_selected[1]
            dad_dna = dad.get_dna()
            mom_dna = mom.get_dna()
            
            crossover_point = randrange(1 , len(dad_dna) - 1 )

            son = self.class_individual()
            
            crossed_genes = dad_dna[:crossover_point] + mom_dna[crossover_point:]
            son.set_dna(crossed_genes)
            
            new_population.append(son)

            
        self.population = list(new_population)
        #print("END CROSSOVER")
    def mutation(self):
        for i in range(self.size_population):
            number_drawn = random()
            
            if number_drawn <= self.mutation_rate:
                
                if self.elitism == True:
                    individual_index_drawn = randrange(1,self.size_population)
                else:
                    individual_index_drawn = randrange(0,self.size_population)
                
                dna = self.population[ individual_index_drawn ].get_dna()
                
                dna_index_drawn = randrange( len(dna) )
                
                random_alel =  self.range_alels_individuals[ randrange( len(self.range_alels_individuals) ) ]
                dna[dna_index_drawn] = random_alel
                
                self.population[ individual_index_drawn ].set_dna(dna) 
                
                print("MUTATION IN",individual_index_drawn,"!")
    
    def return_average_fitness(self,all_fitness):
        #print("AVERAGE")
        
        average_fitness = sum([ fitness[1] for fitness in all_fitness ]) / self.size_population
        #print("END AVERAGE")
        return average_fitness
        
    def return_best_individual_and_biggest_fitness(self,all_fitness):
        #print("BIGGESTBEST")
    
        biggest_fitness = all_fitness[0]
        
        for fitness in all_fitness:
            if biggest_fitness[1] < fitness[1]:
                biggest_fitness = fitness
                
        #print("END BIGGESTBEST")
        return biggest_fitness[0] , biggest_fitness[1] 
    
