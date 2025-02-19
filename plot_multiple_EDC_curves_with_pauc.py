import pandas as pd
import matplotlib.pyplot as plt


pauc_lower = 0.0
pauc_upper = 0.4

fnmr_lower = 0.0
fnmr_upper = 0.10


edc_files = []
# edc_files.append("output_files\Predicted-SPECIFIC-9-Test-set-VGGFace200k-ERC.csv")
# edc_files.append("output_files\Predicted-RFR-Top-20-Features-Test-set-VGGFace200k-ERC.csv")
# edc_files.append("output_files\Predicted-RFR-Top-15-Features-Test-set-VGGFace200k-ERC.csv")
# edc_files.append("output_files\Predicted-RFR-Top-10-Features-Test-set-VGGFace200k-ERC.csv")
# edc_files.append("output_files\Predicted-KNN-Test-set-VGGFace200k-ERC.csv")
# edc_files.append("output_files\OFIQ-UQS-Test-set-VGGFace200k-ERC.csv")
# edc_files.append("output_files\Predicted-RFR-SPECIFIC-14-5-FoldCV-All-Features-Test-set-VGGFace200k-ERC.csv")
# edc_files.append("output_files\Predicted-RFR-SPECIFIC-15-5-FoldCV-All-Features-Test-set-VGGFace200k-ERC.csv")
# edc_files.append("output_files\Predicted-RFR-SPECIFIC-14-NoPreprocessing-All-Features-Test-set-VGGFace200k-ERC.csv")
# edc_files.append("output_files\Predicted-RFR-SPECIFIC-14-OcclusionFeaturesRemoved-Test-set-VGGFace200k-ERC.csv")
# edc_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14.csv")
# edc_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low0-10-high80.csv")
# edc_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low0-30-high80.csv")
# edc_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low0-40-high60.csv")
# edc_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low5-40-high60.csv")
# edc_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low10-40-high60.csv")
# edc_files.append("output_files\RF-CLASSIFIER-SPECIFIC-14-low10-50-high51.csv")









# edc_files.append("RF-EDCs\EDC-RFR-SPECIFIC_FINAL_1-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFR-SPECIFIC_FINAL_2-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFR-SPECIFIC_FINAL_3-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFR-SPECIFIC_FINAL_4-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFR-SPECIFIC_FINAL_5-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFR-SPECIFIC_FINAL_6-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFR-SPECIFIC_FINAL_7-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFR-SPECIFIC_FINAL_8-VGGFace200k-rs-36-test-set.csv")


# edc_files.append("RF-EDCs\EDC-RFC-BROAD_DEFAULT_1-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_1-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_2-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_3-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_4-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_5-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_6-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_7-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_8-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_9-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_10-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_11-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\EDC-RFC-SPECIFIC_FINAL_12-All-VGGFace200k-rs-36-test-set.csv")



# =========== The one with best RFR pauc scores ============
# edc_files.append("RF-EDCs\RFR-All\EDC-RFR-SPECIFIC_FINAL_4-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFR-Top-10\EDC-RFR-SPECIFIC_FINAL_4-Top-10-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFR-Top-15\EDC-RFR-SPECIFIC_FINAL_4-Top-15-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFR-Top-20\EDC-RFR-SPECIFIC_FINAL_4-Top-20-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFR-Top-24\EDC-RFR-SPECIFIC_FINAL_4-Top-24-VGGFace200k-rs-36-test-set.csv")



# ========== The one with best RFC pauc scores =============
# edc_files.append("RF-EDCs\RFC-All\EDC-RFC-SPECIFIC_FINAL_11-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFC-Top-10\EDC-RFC-SPECIFIC_FINAL_11-Top-10-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFC-Top-15\EDC-RFC-SPECIFIC_FINAL_11-Top-15-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFC-Top-20\EDC-RFC-SPECIFIC_FINAL_11-Top-20-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFC-Top-24\EDC-RFC-SPECIFIC_FINAL_11-Top-24-VGGFace200k-rs-36-test-set.csv")


