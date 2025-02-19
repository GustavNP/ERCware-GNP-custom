This is a modified version of ERCWare.
===================================
The following files have been added by Gustav Nilsson Pedersen as part of the work on his master's thesis:

- compute_edc_for_all_files_in_directory.py
- compute_pauc_for_all_files_in_directory.py
- plot_multiple_EDC_curves_with_pauc.py

plot_edc_VGG_Face.py was added by Gustav in a previous course at the Technical University of Denmark.

To compute edc data points for multiple files, place csv files in "pair-files" folder and run "compute_edc_for_all_files_in_directory.py". The csv files should contain comparison scores in the first column and quality scores in the second column. The comparison scores should be dissimilarity scores.

To compute pauc values for multiple files, run "compute_pauc_for_all_files_in_directory.py" and it will compute pauc for all files in "EDC-files".

To plot edc curves for files, add the file paths to the script "plot_multiple_EDC_curves_with_pauc.py", then run it and it will plot the edc curves.






Readme from original project:
Error vs. Discard Characteristic (EDC) plots
============================================

This folder contains the "Error versus Discard Characteristic (EDC) Plotting Tool", which was developed by Martin Olsen and Elham Tabassi in the scope of the development of ISO/IEC 29794-4.
Note that, prior to standardization in ISO/IEC 29794-1, the "Discard" part of the term originally was "Reject".

The example script was adjusted by Christian Rathgeb, Jannis Priesnitz and Torsten Schlett and should now serve for all ISO/IEC 29794-x parts, to automatically generate the EDC plots to demonstrate the predictive nature of the selected quality metrics.

- Required packages:
  - numpy: For EDC computations in `edc.py` & `plot_edc.py`.
  - matplotlib: For graph plotting in `plot_edc.py`.
- Lowest tested versions for `plot_edc.py`:
  - Python: 3.6.2
  - numpy: 1.15.0
  - matplotlib 2.2.5
- Highest tested versions for `plot_edc.py`:
  - Python: 3.9.1
  - numpy: 1.20.1
  - matplotlib 3.3.4
- Lowest tested versions for `compute_edc` alone (`edc.py`):
  - Python: 3.5.6
  - numpy: 1.7.0

Parameters for `plot_edc.py`
----------------------------

`--help`: Show the CLI help message and exit.

`--version`: Show the script's version and exit.

`--input` (Default "input.csv"): Path to a CSV file that contains comparisons scores (first column) and quality scores (second column) corresponding to biometric sample pairs (rows). The scores are read as floating-point numbers (the quality scores usually range from 0 to 100 or from 0 to 1, but only the order matters for the EDC computation). Lower quality scores correspond to lower/worse quality, and lower comparison scores correspond to lower similarity. The first row is meant for headers and thus skipped during loading.

`--output` (Default "test_EDC"): The output file path, but the path extension will be added/modified to save a plot *.pdf and a result *.csv. Directories will be created if required.

`--quantile` (Default 0.1): Specifies the quantile of the input comparison scores, which establishes the comparison threshold for the EDC in this example script.

Example call: `python plot_edc.py --input input.csv --output test_EDC`

References for EDC plots
------------------------

The concept of EDC was introduced in 2007 by Patrick Grother and Elham Tabassi.

[Grother2007] P. Grother, E. Tabassi: "Performance of Biometric Quality Measures", IEEE Trans. on Pattern Analysis and Machine Intelligence, 29(4):531–543, April 2007.

[Olsen2016] M. Olsen, V. Smida, C. Busch: "Finger image quality assessment features - definitions and evaluation", IET Biometrics, 5(2):47–64, June 2016.

[Priesnitz2020] J. Priesnitz, C. Rathgeb, N. Buchmann, C. Busch, M. Margraf: "Touchless  Fingerprint Sample Quality and Biometric Performance Prediction: Prerequisites for the Applicability of NFIQ2.0“, in Proceedings of the IEEE 19th International Conference of the Biometrics Special Interest Group (BIOSIG), Darmstadt, September 16-18, 2020
