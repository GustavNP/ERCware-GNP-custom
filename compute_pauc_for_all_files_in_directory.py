
import os
import csv
import pandas as pd

pauc_lower = 0.0
pauc_upper = 0.4





directory_path = "C:\\Users\\admin\\source\\repos\\ERCware\\CQM-EDCs"


pAUC_dictionary = {}

for root, dirs, files in os.walk(directory_path):
    for file in files:
        if ".csv" not in file:
            continue
        edc_points = []
        file_path = os.path.join(root, file)
        with open(file_path) as fileObject:
            reader = csv.reader(fileObject, delimiter=';')
            for row in reader:
                discard_fraction = float(row.pop(0).replace(',', '.'))
                error_rate = float(row.pop(0).replace(',', '.'))
                edc_points.append([discard_fraction, error_rate])

        pauc = 0.0
        for i in range(0,len(edc_points)-1):
            if edc_points[i][0] < pauc_upper:
                upper = min(edc_points[i+1][0], pauc_upper)
                val = edc_points[i][1] * (upper - edc_points[i][0])
                pauc += val
                # print("val")
                # print(val)
                # print("pauc_temp")
                # print(pauc)
        pAUC_dictionary[file] = pauc
        print(pauc)

with open("pauc_files\pauc_CQMs_VGGFace200k-25-percent-of-images-in-train-set.csv", "w", newline="") as csv_file:
    csv.writer(csv_file, delimiter=";").writerows(((file, pauc_value, pauc_lower, pauc_upper) for file, pauc_value in pAUC_dictionary.items()))


