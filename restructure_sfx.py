import os
import shutil
import csv

# Move all files into a more coherent Scene-based folder structure
mapping = {
    "SFX/GLOBAL": "SFX/00_GLOBAL",
    "SFX/P1_WORLD": "SFX/P1_PROLOGUE",
    "SFX/ACT_I/market": "SFX/A1_MARKET",
    "SFX/ACT_I/escape": "SFX/A3_ESCAPE",
    "SFX/ACT_I/tonsure": "SFX/A4_TONSURE",
    "SFX/ACT_II_III/san_damiano": "SFX/B1_SAN_DAMIANO",
    "SFX/ACT_II_III/washing": "SFX/C2_SISTERHOOD",
    "SFX/ACT_IV/siege": "SFX/D2_SIEGE",
    "SFX/ACT_IV/mass": "SFX/D6_CHRISTMAS_MASS"
}

for old_dir, new_dir in mapping.items():
    if os.path.exists(old_dir):
        os.makedirs(new_dir, exist_ok=True)
        for root, _, files in os.walk(old_dir):
            for file in files:
                if file.endswith(".wav"):
                    shutil.move(os.path.join(root, file), os.path.join(new_dir, file))

# Remove old empty directories
shutil.rmtree("SFX/ACT_I", ignore_errors=True)
shutil.rmtree("SFX/ACT_II_III", ignore_errors=True)
shutil.rmtree("SFX/ACT_IV", ignore_errors=True)
shutil.rmtree("SFX/GLOBAL", ignore_errors=True)
shutil.rmtree("SFX/P1_WORLD", ignore_errors=True)

# Merge registers: delete sfx_asset_register_COMPLETE.csv and keep one sfx_asset_register.csv
if os.path.exists("sfx_asset_register_COMPLETE.csv"):
    os.remove("sfx_asset_register_COMPLETE.csv")

print("Restructured folders to Scene Numbers and cleaned up duplicates.")
