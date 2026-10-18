import csv

file_path = "Sound_Choir_Synth_Sheet.csv"

mapping = {
    "P1.01": "SFX-02, SFX-03", 
    "P1.02": "SFX-02, SFX-03, SFX-05", 
    "P1.03": "SFX-07",
    "A1.01": "SFX-08",
    "A1.02": "SFX-09",
    "A3.01": "SFX-10",
    "A3.03": "SFX-11",
    "A3.04": "SFX-12",
    "A4.01": "SFX-13, SFX-14",
    "B1.03": "SFX-15",
    "B1.04": "SFX-15",
    "B2.01": "SFX-16, SFX-17",
    "C2.01": "SFX-16, SFX-17",
    "D2.01": "SFX-18",
    "D2.02": "SFX-18, SFX-19",
    "D6.02": "SFX-20",
    "D6.03": "SFX-20, SFX-21"
}

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

comment = lines[0]
csv_lines = lines[1:]

reader = csv.DictReader(csv_lines)
fieldnames = reader.fieldnames
rows = []

for row in reader:
    beat_id = row["Beat ID"]
    if beat_id in mapping:
        existing = row["SFX / Playback Layer"]
        if existing.strip().upper() == "NONE":
            row["SFX / Playback Layer"] = f"[{mapping[beat_id]}]"
        else:
            row["SFX / Playback Layer"] = f"[{mapping[beat_id]}] {existing}"
    rows.append(row)

with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(comment)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Mapped SFX tags successfully.")
