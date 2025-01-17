import numpy as np


def compute_edc(pair_comparison_scores, pair_quality_scores, comparison_threshold):
    # Create a numpy array and sort it by quality:
    scores = np.array(
        list(zip(pair_comparison_scores, pair_quality_scores)),
        dtype=[("comparison", "f8"), ("quality", "u4")],
    )
    scores.sort(order="quality")
    # Run the EDC computations:
    error_and_discard_fraction_list = []
    quality_prior, quality_threshold = None, None
    for i in range(len(scores)):
        # Skip already processed quality thresholds:
        quality_prior = quality_threshold
        quality_threshold = scores["quality"][i]
        if quality_threshold == quality_prior:
            continue
        # Compute the error on the undiscarded data:
        remaining = len(scores) - i
        error = np.sum(scores["comparison"][i:] < comparison_threshold) / remaining
        # Store the result pair:
        discard_fraction = i / len(scores)
        error_and_discard_fraction_list.append((error, discard_fraction))
    return error_and_discard_fraction_list