# ========== Top and bottom 3 CQMs ==========
# edc_files.append("CQM-EDCs\EDC-FaceOcclusionPrevention.scalar_VGGFace200k-25-percent-of-train-set.csv")
# edc_files.append("CQM-EDCs\EDC-EyesVisible.scalar_VGGFace200k-25-percent-of-train-set.csv")
# edc_files.append("CQM-EDCs\EDC-HeadPoseYaw.scalar_VGGFace200k-25-percent-of-train-set.csv")
# edc_files.append("CQM-EDCs\EDC-MarginAboveOfTheFaceImage.scalar_VGGFace200k-25-percent-of-train-set.csv")
# edc_files.append("CQM-EDCs\EDC-BackgroundUniformity.scalar_VGGFace200k-25-percent-of-train-set.csv")
# edc_files.append("CQM-EDCs\EDC-ExpressionNeutrality.scalar_VGGFace200k-25-percent-of-train-set.csv")


# ========= Best model for RFC for each ablation ============
# edc_files.append("RF-EDCs\RFC-All\EDC-RFC-SPECIFIC_FINAL_22-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFC-Top-10\EDC-RFC-SPECIFIC_FINAL_12-Top-10-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFC-Top-15\EDC-RFC-SPECIFIC_FINAL_11-Top-15-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFC-Top-20\EDC-RFC-SPECIFIC_FINAL_11-Top-20-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFC-Top-24\EDC-RFC-SPECIFIC_FINAL_10-Top-24-VGGFace200k-rs-36-test-set.csv")



# ========= Best model for RFC for using all features ============
# edc_files.append("RF-EDCs\RFC-All\EDC-RFC-SPECIFIC_FINAL_22-All-VGGFace200k-rs-36-test-set.csv")




# ========= Best model for RFR for each ablation ============
# edc_files.append("RF-EDCs\RFR-All\EDC-RFR-SPECIFIC_FINAL_4-All-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFR-Top-24\EDC-RFR-SPECIFIC_FINAL_4-Top-24-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFR-Top-20\EDC-RFR-SPECIFIC_FINAL_9-Top-20-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFR-Top-15\EDC-RFR-SPECIFIC_FINAL_10-Top-15-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFR-Top-10\EDC-RFR-SPECIFIC_FINAL_11-Top-10-VGGFace200k-rs-36-test-set.csv")



# ========= Best model for RFC for using all features ============
# edc_files.append("RF-EDCs\RFR-All\EDC-RFR-SPECIFIC_FINAL_4-All-VGGFace200k-rs-36-test-set.csv")













# ====== For EDC curves for random forest models ======

ax = plt.step([0], [0]) # dummy to initialize ax
plt.clf()

# OFIQ MagFace UQS
edc_df = pd.read_csv("output_files\OFIQ-UQS-Test-set-VGGFace200k-ERC.csv", sep=';', decimal=',', header=None)
discard_fractions = edc_df[0].values
errors = edc_df[1].values
ax = plt.step(discard_fractions, errors, where="post", label="OFIQ MagFace UQS - pAUC: 0.02628")

pauc_df = pd.read_csv("pauc_files\pauc.csv", sep=';', header=None)
pauc_df[1] = pauc_df[1].apply(lambda x: round(x, 5))
pauc_dict = pd.Series(pauc_df[1].values,index=pauc_df[0]).to_dict()
for file in edc_files:
    edc_df = pd.read_csv(file, sep=';', decimal=',', header=None)
    discard_fractions = edc_df[0].values
    errors = edc_df[1].values
    # ax = plt.step(discard_fractions, errors, where="post", label=file.split('\\')[1]) # TODO: should add "label=<something>"
    pauc_rounded = pauc_dict[file]
    rfc_or_rfr = "RFR" # Change to RFC or RFR
    ax = plt.step(discard_fractions, errors, where="post", label=file.split(f'EDC-{rfc_or_rfr}-')[1].split('-VGG')[0] + " - pAUC: " + str(pauc_rounded)) # TODO: should add "label=<something>"

