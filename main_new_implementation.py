#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:36:18 2018

@author: Salinas Hernandez Jaime
"""

import random
import math

#
import datetime
import time
import os
import json
import sys
import AngryBirdsGA.XmlHelpers_mod as xml

__author__ = "Salinas Hernandez Jaime"
__copyright__ = "Copyright 2018, Tijuana Institute of Technology"
__credits__ = ["Dr. Mario García Valdez",""]
__license__ = "ITT"
__version__ = "1.0.3"
__date__ = "October 19, 2018 14:10"
__maintainer__ = "Salinas Hernandez Jaime"
__email__ = "jaime.salinas@tectijuana.edu.mx"
__status__ = "Development"



## Values used for the genetic algorithm
population = 10     # For now it can only be below 10
max_gen = 100       # Max number of generations
fits = [0]           # Variable to save the fitness of each generation
gen = 1             # Generation 1
per_cross = 0.5     # Percentage of cross-over (cross-over operator)
per_comb = 0.3      # Percentage of combination (combination operator)
per_mut = 0.4       # Percentage of mutation
cross_type = 0      # Type of cross-over [ 0: One point CO - 1: Random point CO - TBD]
ind_pieces = 10     # Number of pieces that define an individual


## "Dictionary" to save the base pieces and structures
pieceDic = []
pieceDic.append([[72, 72], ["Circle","wood",0,0,0]])
pieceDic.append([[22, 42], ["RectTiny","wood",0,0,0]])
pieceDic.append([[22, 82], ["RectSmall","wood",0,0,0]])
pieceDic.append([[22, 162], ["RectMedium","wood",0,0,0]])
pieceDic.append([[22, 182], ["RectBig","wood",0,0,0]])
pieceDic.append([[42, 82], ["RectFat","wood",0,0,0]])
pieceDic.append([[42, 42], ["SquareSmall","wood",0,0,0]])
pieceDic.append([[22, 22], ["SquareTiny","wood",0,0,0]])
pieceDic.append([[72, 72], ["Triangle","wood",0,0,0]])
pieceDic.append([[82, 82], ["TriangleHole","wood",0,0,0]])
pieceDic.append([[82, 82], ["SquareHole","wood",0,0,0]])
pieceDic.append([[182, 202], ["RectBig","wood",0,-91,0],
                 ["RectMedium","wood",-90,0,90],
                 ["RectMedium","wood",90,0,90],
                 ["RectBig","wood",0,91,0]])
pieceDic.append([[182, 82], ["RectBig","wood",0,-31,0],
                 ["RectTiny","wood",-90,0,90],
                 ["RectTiny","wood",90,0,90],
                 ["RectBig","wood",0,31,0]])

## *Dynamically add more via the genetic algorithm


## Population variables for the algorithm 
p01 = [] 
p02 = []
p03 = []
p04 = []
p05 = []
p06 = []
p07 = []
p08 = []
p09 = []
p10 = []

## Create a variable reference in a list format to change values smoothly
pop_list = [p01, p02, p03, p04, p05, p06, p07, p08, p09, p10]

## Obtener el valor maximo de piezas o compuestos al momento 
n= len(pieceDic)

## A cycle to fill-up the first generation of the population
for pop in pop_list:
    # Determine via a random number which pieces to assign
    elem =[random.randint(1, n) for p in range (0, ind_pieces)]
    x =[random.randint(0, 500) for p in range (0, ind_pieces)]
    y =[random.randint(0, 500) for p in range (0, ind_pieces)]        
    
    for piece in range(0, len(elem)):
        pop.append([pieceDic[elem[piece]-1], x[piece], y[piece]])
        
while gen < max_gen and max(fits) < 100:
    fits = [0]
    # If the current generation is not the first one generate a new population
    if gen != 1:
        # Determine via a random number which pieces to assign
        elem =[random.randint(1, n) for p in range (0, ind_pieces)]
        x =[random.randint(0, 500) for p in range (0, ind_pieces)]
        y =[random.randint(0, 500) for p in range (0, ind_pieces)]        
        
        for piece in range(0, len(elem)):
            pop.append([pieceDic[elem[piece]-1], x[piece], y[piece]])
            
    # Outside IF statement
    
    # Check if the current number of population multiplied by the cross-over percentage
    # is an even or odd number, in the later case remove 1 from the value
    many = len(pop_list) * per_cross
    if many % 2 == 0:
        pass
    else:
        many = many - 1
    
    # Obtain the "parents" of the generation
    parents = []
    pr = 1
    while pr <= many:
        r = random.randint(1, population)
        if r not in parents: 
            parents.append(r)
            pr = pr + 1
            
    # Generate the cross-over operation (one-point crossover)
    for cross_parent in range(0, len(parents), 2):
        # Generate a copy of each parent for the cross-over operation
        father = pop_list[parents[cross_parent] -1 ].copy()
        mother = pop_list[parents[cross_parent + 1] - 1].copy()
        
        # "Divide" the parents chromosomes for the operation
        father11 = father[0:math.floor(ind_pieces/2)]
        father12 = father[math.floor(ind_pieces/2):]
        
        mother11 = mother[0:math.floor(ind_pieces/2)]
        mother12 = mother[math.floor(ind_pieces/2):]
        
        # Generate the childs of both parents
        son = father11 + mother12
        daughter = mother11 + father12
        
        # Mutate the childs (by chance like throwing a 100 side dice)
        # If greater than the treshold then mutate
        chance = random.randint(1, 100)
        threshold = 100 - (100 * per_mut)
        if chance > threshold:
            var=0
            #print("Mutate")
        else:
            var=1
            #print("Not Mutate")
        
        
        # Replace the parents in the generation
        pop_list[parents[cross_parent] - 1] = son
        pop_list[parents[cross_parent + 1] - 1] = daughter
        
    
    # After the cross-over
    
    # Increase value of the generation for the next cycle
    gen = gen + 1

    
project_root = os.getcwd()
config_param = json.loads(open("ga_parameters.json","r").read() )
log_path = os.path.join(project_root, config_param['log_dir'])
xml.writeXML(p01, os.path.join(project_root, log_path + "/levels-999.xml"))
    