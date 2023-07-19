##
# @brief Unit tests for the buildEnvironmentField function

import unittest
from src.magEnvironment2D import MagEnvironment2D
import numpy as np

##
# @brief This class tests the buildEnvironmentField function
class TestBuildEnvironmentField(unittest.TestCase):
    def test_buildEnvironmentField_shape(self):
        # Tests for building the environment field dimensions
        UUT = MagEnvironment2D()
        UUT.load_config()
        UUT.load_Mag_config()
        UUT.build_field()
        self.assertEqual(UUT.Field.shape, (20,20,2))

    def test_buildEnvironmentField_magnitude(self):
        # Tests for the field magnitude at 0,0
        UUT = MagEnvironment2D()
        UUT.load_config()
        UUT.load_Mag_config()
        UUT.build_field()
        expected_value = np.array([27519, -16099.9])
        actual_value = UUT.Field[0][0]
        self.assertTrue(np.allclose(actual_value, expected_value))

    def test_buildEnvironmentField_magnitude_lims(self):
        # Tests for the field magnitude at the limits of the environment
        UUT = MagEnvironment2D()
        UUT.load_config()
        UUT.load_Mag_config()
        UUT.build_field()
        expected_value = np.array([27519, -16099.9])
        actual_value = UUT.Field[UUT.Field.shape[0]-1][UUT.Field.shape[0]-1]
        self.assertTrue(np.allclose(actual_value, expected_value))

if __name__ == '__main__':
    unittest.main()