plt.legend(title='Score origin:')
plt.savefig("test.pdf", bbox_inches="tight")
plt.ylim( fnmr_lower, fnmr_upper )  
plt.xlim( pauc_lower, pauc_upper )
plt.ylabel("FNMR")  
plt.xlabel("Discard fraction")
plt.show()






# ======= For EDC curves for CQMs ========

# ax = plt.step([0], [0]) # dummy to initialize ax
# plt.clf()

# # OFIQ MagFace UQS
# edc_df = pd.read_csv("output_files\OFIQ-UQS-Test-set-VGGFace200k-ERC.csv", sep=';', decimal=',', header=None)
# discard_fractions = edc_df[0].values
# errors = edc_df[1].values
# ax = plt.step(discard_fractions, errors, where="post", label="OFIQ MagFace UQS - pAUC: 0.02628")

# pauc_df = pd.read_csv("pauc_files\pauc_CQMs_VGGFace200k-25-percent-of-images-in-train-set.csv", sep=';', header=None) # For CQM paucs
# pauc_df[1] = pauc_df[1].apply(lambda x: round(x, 5))
# pauc_dict = pd.Series(pauc_df[1].values,index=pauc_df[0]).to_dict()
# for file in edc_files:
#     edc_df = pd.read_csv(file, sep=';', decimal=',', header=None)
#     discard_fractions = edc_df[0].values
#     errors = edc_df[1].values
#     # ax = plt.step(discard_fractions, errors, where="post", label=file.split('\\')[1]) # TODO: should add "label=<something>"
#     pauc_rounded = pauc_dict[file.split('\\')[1]]
#     ax = plt.step(discard_fractions, errors, where="post", label=file.split('EDC-')[1].split('_VGG')[0] + " - pauc: " + str(pauc_rounded)) # TODO: should add "label=<something>"

# plt.legend(title='Score origin:')
# plt.savefig("test.pdf", bbox_inches="tight")
# plt.ylim( fnmr_lower, fnmr_upper )  
# plt.xlim( pauc_lower, pauc_upper )  
# plt.show()







# # ========= Best model for RFC and RFR of all ablations ============
# edc_files.append("RF-EDCs\RFR-Top-20\EDC-RFR-SPECIFIC_FINAL_9-Top-20-VGGFace200k-rs-36-test-set.csv")
# edc_files.append("RF-EDCs\RFC-Top-20\EDC-RFC-SPECIFIC_FINAL_11-Top-20-VGGFace200k-rs-36-test-set.csv")

# ax = plt.step([0], [0]) # dummy to initialize ax
# plt.clf()

# # OFIQ MagFace UQS
# edc_df = pd.read_csv("output_files\OFIQ-UQS-Test-set-VGGFace200k-ERC.csv", sep=';', decimal=',', header=None)
# discard_fractions = edc_df[0].values
# errors = edc_df[1].values
# ax = plt.step(discard_fractions, errors, where="post", label="OFIQ MagFace UQS - pAUC: 0.02628")

# edc_df = pd.read_csv("RF-EDCs\RFR-Top-20\EDC-RFR-SPECIFIC_FINAL_9-Top-20-VGGFace200k-rs-36-test-set.csv", sep=';', decimal=',', header=None)
# discard_fractions = edc_df[0].values
# errors = edc_df[1].values
# ax = plt.step(discard_fractions, errors, where="post", label="RFR Specific 9 - Top 20 - pAUC: 0.02821")

# edc_df = pd.read_csv("RF-EDCs\RFC-Top-20\EDC-RFC-SPECIFIC_FINAL_11-Top-20-VGGFace200k-rs-36-test-set.csv", sep=';', decimal=',', header=None)
# discard_fractions = edc_df[0].values
# errors = edc_df[1].values
# ax = plt.step(discard_fractions, errors, where="post", label="RFC Specific 11 - Top 20 - pAUC: 0.02865")

# plt.legend(title='Score origin:')
# plt.savefig("test.pdf", bbox_inches="tight")
# plt.ylim( fnmr_lower, fnmr_upper )  
# plt.xlim( pauc_lower, pauc_upper )  
# plt.show()