import csv

file_path = "Sound_Choir_Synth_Sheet.csv"

# Corrected mapping using exactly the Beat IDs from the Master matrix
mapping = {
    # P1 World mappings
    "P1.003": "SFX-01A", # Breathing
    "P1.004": "SFX-02, SFX-03, SFX-04, SFX-05, SFX-06", # Overload
    "P1.005": "SFX-07", # Rumble
    
    # Act I mappings
    "A1.002": "SFX-08, SFX-09", # Market, Coins
    "A3.011": "SFX-10", # Palm Sunday Crowd
    "A3.017": "SFX-11", # Footsteps on stone
    "A3.023": "SFX-12", # Clare's running breath
    "A3.026": "SFX-14", # Door of dead impact (A3.026 is "the bang on the door")
    "A4.009": "SFX-13, SFX-17", # Shears and tonsure cutting
    
    # Act II / III mappings
    "B1.004": "SFX-18", # Lightning strike
    "B1.009": "SFX-15, SFX-20", # Cicadas and transformation
    "B1.010": "SFX-15",
    "B2.001": "SFX-16, SFX-17, SFX-21, SFX-22", # Washing
    "C2.004": "SFX-16, SFX-22", # Washing Agnes
    
    # Act IV mappings
    "D1.002": "SFX-23", # Pen scratching
    "D2.007": "SFX-19, SFX-24", # Siege pressure, Timeless war, marching
    "D2.008": "SFX-19, SFX-24", 
    "D2.012": "SFX-25", # Panic voices
    "D3.003": "SFX-27", # Soldiers retreating
    "D4.004": "SFX-28", # Body falling Foley
    "D6.002": "SFX-29", # Christmas bells (Distant)
    "D6.005": "SFX-30, SFX-31, SFX-32" # Congregation, Organ layer, Composite
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
        if existing.strip().upper() == "NONE" or existing.strip() == "":
            row["SFX / Playback Layer"] = f"[{mapping[beat_id]}]"
        else:
            row["SFX / Playback Layer"] = f"[{mapping[beat_id]}] {existing}"
    rows.append(row)

with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(comment)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Mapped SFX tags correctly.")
