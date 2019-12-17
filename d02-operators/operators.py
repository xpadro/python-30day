import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    """
    Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), 
    and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
    """

    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)

    total_cost = meal_cost + tip + tax
    print(round(total_cost))


solve(12, 20, 8)