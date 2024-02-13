import time, os
import numpy as np
import rasterio
import pandas as pd
import pqkmeans

def PQKMeans(input_raster, output_directory, output_raster, k, num_subdim, Ks, sample_size):

    tstart=time.perf_counter()
    print(f"{tstart/60} min")

    src = rasterio.open(input_raster)
    num_bands = len(src.indexes)
    bands={}
    for i in range(num_bands):
        band = np.ma.masked_values(src.read(i+1), src.nodata)

        ###Based on previous failures, the author recommends to use arrays instead of data from pandas in order to have (input values, ndimension):

        bands["band_" + str(i+1)] = band[band==band]

    #for calculations using algorithms we have to drop NaN values. previous step!!!!
    t2=time.perf_counter()
    print(f"Bands into dictionary finished in {t2/60 - tstart/60} min")

    data = pd.DataFrame.from_dict(bands)
    t3=time.perf_counter()
    print(f"Bands into dataframe finished in {t3/60 - t2/60} min")
    data2= data.dropna()

    X = np.asarray((data2[list(data)]))
    print(f"Number of bytes: {X.nbytes} ({X.nbytes/1000000000} Gb)")
    print(f"Array shape: (n of pixels per band, n of bands){X.shape}")
    ####Train the encoder!!!
    # num_subdim or M has to be multiple of the input dimension:
    encoder_start_time=time.perf_counter()
    print("Encoding.....")
    encoder = pqkmeans.encoder.PQEncoder(num_subdim=num_subdim, Ks=Ks)
    encoder.fit(X[:sample_size])
    X_pqcode = encoder.transform(X)
    encoder_end_time=time.perf_counter()
    print(f"Finished encoding in {encoder_end_time/60 - encoder_start_time/60} min")
    print(f"Pqcode shape: {X_pqcode.shape}")

    np.save(os.path.join(output_directory, "pqcode.npy"), X_pqcode)
    print(os.path.join(output_directory, "pqcode.npy"))
    ####Clustering
    clustering_start_time=time.perf_counter()
    pqkmean = pqkmeans.clustering.PQKMeans(encoder=encoder, k=k)
    Labels = pqkmean.fit_predict(X_pqcode)
    clustering_end_time=time.perf_counter()
    print(f"Finished clustering in {clustering_end_time/60 - clustering_start_time/60} min")

    #the array of the KMeans result does not contain the NaN values, so it is impossible to reshape to its original shape(raster). the nextstep is to find a way to add the Nan values (then nodata) to the labels. Maybe a for loop!!!
    print("Writing clustering result into image.....")
    writing_start=time.perf_counter()

    Z= pd.DataFrame({"Labels":Labels})
    Z_Reindexed = Z.set_index(data2.index)
    data["Label"] = Z_Reindexed["Labels"]
    Result = pd.to_numeric(data["Label"], downcast = "float" )
    im = Result.values
    im = np.reshape(Result.values, (band.shape[0],  band.shape[1] ))
    ##### After, Save

    # if proj == "EPSG":
    #         proj = proj + ": " + epsg_value + " +ellps=" + ellps + " +datum=" +datum

    #         ## For some rasterio versions (recent)
    #         #proj = proj + ": " + epsg_value
    # else:
    #         proj = proj + " +ellps=" + ellps + " +datum=" +datum
    # print("CRS is: +proj = " + proj)

    PQKMean_output = rasterio.open(output_raster, "w", driver = "GTiff", height =  band.shape[0], width =  band.shape[1], dtype =  band.dtype, count = 1, nodata = src.nodata, crs = src.crs, transform =  src.transform)
    PQKMean_output.write(im, 1)
    PQKMean_output.close()
    writing_end=time.perf_counter()
    print(f"Finished writing clustering in {writing_end/60 - writing_start/60} min")
    print(f"Total pqkmeans time: {clustering_end_time/60 - encoder_start_time/60} min")
    print(f"Total processing time: {writing_end/60 - tstart/60} min")
