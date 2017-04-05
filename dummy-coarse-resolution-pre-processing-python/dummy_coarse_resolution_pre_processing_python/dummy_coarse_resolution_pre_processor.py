import snappy

class dummy_coarse_resolution_pre_processor:

    def pre_process(self, coarse_res_l1):
        print 'I preprocess'
        return snappy.Product('coarse_res_pre_processed', 'coarse_res_pre_processed',
                              coarse_res_l1.getSceneRasterWidth(), coarse_res_l1.getSceneRasterHeight())