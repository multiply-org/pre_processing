package org.eu.multiply.preprocessing.dummy.coarse;

import org.esa.snap.core.datamodel.Product;

/**
 * @author Tonio Fincke
 */
public class CoarseResolutionPreProcessor {

    public static Product preProcess(Product product) {
        return new Product("preprocessed", "preprocessed",
                           product.getSceneRasterWidth(), product.getSceneRasterHeight());
    }

}
