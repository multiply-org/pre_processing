#!/usr/bin/env python

from setuptools import setup

setup(name='multiply-pre-processing',
      version='0.1',
      description='MULTIPLY Pre-Processing',
      author='MULTIPLY Team',
      packages=['multiply_coarse_resolution_pre_processing',
                'multiply_high_resolution_pre_processing',
                'multiply_sar_pre_processing'],
     )