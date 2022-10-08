import cv2
import numpy as np
import glob
import pydicom
import nrrd
from PIL import Image 
import PIL 
import matplotlib
from matplotlib import pyplot as plt
from os.path import exists
from pydicom.encaps import encapsulate
from pydicom.uid import JPEG2000
from imagecodecs import jpeg2k_encode





alldata = glob.glob("../Data/All_Data/*")
print(len(alldata))
for direcroty in alldata:

    if direcroty == "./All_Data/301404B5C74DA2A4F46C2FC3D23989E0A557C81F_20130628_1506_L_MLO_MAMMO":
        continue
    if not "FEFEEE84BE195F519C751217FC0F5EF794C0C053" in direcroty:
        continue
    print(direcroty)


    DCM_filepath = glob.glob(direcroty+"/*.dcm")[0]
    NRRD_filepath = glob.glob(direcroty+"/*.nrrd")
    if (len(NRRD_filepath) == 2):
        print("1")
        NRRD_filepath = NRRD_filepath[1]
    else:
        NRRD_filepath = NRRD_filepath[0]
    
    with pydicom.dcmread(DCM_filepath) as dcm:
        nrrdData, nrrdHeader = nrrd.read(NRRD_filepath)

        size = nrrdData.shape
        offset = nrrdHeader["Segmentation_ReferenceImageExtentOffset"].split(" ")
        if (len(size) == 4):
            size = [size[1], size[2]]
        else:
            size = [size[0], size[1]]
        
        offset = [max(0, int(offset[0])), max(0, int(offset[1]))]

        ori_data = dcm.pixel_array
        np.save(ori_data.tostring(), "npsave.dcm")
        cropped_image = ori_data[offset[1]:offset[1] + size[1], offset[0]:offset[0] + size[0]]
        # plt.imsave(direcroty+"/cropped.jpg", cropped_image, cmap=plt.cm.bone)
        plt.imsave("./All_Cropped_Data_JPG/"+direcroty.split("/")[-1]+"_cropped.jpg", cropped_image, cmap=plt.cm.bone)
        cropped_image = ori_data[offset[1]:offset[1] + size[0], offset[0]:offset[0] + size[1]]
        # plt.imsave(direcroty+"/cropped_oppo.jpg", cropped_image, cmap=plt.cm.bone)
        plt.imsave("./All_Cropped_Data_oppo/"+direcroty.split("/")[-1]+"_cropped.jpg", cropped_image, cmap=plt.cm.bone)




 