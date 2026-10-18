import csv
import os

# 1. Count what we SHOULD have
target_count = 0
sfx_ids = set()
if os.path.exists("sfx_asset_register.csv"):
    with open("sfx_asset_register.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sfx_id = row.get("Asset ID", "").strip()
            if sfx_id:
                sfx_ids.add(sfx_id)

target_count = len(sfx_ids)

# 2. Count what we ACTUALLY have
actual_count = 0
found_files = []
for root, _, files in os.walk("SFX"):
    for file in files:
        if file.endswith(".wav"):
            actual_count += 1
            found_files.append(file)

print(f"TARGET_COUNT={target_count}")
print(f"ACTUAL_COUNT={actual_count}")
print(f"IDS: {sorted(list(sfx_ids))}")
