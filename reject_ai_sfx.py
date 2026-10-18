import csv

file_path = "sfx_asset_register.csv"
rows = []

with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        if row["Asset ID"].startswith("SFX-03"):
            row["Approved"] = "REJECTED (AI Artifacts)"
            row["Notes"] += " AI generation failed realism check. Replaced with acoustic field recording."
        if row["Asset ID"].startswith("SFX-05"):
            row["Approved"] = "REJECTED (AI Artifacts)"
            row["Notes"] += " AI generation failed realism check. Replaced with acoustic field recording."
        rows.append(row)

with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Updated register to reject AI traffic and emergency stems.")
