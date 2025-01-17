import argparse
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from edc import compute_edc

parser = argparse.ArgumentParser(prog="Plot-EDC",
                                 description="EDC (Error vs. Discard Characteristic) computation & plotting example."
                                 " This example computes the FNM-EDC and assumes that"
                                 " lower comparison scores correspond to lower similarity,"
                                 " but the compute_edc function can also compute FM-EDCs,"
                                 " or use dissimilarity comparison scores.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")
parser.add_argument("-i",
                    "--input",
                    type=Path,
                    default="input.csv",
                    help="CSV file with floating-point pair comparison scores in the first column,"
                    " and pair quality scores in the second column"
                    " (derived from the pairs' per-sample quality scores, e.g. by taking the minimum)."
                    " Lower quality scores correspond to lower/worse quality,"
                    " and lower comparison scores correspond to lower similarity."
                    " The first row is skipped to allow headers.")
parser.add_argument("-o",
                    "--output",
                    type=Path,
                    default="test_EDC",
                    help="Output file path, which should be specified without extension."
                    " The path extension will be modified to save a plot *.pdf and a result *.csv."
                    " Directories will be created if required.")
parser.add_argument("-q",
                    "--quantile",
                    type=float,
                    default=0.95,
                    help="Specifies the quantile of the input comparison scores,"
                    " which establishes the comparison threshold for the EDC in this example.")
args = parser.parse_args()

# Load the CSV input file:
with open(args.input, "r") as csv_file:
    csv_lines = csv.reader(csv_file)
    next(csv_lines, None)  # Skip the CSV headers.
    pair_comparison_scores, pair_quality_scores = [], []
    for csv_line in csv_lines:
        pair_comparison_scores.append(float(csv_line[0]))
        pair_quality_scores.append(int(csv_line[1]))

# Compute a quantile of the input comparison scores to use it as the comparison threshold:
comparison_threshold = np.quantile(pair_comparison_scores, args.quantile)
quality_score_at_threshold1 = np.quantile(pair_quality_scores, 0.84)
comparison_score_at_threshold1 = np.quantile(pair_comparison_scores, 1-0.84)
quality_score_at_threshold2 = np.quantile(pair_quality_scores, 0.916)
comparison_score_at_threshold2 = np.quantile(pair_comparison_scores, 1-0.916)
quality_score_at_threshold3 = np.quantile(pair_quality_scores, 0.9682)
comparison_score_at_threshold3 = np.quantile(pair_comparison_scores, 1-0.9682)
quality_score_at_threshold4 = np.quantile(pair_quality_scores, 0.97441)
print(comparison_threshold)
print(quality_score_at_threshold1)
print(comparison_score_at_threshold1)
print(quality_score_at_threshold2)
print(comparison_score_at_threshold2)
print(quality_score_at_threshold3)
print(comparison_score_at_threshold3)
print(quality_score_at_threshold4)

# Run the EDC computations:
discard_fractions, errors = compute_edc(pair_comparison_scores, pair_quality_scores, comparison_threshold, np.greater)

# Ensure that the output directory exists:
args.output.parent.mkdir(parents=True, exist_ok=True)

# Draw, save, and display a basic EDC plot:
plt.step(discard_fractions, errors, where="post")
plt.savefig(args.output.with_suffix(".pdf"), bbox_inches="tight")
plt.show()


# Write the results to a CSV file (with "," as decimal separator and ";" as CSV delimiter to match ISO/IEC conventions):
def format_csv_value(value):
    return str(value).replace(".", ",")


with open(args.output.with_suffix(".csv"), "w", newline="") as csv_file:
    csv.writer(csv_file, delimiter=";").writerows(((format_csv_value(discard_fraction), format_csv_value(error))
                                                   for discard_fraction, error in zip(discard_fractions, errors)))
