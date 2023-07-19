##
# @file MAD
# @brief This is the main file for the MAD project.
# @details This file contains the Simulator class which is the main class for the MAD project.
#

from magEnvironment2D import MagEnvironment2D
from Sub2D import Sub2D

##
# @brief This is the main class for the MAD project.
class Simulator:
    ##
    # @brief This is the constructor for the Simulator class.
    def __init__(self):

        # submodel
        self.environment = MagEnvironment2D()
        self.sub = Sub2D()

    ##
    # @brief This function initializes the simulator.
    def initialize(self):
        self.environment.load_config()

sim = Simulator()
sim.initialize()
print(sim.environment.xMag)