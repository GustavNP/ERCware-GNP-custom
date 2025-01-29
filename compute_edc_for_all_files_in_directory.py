import argparse
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import os

from edc import compute_edc


quantile = 0.90
# directory_path = "C:\\Users\\admin\\source\\repos\\FaceSimilarity\\CQM-and-dissimilarity-pairs"
# directory_path = "RFR-SPECIFIC-FINAL-Predictions"
# directory_path = "RFC-Predictions"
# directory_path = "C:/Users/admin/source/repos/FaceSimilarity/dissimilarity_and_quality_score_pairs/RFC-Top-24"
# directory_path = "C:/Users/admin/source/repos/FaceSimilarity/dissimilarity_and_quality_score_pairs/RFC-Top-20"
# directory_path = "C:/Users/admin/source/repos/FaceSimilarity/dissimilarity_and_quality_score_pairs/RFC-Top-15"
# directory_path = "C:/Users/admin/source/repos/FaceSimilarity/dissimilarity_and_quality_score_pairs/RFC-Top-10"
directory_path = "C:/Users/admin/source/repos/FaceSimilarity/dissimilarity_and_quality_score_pairs/RFR-Top-20"


lower_discard_fraction = 0.0
upper_discard_fraction = 0.40
lower_error_rate = 0.0
upper_error_rate = 0.125


output_directory = "RF-EDCs/RFR-Top-20"

for root, dirs, files in os.walk(directory_path):
    for file in files:
        if ".csv" not in file:
            continue
        # Load the CSV input file:
        file_path = os.path.join(root, file)
        with open(file_path, "r") as csv_file:
            csv_lines = csv.reader(csv_file)
            next(csv_lines, None)  # Skip the CSV headers.
            pair_comparison_scores, pair_quality_scores = [], []
            for csv_line in csv_lines:
                pair_comparison_scores.append(float(csv_line[0]))
                pair_quality_scores.append(int(csv_line[1]))

        print(file)
        # Compute a quantile of the input comparison scores to use it as the comparison threshold:
        comparison_threshold = np.quantile(pair_comparison_scores, quantile)
        quality_score_at_threshold = np.quantile(pair_quality_scores, quantile)
        print(comparison_threshold)


        # Run the EDC computations:
        discard_fractions, errors = compute_edc(pair_comparison_scores, pair_quality_scores, comparison_threshold, np.greater)
        
        discard_fractions = np.concatenate((discard_fractions, np.array([1.0])))
        errors = np.concatenate((errors, np.array([0.0])))

        output_filename_csv = file.split('OFIQ_')[1] # assumes the files use CQMs, RFR or RFC, and the name of interest comes after "OFIQ_"
        output_filename_pdf = output_filename_csv.replace('csv', 'pdf')


        # Draw, save, and display a basic EDC plot:
        plt.step(discard_fractions, errors, where="post")
        plt.ylim( lower_error_rate, upper_error_rate )  
        plt.xlim( lower_discard_fraction, upper_discard_fraction )  
        # plt.savefig(f"CQM-EDCs/EDC-{output_filename_pdf}", bbox_inches="tight")
        plt.savefig(f"{output_directory}/EDC-{output_filename_pdf}", bbox_inches="tight")
        # plt.show()
        plt.clf()


        # Write the results to a CSV file (with "," as decimal separator and ";" as CSV delimiter to match ISO/IEC conventions):
        def format_csv_value(value):
            return str(value).replace(".", ",")

        # with open(f"CQM-EDCs/EDC-{output_filename_csv}", "w", newline="") as csv_file:
        with open(f"{output_directory}/EDC-{output_filename_csv}", "w", newline="") as csv_file:
            csv.writer(csv_file, delimiter=";").writerows(((format_csv_value(discard_fraction), format_csv_value(error))
                                                        for discard_fraction, error in zip(discard_fractions, errors)))
