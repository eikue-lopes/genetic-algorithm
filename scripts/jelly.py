# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:26:32 2020

@author: eikue
"""

from random import randint
from globals import *
from nna import NeuralNetworkArtificial as NNA
from nna import relu
import shelve

class Jelly:
    def __init__(self,happiness=initial_happiness_jellys,health=initial_health_jellys,nutrition=initial_nutrition_jellys,golds=initial_golds_jellys,horses=initial_horses_jellys):
        global brain_structure_jelly
        self.brain = NNA(num_inputs=5,structure_layers=brain_structure_jellys,activate_function=relu,outputs_aliases=['buy-horses','sell-horses','buy-health','buy-nutrition','buy-happiness'])
        
        self.happiness = happiness
        self.health = health
        self.nutrition = nutrition
        self.golds = golds
        self.horses = horses

        self.posx = randint(spawn_place_posx,(spawn_place_posx + spawn_place_width) - jelly_width)
        self.posy = randint(spawn_place_posy,(spawn_place_posy + spawn_place_height) - jelly_height)
    

    def fitness(self):
        fitness = self.golds + (self.horses * sell_price_horse)
        print("Fitness:",fitness)
        return fitness
        
    def get_dna(self):
        return self.brain.get_weights_nna()
        
    def set_dna(self,dna):
        self.brain.set_weights_nna(dna)


    def draw(self,screen,surface_sprite_image):
        screen.blit(surface_sprite_image,(self.posx,self.posy))

    def get_and_translate_jelly_response(self):
    
        inputs_jelly = [self.happiness,self.health,self.nutrition,self.golds,self.horses]
        jelly_response = self.brain.resolve(inputs=inputs_jelly)
        keys = list(jelly_response.keys())
        values = list(jelly_response.values())
        biggest_answer = max(values)
        key_biggest_answer = keys[values.index(biggest_answer)]
        #print(jelly_response)
        #print(key_biggest_answer)
        #print(jelly_response[key_biggest_answer])
        return key_biggest_answer
    
