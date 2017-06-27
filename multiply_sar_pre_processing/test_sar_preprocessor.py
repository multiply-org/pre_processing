"""
Testing the SAR Preprocessor
"""

from . sar_pre_processor import SARPreProcessor
import unittest
import tempfile

class SARTest(unittest.TestCase):
    def setUp(self):
        self.d_in = tempfile.mkdtemp()

        self.c = {'gpt' : '/some/direcotry/'}


        self.c.update({'lr' : {'lat': 45., 'lon' : 11.2}})
        self.c.update({'ul' : {'lat': 47., 'lon' : 10.2}})


    def tearDown(self):
        pass


    def test_init(self):
        S = SARPreProcessor(config=self.c)
        S.pre_process(input=self.d_in, output=tempfile.mkdtemp())
