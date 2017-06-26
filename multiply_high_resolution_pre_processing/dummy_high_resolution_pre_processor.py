# import snappy

class DummyHighResolutionPreProcessor:

    def pre_process(self, brdf_descriptor, high_res_data):
        print ('Performing pre-processing on high-resolution data using a brdf descriptor')
        # return snappy.Product('high_res_sdr', 'high_res_sdr', 1, 1)
        return 'pre_processed_high_res_product'