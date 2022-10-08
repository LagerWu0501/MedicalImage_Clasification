import glob
import cv2
import torch
import random

target_num = 600

CC_train_p = glob.glob("CC/Train/EIC_positive/*")
MLO_train_p = glob.glob("MLO/Train/EIC_positive/*")

CC_train_n = glob.glob("CC/Train/EIC_negative/*")
MLO_train_n = glob.glob("MLO/Train/EIC_negative/*")

negative_dif = target_num - len(CC_train_n)
positive_dif = target_num - len(CC_train_p)


negative_index = random.sample(range(len(CC_train_n)), negative_dif)
positive_index = random.sample(range(len(CC_train_p)), positive_dif%(len(CC_train_p)))

print(len(CC_train_n))
print(len(MLO_train_n))
print(len(CC_train_p))
print(len(MLO_train_p))


for n_ind in negative_index:
    C = cv2.imread(CC_train_n[n_ind])
    M = cv2.imread(MLO_train_n[n_ind])

    degree_C = random.sample(range(1, 180), 1)
    scale_C = random.sample(range(85, 100), 1)
    rotated_C_M = cv2.getRotationMatrix2D((C.shape[1] / 2, C.shape[0] / 2), degree_C[0], scale_C[0] / 100)
    rotated_C = cv2.warpAffine(C, rotated_C_M, (C.shape[1], C.shape[0]))
    
    degree_M = random.sample(range(1, 180), 1)
    scale_M = random.sample(range(85, 100), 1)
    rotated_M_M = cv2.getRotationMatrix2D((M.shape[1] / 2, M.shape[0] / 2), degree_M[0], scale_M[0] / 100)
    rotated_M = cv2.warpAffine(M, rotated_M_M, (M.shape[1], M.shape[0]))

    cv2.imwrite("CC/Train/EIC_negative/" + CC_train_n[n_ind].split('/')[-1].split("_CC")[0] + "_CC0.jpg", rotated_C)
    cv2.imwrite("MLO/Train/EIC_negative/" + MLO_train_n[n_ind].split('/')[-1].split("_MLO")[0] + "_MLO0.jpg", rotated_M)

for p_ind in range(len(CC_train_p)):
    C = cv2.imread(CC_train_p[p_ind])
    M = cv2.imread(MLO_train_p[p_ind])

    degree_C = random.sample(range(1, 180), 1)
    scale_C = random.sample(range(85, 100), 1)
    rotated_C_M = cv2.getRotationMatrix2D((C.shape[1] / 2, C.shape[0] / 2), degree_C[0], scale_C[0] / 100)
    rotated_C = cv2.warpAffine(C, rotated_C_M, (C.shape[1], C.shape[0]))
    
    degree_M = random.sample(range(1, 180), 1)
    scale_M = random.sample(range(85, 100), 1)
    rotated_M_M = cv2.getRotationMatrix2D((M.shape[1] / 2, M.shape[0] / 2), degree_M[0], scale_M[0] / 100)
    rotated_M = cv2.warpAffine(M, rotated_M_M, (M.shape[1], M.shape[0]))
    cv2.imwrite("CC/Train/EIC_positive/" + CC_train_p[p_ind].split('/')[-1].split("_CC")[0] + "_CC0.jpg", rotated_C)
    cv2.imwrite("MLO/Train/EIC_positive/" + MLO_train_p[p_ind].split('/')[-1].split("_MLO")[0] + "_MLO0.jpg", rotated_M)

# for p_ind in range(len(CC_train_p)):
#     C = cv2.imread(CC_train_p[p_ind])
#     M = cv2.imread(MLO_train_p[p_ind])

#     degree_C = random.sample(range(1, 180), 1)
#     scale_C = random.sample(range(85, 100), 1)
#     rotated_C_M = cv2.getRotationMatrix2D((C.shape[1] / 2, C.shape[0] / 2), degree_C[0], scale_C[0] / 100)
#     rotated_C = cv2.warpAffine(C, rotated_C_M, (C.shape[1], C.shape[0]))
    
#     degree_M = random.sample(range(1, 180), 1)
#     scale_M = random.sample(range(85, 100), 1)
#     rotated_M_M = cv2.getRotationMatrix2D((M.shape[1] / 2, M.shape[0] / 2), degree_M[0], scale_M[0] / 100)
#     rotated_M = cv2.warpAffine(M, rotated_M_M, (M.shape[1], M.shape[0]))
#     cv2.imwrite("CC/Train/EIC_positive/" + CC_train_p[p_ind].split('/')[-1].split("_CC")[0] + "_CC1.jpg", rotated_C)
#     cv2.imwrite("MLO/Train/EIC_positive/" + MLO_train_p[p_ind].split('/')[-1].split("_MLO")[0] + "_MLO1.jpg", rotated_M)