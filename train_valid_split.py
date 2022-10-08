import shutil
import glob
import random
import os

ratio = 0.1

positive = glob.glob("ALL_Train/EIC_positive/*")
positive_r = random.sample(positive, k=int(ratio*len(positive)))
for p in positive:
    if p in positive_r:
        shutil.move(p, "Valid/" + p.split("ALL_Train/")[-1])
    else:
        shutil.move(p, "Train/" + p.split("ALL_Train/")[-1])
        
        
negative = glob.glob("ALL_Train/EIC_negative/*")
negative_r = random.sample(negative, k=int(ratio*len(negative)))
for p in negative:
    if p in negative_r:
        shutil.move(p, "Valid/" + p.split("ALL_Train/")[-1])
    else:
        shutil.move(p, "Train/" + p.split("ALL_Train/")[-1])
