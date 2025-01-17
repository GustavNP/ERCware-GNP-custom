import numpy as np


def compute_edc(pair_comparison_scores, pair_quality_scores, comparison_threshold, comparison_function):
    """Computes the EDC using `numpy` functions.

    This docstring is written in the numpydoc style.

    Parameters
    ----------
    pair_comparison_scores : array_like
        The pairwise biometric comparison scores (floating-point or integer).
        This does not need to be sorted, but the comparison scores need to correspond to the `pair_quality_scores`,
        so that `zip(pair_comparison_scores, pair_quality_scores)` represents the pairwise comparison & quality scores.
    pair_quality_scores : array_like
        The pairwise biometric quality scores (floating-point or integer).
        It is assumed that higher quality scores mean better quality,
        so that comparisons with lower quality scores are discarded first.
        Pairwise quality scores can be derived as the minimum of the pairs' corresponding sample quality scores.
    comparison_threshold : float or int
        The `pair_quality_scores` are compared against this `comparison_threshold` via the `comparison_function`
        to determine which of the comparisons represent an "error" in the computed EDC.
    comparison_function : np.ufunc
        Choosing this function depends on whether higher or lower comparison scores mean higher similarity,
        and it depends on whether a FNM-EDC or a FM-EDC is to be computed.
        The `pair_comparison_scores` are the left-hand side of the comparison,
        `comparison_threshold` is the right-hand side.
        E.g. if higher comparison scores mean higher similarity,
        then `np.less` can be used to compute the FNM-EDC,
        and `np.greater_equal` can be used to compute the FM-EDC.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        The `discard_fractions` and the corresponding `error_fractions` of the computed EDC are returned.
        For EDC plots, the `discard_fractions` are typically plotted on the x-axis, `error_fractions` on the y-axis.
    """
    # Create a numpy array and sort it by quality:
    scores = np.array(
        list(zip(pair_comparison_scores, pair_quality_scores)),
        dtype=[("comparison", "f8"), ("quality", "f8")],
    )
    scores.sort(order="quality")
    # Run the EDC computations:
    # The array indices correspond to the discard counts, so 0 comparisons are discarded at index 0.
    comparison_count = len(scores)
    # Compute the (binary) per-comparison errors by comparing the comparison scores against the comparison_threshold:
    error_counts = np.zeros(comparison_count, dtype=np.uint32)
    comparison_function(scores["comparison"], comparison_threshold, out=error_counts)
    # Then compute the cumulative error_counts sum:
    # The total error count will be at index 0, which corresponds to 0 discarded comparisons (or samples).
    # Conversely, at index comparison_count-1 only one comparison isn't discarded and the error count remains 0 or 1.
    error_counts = np.flipud(np.cumsum(np.flipud(error_counts), out=error_counts))
    # Usually the EDC should model the effect of discarding samples (instead of individual comparisons) based on
    # a progressively increasing quality threshold. This means that sequences of identical quality scores have to be
    # skipped at once. In this implementation the discard counts are equivalent to the array indices, so computing
    # the relevant array indices for the quality sequence starting points also obtains the corresponding discard counts:
    discard_counts = np.where(scores["quality"][:-1] != scores["quality"][1:])[0] + 1
    discard_counts = np.concatenate(([0], discard_counts))
    # Subtracting the discard_counts from the total comparison_count results in the remaining_counts:
    remaining_counts = comparison_count - discard_counts
    # Divide the relevant error_counts by the remaining_counts to compute the error_fractions:
    error_fractions = error_counts[discard_counts] / remaining_counts
    # Divide the discard_counts by the total comparison_count to compute the discard_fractions:
    discard_fractions = discard_counts / comparison_count
    # Return the discard_fractions together with the corresponding error_fractions:
    return discard_fractions, error_fractions
