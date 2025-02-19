
import os
import csv

pauc_lower = 0.0
pauc_upper = 0.4



# Author: Gustav Nilsson Pedersen - s174562


directory_path = "EDC-files"


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
        pAUC_dictionary[file] = pauc
        print(pauc)

with open("pauc-files\pauc-all-EDCs.csv", "w", newline="") as csv_file:
    csv.writer(csv_file, delimiter=";").writerows(((file, pauc_value, pauc_lower, pauc_upper) for file, pauc_value in pAUC_dictionary.items()))


