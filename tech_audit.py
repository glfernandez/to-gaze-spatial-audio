import csv
import re

matrix_file = "master_production_cue_matrix.csv"

# Read existing data
rows = []
with open(matrix_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

# Processing rules for operational audit
for idx, row in enumerate(rows):
    beat_id = row["Beat ID"]
    scene = row["Production Scene"]
    text = row["Full Script Text"]
    sfx = row["SFX / Playback Layer"]
    synth = row["Analog Synth Layer"]
    choir = row["Choir / Vocal Layer"]
    media = row["Projector / Multimedia"]
    
    # 1. Base Status: Most things are DESIGN LOCKED now creatively.
    row["Design Status"] = "DESIGN LOCKED"
    if "rehearsal" in synth.lower() or "optional" in synth.lower() or "rehearsal" in sfx.lower():
        row["Design Status"] = "REHEARSAL TEST"
    if "rehearsal" in choir.lower() or "optional" in choir.lower():
        row["Design Status"] = "REHEARSAL TEST"
        
    # 2. General TBD cleanup
    if row["Development / Behaviour"] == "TBD":
        row["Development / Behaviour"] = "-"
    if row["Cue OUT Trigger"] == "TBD":
        row["Cue OUT Trigger"] = "-"
    if row["Transition / Next State"] == "TBD":
        row["Transition / Next State"] = "-"
    if row["Standby / Operator Notes"] == "":
        row["Standby / Operator Notes"] = "-"
        
    # 3. Dynamic OUT Triggers
    has_cue = False
    if "CUE" in sfx or "CUE" in synth or "CUE" in choir or "CUE" in media:
        has_cue = True
        
    # Identify CUTs / FADEs
    if "FADE TO SILENCE" in synth or "FADE OUT" in synth:
        row["Cue OUT Trigger"] = "Execute Fade"
        row["Transition / Next State"] = "To Silence"
    if "HARD CUT" in synth or "HARD CUT" in sfx or "CUT" in sfx:
        row["Cue OUT Trigger"] = "Hard Cut on Action/Line"
        row["Transition / Next State"] = "Instant Silence"
        
    if has_cue and row["Cue OUT Trigger"] == "-":
        row["Cue OUT Trigger"] = "HOLD until next sequence"

    # 4. Explicit Standbys (Critical moments)
    if scene == "P1 — Opening Breath / Modern World":
        if "HARD CUT" in sfx or "HARD CUT" in synth or "silence" in text.lower() and "noise" in text.lower():
            row["Standby / Operator Notes"] = "STANDBY: All depts HARD CUT to absolute silence"
            row["Cue OUT Trigger"] = "Visual cue: End of text / Sharda physical stop"
            row["Transition / Next State"] = "Acoustic vacuum"
            
    if scene == "A3 — Palm Sunday / The Escape":
        if "Door of the dead" in text or "BANG" in sfx:
            row["Standby / Operator Notes"] = "STANDBY: SFX Heavy impact. Synth disruption."
            row["Development / Behaviour"] = "Nervous system pulse suddenly spikes"
            
    if scene.startswith("A3") or scene.startswith("A4"):
        if "scissors" in text.lower() or "Tonsure" in row["Dramatic Purpose / Emotional State"]:
            if "HARD CUT" in synth:
                row["Standby / Operator Notes"] = "STANDBY: Cut all pulse. 100% Acoustic reality."
                row["Cue OUT Trigger"] = "Francis takes out scissors"
                
    if scene == "D2 — Soldiers / Siege" or "D2" in beat_id:
        if "I will always protect you" in text:
            row["Standby / Operator Notes"] = "CRITICAL STANDBY: Siege chaos HARD CUT. Choir bare vocal."
            row["Cue OUT Trigger"] = "On Child Christ Voice"
            row["Transition / Next State"] = "Complete absence of pressure"
            row["Design Status"] = "REHEARSAL TEST" # Needs fine tuning in room
            
    if scene == "D6 — Christmas Mass / Wonder":
        if "Blessed be the Lord" in text or "You did not leave me" in text:
            row["Standby / Operator Notes"] = "CRITICAL STANDBY: Mass expansion collapse. Instant cut to breathing."
            row["Cue OUT Trigger"] = "Line: 'You did not leave me'"
            row["Transition / Next State"] = "Return to frail body / Dry"

    if scene == "E1 — Epilogue" or "E1" in beat_id:
        if "Only to remain" in text:
            row["Standby / Operator Notes"] = "STANDBY: Final silence hold."
            row["Cue OUT Trigger"] = "Line: 'Only to remain'"
        if "Black out" in text or "audience" in text.lower():
            row["Standby / Operator Notes"] = "CRITICAL STANDBY: Blackout. 5 SECOND HOLD. NO APPLAUSE."
            row["Cue OUT Trigger"] = "Sharda gaze complete"
            row["Transition / Next State"] = "Absolute darkness and silence"

with open(matrix_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Tech/Operational audit applied to 234 rows!")
