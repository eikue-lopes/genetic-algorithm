# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:10:20 2020

@author: eikue
"""
#global variables and constants

#graphics

ENABLE_GRAPHICS = True
DIR_JELLY_IMAGE = "../images/jelly.png"
jelly_sprite_image = None
jelly_width = 32
jelly_height = 32

screen = None
screen_width = 600
screen_height = 480
bg_color = (200,150,150)

spawn_place_width = 200
spawn_place_height = 200
spawn_place_posx = (screen_width - spawn_place_width) // 2
spawn_place_posy = (screen_height - spawn_place_height) // 2
spawn_place = (spawn_place_posx,spawn_place_posy,spawn_place_width,spawn_place_height)
bg_color_spawn_place = (100,100,100)


buy_horses_place_width = 100
buy_horses_place_height = 100
buy_horses_place_posx = 0
buy_horses_place_posy = 0
buy_horses_place = (buy_horses_place_posx,buy_horses_place_posy,buy_horses_place_width,buy_horses_place_height)
bg_color_buy_horses_place = (150,150,0)


nutrition_place_width = 100
nutrition_place_height = 100
nutrition_place_posx = screen_width - nutrition_place_width
nutrition_place_posy = 0
nutrition_place = (nutrition_place_posx,nutrition_place_posy,nutrition_place_width,nutrition_place_height)
bg_color_nutrition_place = (0,0,150)

sell_horses_place_width = 50
sell_horses_place_height = 200
sell_horses_place_posx = screen_width - sell_horses_place_width
sell_horses_place_posy = (screen_height - sell_horses_place_height) // 2
sell_horses_place = (sell_horses_place_posx,sell_horses_place_posy,sell_horses_place_width,sell_horses_place_height)
bg_color_sell_horses_place = (0,150,0)

health_place_width = 100
health_place_height = 100
health_place_posx = screen_width - health_place_width
health_place_posy = screen_height - health_place_height
health_place = (health_place_posx,health_place_posy,health_place_width,health_place_height)
bg_color_health_place = (200,0,0)

happiness_place_width = 100
happiness_place_height = 100
happiness_place_posx = 0
happiness_place_posy = screen_height - happiness_place_height
happiness_place = (happiness_place_posx,happiness_place_posy,happiness_place_width,happiness_place_height)
bg_color_happiness_place = (100,0,100)


#logics

elitism = True
size_population = 1000
mutation_rate = 0.01
years = 100
fitness_goal = 1500000


initial_golds_jellys = 1000
initial_horses_jellys = 10
initial_happiness_jellys = 50
initial_health_jellys = 80
initial_nutrition_jellys = 20


decrement_happiness = 7
decrement_health = 8
decrement_nutrition = 10

buy_price_horse = 100
sell_price_horse = 300

buy_price_unit_nutrition = 50
buy_price_unit_health = 40
buy_price_unit_happiness = 30
