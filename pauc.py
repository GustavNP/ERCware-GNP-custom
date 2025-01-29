
import os
import csv
import pandas as pd

pauc_lower = 0.0
pauc_upper = 0.4



# file_to_read_edc = "D:/Overførsler/general_scripts_handbooks_standards/scripts/EDC/ercware-master/python/Facenet_03_yunet_01_OFIQ_quant_test.csv"
# file_to_read_edc = "./output_files/Predicted_UQS_LFW_EDC.csv"
# file_to_read_edc = "./output_files/test_UQS_LFW_EDC.csv"
# file_to_read_edc = "./output_files/OFIQ_UQS_LFW_EDC.csv"
# file_to_read_edc = "./output_files/LFW_trained_Predicted_UQS_LFW_EDC.csv"
# file_to_read_edc = "./output_files/LFW-trained_Scalar_Predicted-UQS-LFW_EDC.csv"
# # file_to_read_edc = "./output_files/LFW-trained_Scalar-extra-removed_Predicted-UQS-LFW-EDC.csv"

input_files = []
input_files.append("output_files\Predicted-SPECIFIC-9-Test-set-VGGFace200k-ERC.csv")
input_files.append("output_files\Predicted-RFR-Top-20-Features-Test-set-VGGFace200k-ERC.csv")
input_files.append("output_files\Predicted-RFR-Top-15-Features-Test-set-VGGFace200k-ERC.csv")
input_files.append("output_files\Predicted-RFR-Top-10-Features-Test-set-VGGFace200k-ERC.csv")
input_files.append("output_files\Predicted-KNN-Test-set-VGGFace200k-ERC.csv")
input_files.append("output_files\OFIQ-UQS-Test-set-VGGFace200k-ERC.csv")
input_files.append("output_files\Predicted-RFR-SPECIFIC-14-5-FoldCV-All-Features-Test-set-VGGFace200k-ERC.csv")
input_files.append("output_files\Predicted-RFR-SPECIFIC-15-5-FoldCV-All-Features-Test-set-VGGFace200k-ERC.csv")
input_files.append("output_files\Predicted-RFR-SPECIFIC-14-NoPreprocessing-All-Features-Test-set-VGGFace200k-ERC.csv")
input_files.append("output_files\Predicted-RFR-SPECIFIC-14-OcclusionFeaturesRemoved-Test-set-VGGFace200k-ERC.csv")
input_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14.csv")
input_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low0-10-high80.csv")
input_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low0-30-high80.csv")
input_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low0-40-high60.csv")
input_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low10-40-high60.csv")
input_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low5-40-high60.csv")
input_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low10-50-high51.csv")



for root, dirs, files in os.walk("RF-EDCs"):
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(root, file)
            input_files.append(file_path)






pAUC_dictionary = {}
for file in input_files:
    edc_points = []
    with open(file) as fileObject:
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

with open("pauc_files\pauc.csv", "w", newline="") as csv_file:
    csv.writer(csv_file, delimiter=";").writerows(((file, pauc_value, pauc_lower, pauc_upper) for file, pauc_value in pAUC_dictionary.items()))


