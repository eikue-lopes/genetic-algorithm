# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:12:30 2020

@author: eikue
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:26:32 2020

@author: eikue
"""

from random import randint
from globals import *


class Jelly:
    def __init__(self,happiness=initial_happiness_jellys,health=initial_health_jellys,nutrition=initial_nutrition_jellys,golds=initial_golds_jellys,horses=initial_horses_jellys):
        global years
        self.dna = [randint(1,5) for i in range(years)]
        self.happiness = happiness
        self.health = health
        self.nutrition = nutrition
        self.golds = golds
        self.horses = horses

        self.posx = randint(spawn_place_posx,(spawn_place_posx + spawn_place_width) - jelly_width)
        self.posy = randint(spawn_place_posy,(spawn_place_posy + spawn_place_height) - jelly_height)
    

    def fitness(self):
        fitness = (self.golds + (self.horses * sell_price_horse))
        print("Fitness:",fitness)
        return fitness
        
    def get_dna(self):
        return self.dna
        
    def set_dna(self,dna):
        self.dna = list(dna)


    def draw(self,screen,surface_sprite_image):
        screen.blit(surface_sprite_image,(self.posx,self.posy))

    def get_and_translate_jelly_response(self,current_year):
        response = self.dna[current_year]
        #'buy-horses','sell-horses','buy-health','buy-nutrition','buy-happiness'
        if response == 1:
            return 'buy-horses'
        elif response == 2:
            return 'sell-horses'
        elif response == 3:
            return 'buy-health'
        elif response == 4:
            return 'buy-nutrition'
        elif response == 5:
            return 'buy-happiness'
    
    def execute_order_jelly(self,translated_response):
        
        average_attributes_jelly = (self.happiness + self.health + self.nutrition) // 3
        
        if translated_response == 'sell-horses':
            sell_horses_permission = average_attributes_jelly
            if self.horses >= sell_horses_permission:
                self.golds += (sell_horses_permission * sell_price_horse)
                self.horses -= sell_horses_permission
            else:
               self.golds += (self.horses * sell_price_horse)
               self.horses = 0
               
            self.posx = (sell_horses_place_posx + jelly_width // 2)
            self.posy = (sell_horses_place_posy + randint(0,70) + jelly_height // 2)  
            
        elif translated_response == 'buy-horses':
            buy_horses_permission = average_attributes_jelly
    
            if self.golds >= (buy_horses_permission * buy_price_horse):
               self.horses += buy_horses_permission
               self.golds -= (buy_horses_permission * buy_price_horse)
            else:
               self.horses += (self.golds // buy_price_horse)
               self.golds -= (self.golds // buy_price_horse) * buy_price_horse
               
            self.posx = (buy_horses_place_posx + randint(0,40) + jelly_width // 2)
            self.posy = (buy_horses_place_posy + randint(0,40) + jelly_height // 2)
            
        elif translated_response == 'buy-nutrition':
            buy_nutrition_permission = 100.0 - self.nutrition
    
            if self.golds >= (buy_nutrition_permission * buy_price_unit_nutrition):
                self.nutrition += buy_nutrition_permission
                self.golds -= (buy_nutrition_permission * buy_price_unit_nutrition)
    
            else:
                self.nutrition += self.golds // buy_price_unit_nutrition
                self.golds -= (self.golds // buy_price_unit_nutrition) * buy_price_unit_nutrition
    
                
            self.posx = (nutrition_place_posx + randint(0,40) + jelly_width // 2)
            self.posy = (nutrition_place_posy + randint(0,40) + jelly_height // 2)
            
        elif translated_response == 'buy-health':
            buy_health_permission = 100.0 - self.health
    
            if self.golds >= (buy_health_permission * buy_price_unit_health):
                self.health += buy_health_permission
                self.golds -= (buy_health_permission * buy_price_unit_health)
    
            else:
                self.health += self.golds // buy_price_unit_health
                self.golds -= (self.golds // buy_price_unit_health) * buy_price_unit_health
                
            self.posx = (health_place_posx + randint(0,40) + jelly_width // 2)
            self.posy = (health_place_posy + randint(0,40) + jelly_height // 2)
            
        elif translated_response == 'buy-happiness':
            buy_happiness_permission = 100.0 - self.happiness
            
            if self.golds >= (buy_happiness_permission * buy_price_unit_happiness):
                self.happiness += buy_happiness_permission
                self.golds -= (buy_happiness_permission * buy_price_unit_happiness)
            else:
                self.happiness += self.golds // buy_price_unit_happiness
                self.golds -= (self.golds // buy_price_unit_happiness) * buy_price_unit_happiness   
    
            self.posx = (happiness_place_posx + randint(0,40) + jelly_width // 2)
            self.posy = (happiness_place_posy + randint(0,40) + jelly_height // 2)
      
