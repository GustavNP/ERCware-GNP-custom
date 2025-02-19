import csv

import numpy as np
import matplotlib.pyplot as plt
import os

from edc import compute_edc


# Author: Gustav Nilsson Pedersen - s174562


quantile = 0.90
directory_path = "pair-files"


lower_discard_fraction = 0.0
upper_discard_fraction = 0.40
lower_error_rate = 0.0
upper_error_rate = 0.125


output_directory = "EDC-files"

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

        output_filename, extension = os.path.splitext(file)
        output_filename_csv = output_filename + '.csv'
        output_filename_pdf = output_filename_csv.replace('csv', 'pdf')


        # Draw, save, and display a basic EDC plot:
        plt.step(discard_fractions, errors, where="post")
        plt.ylim( lower_error_rate, upper_error_rate )  
        plt.xlim( lower_discard_fraction, upper_discard_fraction )  
        plt.ylabel('FNMR')
        plt.xlabel('Discard fraction')
        plt.savefig(f"{output_directory}/EDC-{output_filename_pdf}", bbox_inches="tight")
        # plt.show()
        plt.clf()


        # Write the results to a CSV file (with "," as decimal separator and ";" as CSV delimiter to match ISO/IEC conventions):
        def format_csv_value(value):
            return str(value).replace(".", ",")

        with open(f"{output_directory}/EDC-{output_filename_csv}", "w", newline="") as csv_file:
            csv.writer(csv_file, delimiter=";").writerows(((format_csv_value(discard_fraction), format_csv_value(error))
                                                        for discard_fraction, error in zip(discard_fractions, errors)))
