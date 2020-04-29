# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:23:20 2020

@author: eikue
"""
from random import randint
import pygame
from globals import *
import shelve

def start_graphics():
    global screen,screen_width,screen_height,jelly_sprite_image
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height)) 
    jelly_sprite_image = pygame.image.load(DIR_JELLY_IMAGE)
    
def draw_graphics_evolve(ga,generation,year,fitness_best_jelly_of_generation,average_fitness):
    global screen,jelly_sprite_image,mutation_rate,size_population,fitness_goal,elitism
    
    screen.fill(bg_color)
    screen.fill(bg_color_spawn_place,spawn_place)
    screen.fill(bg_color_buy_horses_place,buy_horses_place)
    screen.fill(bg_color_nutrition_place,nutrition_place)
    screen.fill(bg_color_sell_horses_place,sell_horses_place)
    screen.fill(bg_color_health_place,health_place)
    screen.fill(bg_color_happiness_place,happiness_place)

    for jelly in ga.population:
        #print(jelly.brain.get_weights_nna())
        jelly.draw(screen,jelly_sprite_image)


    font = pygame.font.SysFont("arial",16)

    hud_generation = font.render("Generation: %d"%generation,True,(255,255,255))
    screen.blit(hud_generation,(10 , screen_height // 4))
    
    hud_year = font.render("Year: %d"%year,True,(255,255,255))
    screen.blit(hud_year,(10 , screen_height // 4 + 20))
    
    hud_best_fitness = font.render("Best Fitness gen %d: %d"%(generation-1,fitness_best_jelly_of_generation),True,(255,255,255))
    screen.blit(hud_best_fitness,(10 , screen_height // 4 + 40))
    
    hud_average_fitness = font.render("Average Fitness gen %d: %d"%(generation-1,average_fitness),True,(255,255,255))
    screen.blit(hud_average_fitness,(10 , screen_height // 4 + 60))

    hud_size_population = font.render("Size Population: %d"%size_population,True,(255,255,255))
    screen.blit(hud_size_population,(10 , screen_height // 4 + 100))

    hud_mutation_rate = font.render("Mutation Rate: %.2f"%mutation_rate,True,(255,255,255))
    screen.blit(hud_mutation_rate,(10 , screen_height // 4 + 120))

    hud_elitism = font.render("Elitism: %d"%elitism,True,(255,255,255))
    screen.blit(hud_elitism,(10 , screen_height // 4 + 140))
    
    hud_fitness_goal = font.render("Fitness Goal: %d"%fitness_goal,True,(255,255,255))
    screen.blit(hud_fitness_goal,(10 , screen_height // 4 + 160))
    





    label_buy_horses = font.render("BH",True,(0,0,0))
    screen.blit(label_buy_horses,(buy_horses_place_posx + buy_horses_place_width // 3, buy_horses_place_posy + buy_horses_place_height // 3))
    
    label_sell_horses = font.render("SH",True,(0,0,0))
    screen.blit(label_sell_horses,(sell_horses_place_posx + sell_horses_place_width // 3 , sell_horses_place_posy + sell_horses_place_height // 3))
    
    label_buy_happiness = font.render("HAPY",True,(0,0,0))
    screen.blit(label_buy_happiness,(happiness_place_posx + happiness_place_width // 3 ,  happiness_place_posy + happiness_place_height // 3))
    
    label_buy_health = font.render("HLTH",True,(0,0,0))
    screen.blit(label_buy_health,(health_place_posx + health_place_width // 3 ,  health_place_posy + health_place_height // 3))
    
    label_buy_nutrition = font.render("NUTR",True,(0,0,0))
    screen.blit(label_buy_nutrition,(nutrition_place_posx + nutrition_place_width // 3,  nutrition_place_posy + nutrition_place_height // 3))
    
    font = pygame.font.SysFont("arial",30)
    label_spawn = font.render("SPAWN",True,(0,0,0))
    screen.blit(label_spawn,(spawn_place_posx + spawn_place_width // 4,  spawn_place_posy + spawn_place_height // 3))


    pygame.display.update() 


def draw_graphics_test(jelly,year):
    global screen
    
    screen.fill(bg_color)
    screen.fill(bg_color_spawn_place,spawn_place)
    screen.fill(bg_color_buy_horses_place,buy_horses_place)
    screen.fill(bg_color_nutrition_place,nutrition_place)
    screen.fill(bg_color_sell_horses_place,sell_horses_place)
    screen.fill(bg_color_health_place,health_place)
    screen.fill(bg_color_happiness_place,happiness_place)
    

    font = pygame.font.SysFont("arial",16)
    
    hud_year = font.render("Year: %d"%year,True,(255,255,255))
    screen.blit(hud_year,(10 , screen_height // 4 + 20))
    
    hud_golds = font.render("Golds: %d"%jelly.golds,True,(255,255,255))
    screen.blit(hud_golds,(10 , screen_height // 4 + 40))
    
    hud_horses = font.render("Horses: %d"%jelly.horses,True,(255,255,255))
    screen.blit(hud_horses,(10 , screen_height // 4 + 60))
    
    hud_heritage = font.render("Heritage: %d"%(jelly.golds + (jelly.horses * sell_price_horse)),True,(255,255,255))
    screen.blit(hud_heritage,(10 , screen_height // 4 + 80))

    hud_happiness = font.render("Happiness: %d"%jelly.happiness,True,(255,255,255))
    screen.blit(hud_happiness,(10 , screen_height // 4 + 140))
    
    hud_health = font.render("Health: %d"%jelly.health,True,(255,255,255))
    screen.blit(hud_health,(10 , screen_height // 4 + 160))
    
    hud_nutrition = font.render("Nutrition: %d"%jelly.nutrition,True,(255,255,255))
    screen.blit(hud_nutrition,(10 , screen_height // 4 + 180))    
    
    
    label_buy_horses = font.render("BH",True,(0,0,0))
    screen.blit(label_buy_horses,(buy_horses_place_posx + buy_horses_place_width // 3, buy_horses_place_posy + buy_horses_place_height // 3))
    
    label_sell_horses = font.render("SH",True,(0,0,0))
    screen.blit(label_sell_horses,(sell_horses_place_posx + sell_horses_place_width // 3 , sell_horses_place_posy + sell_horses_place_height // 3))
    
    label_buy_happiness = font.render("HAPY",True,(0,0,0))
    screen.blit(label_buy_happiness,(happiness_place_posx + happiness_place_width // 3 ,  happiness_place_posy + happiness_place_height // 3))
    
    label_buy_health = font.render("HLTH",True,(0,0,0))
    screen.blit(label_buy_health,(health_place_posx + health_place_width // 3 ,  health_place_posy + health_place_height // 3))
    
    label_buy_nutrition = font.render("NUTR",True,(0,0,0))
    screen.blit(label_buy_nutrition,(nutrition_place_posx + nutrition_place_width // 3,  nutrition_place_posy + nutrition_place_height // 3))

    font = pygame.font.SysFont("arial",30)
    label_spawn = font.render("SPAWN",True,(0,0,0))
    screen.blit(label_spawn,(spawn_place_posx + spawn_place_width // 4,  spawn_place_posy + spawn_place_height // 3))

    jelly.draw(screen,jelly_sprite_image)
    pygame.display.update()
    
def update_evolve(ga,current_year):
    global decrement_happiness,decrement_health,decrement_nutrition
    for i in range(len(ga.population)):
        ga.population[i].happiness = max(0, ga.population[i].happiness - decrement_happiness)
        ga.population[i].health = max(0, ga.population[i].health - decrement_health)
        ga.population[i].nutrition = max(0, ga.population[i].nutrition - decrement_nutrition)
     
        response = ga.population[i].get_and_translate_jelly_response(current_year)
        # print(response,id(ga.population[i]))
        ga.population[i].execute_order_jelly(response)
        #print("GOLDS:",ga.population[i].golds ,"HORSES:",ga.population[i].horses )
        
def update_test(jelly,current_year):
    global decrement_happiness,decrement_health,decrement_nutrition
    
    jelly.happiness = max(0, jelly.happiness - decrement_happiness)
    jelly.health = max(0, jelly.health - decrement_health)
    jelly.nutrition = max(0, jelly.nutrition - decrement_nutrition)

     
    response = jelly.get_and_translate_jelly_response(current_year)
    jelly.execute_order_jelly(response)
    
    print("\nRESPONSE JELLY:",response)
    print("JELLY GOLDS:",jelly.golds,"JELLY HORSES:",jelly.horses,"JELLY HERITAGE (FITNESS):",jelly.fitness())
    print("JELLY HAPPINESS:",jelly.happiness,"JELLY HEALTH:",jelly.health,"JELLY NUTRITION:",jelly.nutrition)



def calculate_economy_amount(ga):

    economy_amount = 0.00    
    for j in ga.population:
        economy_amount += (j.golds + j.horses * sell_price_horse)
        
    return economy_amount

def save_best_dna(dna):
    filename = "best_dna.db"
    db = shelve.open(filename)
    db["dna"] = dna
    db.close()
    
def load_best_dna_saved():
    filename = "best_dna.db"
    db = shelve.open(filename)
    dna = db["dna"]
    db.close()    
    return dna