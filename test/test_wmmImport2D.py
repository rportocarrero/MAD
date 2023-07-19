import unittest
from src.magEnvironment2D import MagEnvironment2D
import filecmp

##
# @ brief This class tests the import of the WMM2020 model data.
class TestWmmImport2D(unittest.TestCase):
    def test_wmmImport_xMag(self):
        # Tests for x magnetic field components at 0 N 0 W
        UUT = MagEnvironment2D()
        UUT.load_Mag_config()
        self.assertEqual(UUT.xMag, 27519)

    def test_wmmImport_xMag_sdev(self):
        # Tests for x magnetic field stdev at 0 N 0 W
        UUT = MagEnvironment2D()
        UUT.load_Mag_config()
        self.assertEqual(UUT.xMag_sdev, 131)

    def test_wmmImport_zMag(self):
        # Tests for z magnetic field components at 0 N 0 W
        UUT = MagEnvironment2D()
        UUT.load_Mag_config()
        self.assertEqual(UUT.zMag, -16099.9)

    def test_wmmImport_zMag_sdev(self):
        # Tests for z magnetic field stdev at 0 N 0 W
        UUT = MagEnvironment2D()
        UUT.load_Mag_config()
        self.assertEqual(UUT.zMag_sdev, 157)

    def test_environmentImport_xlims(self):
        # Test for importing the environment x limits
        UUT = MagEnvironment2D()
        UUT.load_config()
        self.assertEqual(UUT.xLims, [-1000, 1000])

    def test_environmentImport_zlims(self):
        # Test for importing the environment z limits
        UUT = MagEnvironment2D()
        UUT.load_config()
        self.assertEqual(UUT.xLims, [-1000, 1000])

    def test_environmentImport_xres(self):
        # Test for importing the environment x resolution
        UUT = MagEnvironment2D()
        UUT.load_config()
        self.assertEqual(UUT.xres, 100)

    def test_environmentImport_zres(self):
        # Test for importing the environment z resolution
        UUT = MagEnvironment2D()
        UUT.load_config()
        self.assertEqual(UUT.zres, 100)

    def test_save_field_image(self):
        # Tests for saving the field image and comparing it to an existing image
        UUT = MagEnvironment2D()
        UUT.load_config()
        UUT.load_Mag_config()
        UUT.build_field()
        UUT.save_field_image()
        
        expected_file = "expected_field.png"
        generated_file = "field.png"

        self.assertTrue(filecmp.cmp(expected_file, generated_file, shallow=False))

if __name__ == '__main__':
    unittest.main()
