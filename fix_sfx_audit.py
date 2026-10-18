import os
import csv
import subprocess

# 1. Fix SFX-18 Collision (Lightning vs Soldiers)
# B1_SAN_DAMIANO/SFX-18 is Lightning. Rename it to SFX-35
if os.path.exists("SFX/B1_SAN_DAMIANO/SFX-18_REC_v01_RAW.wav"):
    os.rename("SFX/B1_SAN_DAMIANO/SFX-18_REC_v01_RAW.wav", "SFX/B1_SAN_DAMIANO/SFX-35_LIGHTNING_REC_v01_RAW.wav")

# D2_SIEGE/SFX-18 is Soldiers. Rename it to SFX-24 to match my mapping script
if os.path.exists("SFX/D2_SIEGE/SFX-18_REC_v01_RAW.wav"):
    os.rename("SFX/D2_SIEGE/SFX-18_REC_v01_RAW.wav", "SFX/D2_SIEGE/SFX-24_SOLDIERS_REC_v01_RAW.wav")

# 2. Fix SFX-20 Collision (Cicada Transformation vs Christmas Bells)
# B1_SAN_DAMIANO/SFX-20 is Cicada Transformation. Rename to SFX-36
if os.path.exists("SFX/B1_SAN_DAMIANO/SFX-20_REC_v01_RAW.wav"):
    os.rename("SFX/B1_SAN_DAMIANO/SFX-20_REC_v01_RAW.wav", "SFX/B1_SAN_DAMIANO/SFX-36_CICADA_TRANSFORM_REC_v01_RAW.wav")

# D6_CHRISTMAS_MASS/SFX-20 is Christmas Bells. Rename to SFX-29 to match my mapping
if os.path.exists("SFX/D6_CHRISTMAS_MASS/SFX-20_REC_v01_RAW.wav"):
    os.rename("SFX/D6_CHRISTMAS_MASS/SFX-20_REC_v01_RAW.wav", "SFX/D6_CHRISTMAS_MASS/SFX-29_BELLS_REC_v01_RAW.wav")

# D6_CHRISTMAS_MASS/SFX-21 is Congregation. Rename to SFX-30 to match mapping
if os.path.exists("SFX/D6_CHRISTMAS_MASS/SFX-21_REC_v01_RAW.wav"):
    os.rename("SFX/D6_CHRISTMAS_MASS/SFX-21_REC_v01_RAW.wav", "SFX/D6_CHRISTMAS_MASS/SFX-30_CONGREGATION_REC_v01_RAW.wav")

# 3. Fix Sound_Choir_Synth_Sheet.csv mapping to reflect the renamed IDs
mapping_fixes = {
    "SFX-18, SFX-19": "SFX-24, SFX-19",
    "SFX-20, SFX-21": "SFX-29, SFX-30",
    "SFX-20": "SFX-29",
    "[SFX-18]": "[SFX-35]",
    "[SFX-15, SFX-20]": "[SFX-15, SFX-36]"
}

with open("Sound_Choir_Synth_Sheet.csv", "r") as f:
    content = f.read()

# Replace specifically in the SFX column (to avoid messing up other things)
# Actually, a simple string replace is safe because SFX-XX strings are unique
for old, new in mapping_fixes.items():
    content = content.replace(old, new)

with open("Sound_Choir_Synth_Sheet.csv", "w") as f:
    f.write(content)

print("ID collisions fixed and matrix updated.")
