##
# @file: Sub2D
# @brief: This file contains the Sub2D class which is the main class for the MAD project.

import json
import numpy as np
import matplotlib.pyplot as plt

##
# @brief This class loads the local magnetic field data into the simulation.
class Sub2D:
    ##
    # @brief This is the constructor for the Sub2D class.
   def __init__(self):
        length = 80
        magField = 100
        depth = 10
