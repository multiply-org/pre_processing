"""
Testing the SAR Preprocessor
"""

from . sar_pre_processor import SARPreProcessor
import unittest


class SARTest(unittest.TestCase):
    def setUp(self):
        self.c = {'gpt' : '/some/direcotry/'}

    def tearDown(self):
        pass


    def test_init(self):
        S = SARPreProcessor(config=self.c)
