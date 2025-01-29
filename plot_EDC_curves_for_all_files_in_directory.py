import pandas as pd
import matplotlib.pyplot as plt
import os

pauc_lower = 0.0
pauc_upper = 0.4

fnmr_lower = 0.0
fnmr_upper = 0.12


directory_path = "C:\\Users\\admin\\source\\repos\\ERCware\\CQM-EDCs"


for root, dirs, files in os.walk(directory_path):
    for file in files:
        if ".csv" not in file:
            continue
        file_path = os.path.join(root, file)
        edc_df = pd.read_csv(file_path, sep=';', decimal=',', header=None)
        discard_fractions = edc_df[0].values
        errors = edc_df[1].values
        plt.step(discard_fractions, errors, where="post") # TODO: should add "label=<something>"

# plt.legend(title='Score origin:')
plt.ylim( fnmr_lower, fnmr_upper )  
plt.xlim( pauc_lower, pauc_upper )  
plt.savefig("CQM-EDCs-stacked.pdf", bbox_inches="tight")
plt.show()

