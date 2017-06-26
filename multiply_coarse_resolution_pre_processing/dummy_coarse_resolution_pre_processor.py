# import snappy

class DummyCoarseResolutionPreProcessor:

    def pre_process(self, coarse_res_l1):
        print ('Performing pre-processing on coarse resolution data')
        # return snappy.Product('coarse_res_pre_processed', 'coarse_res_pre_processed',
        #                       coarse_res_l1.getSceneRasterWidth(), coarse_res_l1.getSceneRasterHeight())
        return 'pre_processed_coarse_res_product'