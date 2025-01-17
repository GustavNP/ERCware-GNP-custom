
import os
import csv
import pandas as pd

pauc_lower = 0.0
pauc_upper = 0.4

edc_points = []

# file_to_read_edc = "D:/Overførsler/general_scripts_handbooks_standards/scripts/EDC/ercware-master/python/Facenet_03_yunet_01_OFIQ_quant_test.csv"
# file_to_read_edc = "./output_files/Predicted_UQS_LFW_EDC.csv"
# file_to_read_edc = "./output_files/test_UQS_LFW_EDC.csv"
# file_to_read_edc = "./output_files/OFIQ_UQS_LFW_EDC.csv"
file_to_read_edc = "./output_files/LFW_trained_Predicted_UQS_LFW_EDC.csv"
# file_to_read_edc = "./output_files/LFW-trained_Scalar_Predicted-UQS-LFW_EDC.csv"
# # file_to_read_edc = "./output_files/LFW-trained_Scalar-extra-removed_Predicted-UQS-LFW-EDC.csv"

with open(file_to_read_edc) as fileObject:
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
print(pauc)

