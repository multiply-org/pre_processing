"""
Wrapper module to launch preprocessor
"""

import os

class PreProcessor(object):
    def __init__(self, **kwargs):
        self.config = kwargs.get('config', None)
        self._check()

        self.gpt = self.config.gpt

    def _check(self):
        assert self.config is not None, 'ERROR: configuration needs to be provided'

    def pre_process(self):
        assert False, 'Routine should be implemented in child class'

class SARPreProcessor(PreProcessor):
    def __init__(self, **kwargs):
        super(SARPreProcessor, self).__init__(**kwargs)

        # TODO PUT THE GRAPH DIRECTORIES AND NAMES IN A SEPARATE CONFIG !!!

        # xml-processing graph
        self.xmlgraphpath = '/media/tweiss/Work/python_code/MULTIPLY/pre_processing_Sentinel_1/xml_files/'
        self.xmlgraph = 'preprocess_v01.xml'    # the XML config files should gfo somewhere in a specific directory in the multiply-core repo

    def pre_process(self, **kwargs):  # todo discuss if input/output specification part of processing or part of instantiation of the object itself
        """
        Parameters
        ----------
        inputfolder : str
            name of directory where the downloaded SAR data is 
            located
        outputfolder : str
            name of directory where to put results
        """
        self.inputfolder = kwargs.get('input', None)
        assert self.inputfolder is not None, 'ERROR: input folder not specified'
        assert os.path.exists(self.inputfolder)

        self.outputfolder = kwargs.get('output', None)
        assert self.outputfolder is not None, 'ERROR: Outputfolder needs to be specified'
        if not os.path.exists(self.outputfolder):
            os.makedirs(self.outputfolder)
        
        # Name addition for processed data
        xml_addition = 'subset'
        
        lowerright_y = self.config.region['lr']['lat']
        upperleft_y = self.config.region['ul']['lat']
        upperleft_x = self.config.region['ul']['lon']
        lowerright_x = self.config.region['lr']['lon']
        # todo: how is it with coordinates that go across the datum line ??

        # Coordinates for subset area
        area = self.get_area(lowerright_y, upperleft_y, upperleft_x, lowerright_x)
        
        
        # o.k., now the rest of the preprocessor can be added here
        # to keep things most flexible it would be good to have that in 
        # a separate class
        
        return 'some data'

    def get_area(self, latmin, latmax, lonmin, lonmax):
        """
        Change input coordinates for subset operator
        """
        assert latmin <= latmax, 'ERROR: invalid lat'
        assert lonmin <= lonmax, 'ERROR: invalid lon'
        return '%.14f %.14f,%.14f %.14f,%.14f %.14f,%.14f %.14f,%.14f %.14f' % (lonmin, latmin, lonmin, latmax, lonmax, latmax, lonmax, latmin, lonmin, latmin)







