##
# @file MagEnvironment.py
#
# @brief This file contains the MagEnvironment class. 
#
# @section description_doxygen_example Description
# This file loads the local magnetic field data into the simulation.

import json
import numpy as np
import matplotlib.pyplot as plt

##
# @brief This class loads the local magnetic field data into the simulation.
class MagEnvironment2D:
    ## 
    # @brief This is the constructor for the MagEnvironment class.
    def __init__(self):
        # Parameters
        self.xMag = 0.0
        self.xMag_sdev = 0.0
        self.zMag = 0.0
        self.zMag_sdev = 0.0
        self.xLims = [-10,10]
        self.zlims = [-10,10]
        self.zres = 0.1
        self.xres = 0.1
        self.Field = np.zeros((1,1))

    ## 
    # @brief This function loads the magnetic field data from the WMM2020 model.
    # @throws FileNotFoundError if the igrfwmmData file is not found.
    def load_Mag_config(self):
        # load the WMM2020 configuration file
        try:
            with open("igrfwmmData.json") as json_file:
                config_file = json.load(json_file)  
        except FileNotFoundError:
            print("igrfwmmData.json not found. Please run the WMM2020 model to generate this file.")
            exit()

        self.xMag = config_file["result"][0]["xcomponent"]
        self.xMag_sdev = config_file["result"][0]["xcomponent_uncertainty"]
        self.zMag = config_file["result"][0]["zcomponent"]
        self.zMag_sdev = config_file["result"][0]["zcomponent_uncertainty"]

    ##
    # @breif This function loads the environment configuration file.
    # @throws FileNotFoundError if the environment file is not found.
    def load_config(self):
        # load the simulation file 
        try:
            with open("environment2D.json") as json_file:
                config_file = json.load(json_file)
        except FileNotFoundError:
            print("environment.json not found. Please view the examples provided.")
            exit()

        self.xLims = config_file["xLims"]
        self.zLims = config_file["zLims"]
        self.zres = config_file["zres"]
        self.xres = config_file["xres"]

    ##
    # @breif This function builds the environment field.   
    def build_field(self):
        # This creats the ambient 2D magnetic field of the environment that will be used in the simulation.
        vector_tuple = (self.xMag, self.zMag)  # Example 2D vector tuple

        rows = int((self.xLims[1] - self.xLims[0]) / self.xres)
        columns = int((self.zLims[1] - self.zLims[0]) / self.zres)

        # Create the field with the specified vector tuple
        self.Field = np.full((rows, columns, 2), vector_tuple)

    ##
    # @breif This function saves the field image.
    def save_field_image(self):
        # This saves a .png image of the field as a quiver plot
        x_coords = np.arange(self.xLims[0], self.xLims[1], self.xres)
        z_coords = np.arange(self.zLims[0], self.zLims[1], self.zres)
        X, Z = np.meshgrid(x_coords, z_coords)
        U, V = self.Field[:, :, 0], self.Field[:, :, 1]

        fig, ax = plt.subplots()
        ax.quiver(X, Z, U, V)
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Z (m)')
        ax.set_title('Magnetic Field')
        ax.set_xlim(self.xLims[0], self.xLims[1])
        ax.set_ylim(self.zLims[0], self.zLims[1])
        plt.savefig("field.png")