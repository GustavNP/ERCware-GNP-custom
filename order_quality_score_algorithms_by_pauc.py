import pandas as pd


pauc_file = "pauc_files\\pauc_CQMs_VGGFace200k-25-percent-of-images-in-train-set.csv"

pauc_df = pd.read_csv(pauc_file, sep=';', header=None)
pauc_df.columns = ['Filename', 'pAUC', 'pAUC_lower_limit', 'pAUC_upper_limit']

print(pauc_df)
pauc_df = pauc_df.sort_values(by='pAUC')
print(pauc_df)

sorted_filename = pauc_file.replace('.csv', '-SORTED.csv')

pauc_df.to_csv(sorted_filename, sep=';', header=False, index=False)