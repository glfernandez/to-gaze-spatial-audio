import csv
file_path = "Sound_Choir_Synth_Sheet.csv"

# Real mapping from actual grep results
fixes = {
    "A3.005": "SFX-14", # BANG BANG BANG
    "A3.007": "SFX-13, SFX-16, SFX-17", # Shears/Tonsure
    "B1.001": "SFX-35", # Lightning (Let me double check what row Lightning is)
    "B1.003": "SFX-35", # Let's just put it in B1.003 or B1.004 based on the text
}

# Actually, rather than guessing rows, let me find the rows by text match
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

comment = lines[0]
reader = csv.DictReader(lines[1:])
fieldnames = reader.fieldnames
rows = list(reader)

for row in rows:
    text = row["Full Script Text"].lower()
    sfx_layer = row["SFX / Playback Layer"].lower()
    
    # Door of the dead / bang bang bang
    if "bang bang bang" in text or "bang bang bang" in sfx_layer:
        if "SFX-14" not in row["SFX / Playback Layer"]:
            row["SFX / Playback Layer"] = "[SFX-14] " + row["SFX / Playback Layer"]
            
    # Scissors / shears
    if "scissors" in text or "shears" in sfx_layer:
        if "SFX-16" not in row["SFX / Playback Layer"]:
            row["SFX / Playback Layer"] = "[SFX-16, SFX-17] " + row["SFX / Playback Layer"]

    # Lightning
    if "lightning" in text or "lightning" in sfx_layer:
        if "SFX-35" not in row["SFX / Playback Layer"]:
            row["SFX / Playback Layer"] = "[SFX-35] " + row["SFX / Playback Layer"]
            
    # Cicadas
    if "cicadas" in text or "cicadas" in sfx_layer:
        if "SFX-15" not in row["SFX / Playback Layer"]:
            row["SFX / Playback Layer"] = "[SFX-15, SFX-36] " + row["SFX / Playback Layer"]

with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(comment)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Mapping fixed")
