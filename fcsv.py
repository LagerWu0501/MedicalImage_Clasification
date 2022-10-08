import csv
import glob
import pandas as pd

annotation = [["PID", "L_R", "position", "M+Cal", "M", "Cal", "Others"]]

all_patient = glob.glob("Data/All_Data/*/Annotation.fcsv")
for patient in all_patient:
    with open(patient, newline='') as f:
        rows = list(csv.reader(f, delimiter = ','))

    data = pd.DataFrame(rows[3:], columns=rows[2])
    data = data.drop(['# columns = id','z', 'ow', 'ox', 'oy', 'oz', 'sel', 'lock', 'desc', 'associatedNodeID'], axis = 1)
    value = (data.loc[data['vis'] == '1'])['label'].values
    
    PID = patient.split("/")[2].split("_")[0]
    direc = patient.split("/")[2].split("_")[3]
    Type = patient.split("/")[2].split("_")[4]+"_"+patient.split("/")[2].split("_")[5]

    infor = [PID, direc, Type]
    if ("M+Cal" in value):
        infor.append(1)
    else:
        infor.append(0)
    if ("M" in value):
        infor.append(1)
    else:
        infor.append(0)
    
    if ("Cal" in value):
        infor.append(1)
    else:
        infor.append(0)
    if ("AD" in value or "Asy" in value or "OC" in value or "NL" in value):
        infor.append(1)
    else:
        infor.append(0)
    annotation.append(infor)
    
with open("./annotation.csv", 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    # csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(annotation)