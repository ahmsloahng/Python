# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:52:00 2021

@author: Amlan Ghosh
"""

import pulp as plp

'''Setting a solver'''

solver = plp.get_solver()

'''Defining the problem and setting the sense'''

model = plp.LpProblem('Name', sense = plp.LpMinimize) #For Minimization
model = plp.LpProblem('Name', sense = plp.LpMaximize) #For Maximization

'''Defining variables'''
#Integer
var_name = plp.LpVariable.dicts('Name', ((i) for i in iterator), upBound = None, lowBound = None, cat = plp.LpInteger) #dictionary of variables
var_name = plp.LpVariable('Name', upBound = None, lowBound = None, cat = plp.LpInteger) #single varible
#Binary
var_name = plp.LpVariable.dicts('Name', ((i) for i in iterator), cat = plp.LpBinary) #dictionary of variables
var_name = plp.LpVariable('Name', cat = plp.LpBiary) #single varible

'''Defining constraints'''
cons = {i: model.addConstraint(plp.LpConstraint(e = var_name, sense = plp.LpConstraintGE. rhs = 0, name = 'Name_'+i)) for i in iterator} #Greater than
cons = {i: model.addConstraint(plp.LpConstraint(e = var_name, sense = plp.LpConstraintLE. rhs = 0, name = 'Name_'+i)) for i in iterator} #Less than

'''Objective'''
model += plp.lpSum(var_name[i] for i in iterator)

'''Priniting the model'''
print (model)

'''Solving'''
model.solve(solver)

'''Printing problem status'''
print (plp.LpStatus[model.status])

'''Printing variables'''
for i in model.variables():
    print (str(i.name) + '=' + str(i.varValue))
    
'''Printing Objective'''
print (plp.value(model.objective))   