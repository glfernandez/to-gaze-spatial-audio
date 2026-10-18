import csv

matrix_file = "master_production_cue_matrix.csv"

updates = {
    # D2 / Siege
    "D2.001": {
        "Dramatic Purpose / Emotional State": "Threat enters",
        "SFX / Playback Layer": "CUE - Mercenary / war sounds + subtle modern traffic/phone bleed",
        "Analog Synth Layer": "Very low pressure bed begins",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Listening | Action: Alert | Physical State: Controlled | Internal State: Alert"
    },
    "D2.004": {
        "Dramatic Purpose / Emotional State": "She must hold others",
        "SFX / Playback Layer": "CUE - Panic voices of sisters build around her",
        "Analog Synth Layer": "Internal tone thickens",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Looking around | Action: Turns | Physical State: Responsibility lands on her | Internal State: Burdened"
    },
    "D2.005": {
        "Dramatic Purpose / Emotional State": "Mature Clare is still human",
        "SFX / Playback Layer": "External sound becomes unbearable",
        "Analog Synth Layer": "Pressure grows, but not as frantic as P1",
        "SHARDA / CLARE — Position & Performance State": "Position: Pacing | Orientation: Erratic | Action: Pacing | Physical State: Containment cracking | Internal State: Distressed"
    },
    "D2.007": {
        "Dramatic Purpose / Emotional State": "Human limit",
        "SFX / Playback Layer": "External chaos near peak",
        "Analog Synth Layer": "Synth reaches strongest internal pressure",
        "SHARDA / CLARE — Position & Performance State": "Position: Kneeling | Orientation: Upward | Action: Breaks | Physical State: Overwhelmed | Internal State: Desperate"
    },
    "D2.008": {
        "Dramatic Purpose / Emotional State": "Turning point / Surrender",
        "SFX / Playback Layer": "SFX still intense",
        "Analog Synth Layer": "Synth narrows rather than gets bigger",
        "SHARDA / CLARE — Position & Performance State": "Position: Kneeling | Orientation: Up | Action: Surrenders | Physical State: Surrendered | Internal State: Yielding to God"
    },
    # D3 / Eucharistic Stillness (starts here implicitly)
    "D2.010": {
        "Dramatic Purpose / Emotional State": "Grace interrupts fear",
        "Choir / Vocal Layer": "CUE - Voice of Christ as a child",
        "SFX / Playback Layer": "HARD CUT or rapid collapse of SFX",
        "Analog Synth Layer": "HARD CUT TO SILENCE",
        "SHARDA / CLARE — Position & Performance State": "Position: Kneeling | Orientation: Up | Action: Freezes | Physical State: Profound stillness | Internal State: Grace received"
    },
    "D2.011": {
        "Dramatic Purpose / Emotional State": "Stillness becomes action",
        "SFX / Playback Layer": "NONE",
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Moving to Eucharist | Orientation: Toward Eucharist | Action: Walks | Physical State: Calm, deliberate, grounded | Internal State: Absolute peace"
    },
    "D2.013": {
        "Dramatic Purpose / Emotional State": "World changes around her",
        "SFX / Playback Layer": "Distant retreat of soldiers / space opens",
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Standing | Orientation: Toward soldiers/door | Action: Holds Eucharist | Physical State: Holds the gesture | Internal State: Anchored"
    },
    "D2.015": {
        "Dramatic Purpose / Emotional State": "Eucharistic state",
        "SFX / Playback Layer": "Silence / room tone / breath",
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Standing | Orientation: Toward soldiers | Action: Stillness | Physical State: Stillness | Internal State: Eucharistic state"
    }
}

rows = []
with open(matrix_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        b_id = row["Beat ID"]
        if b_id in updates:
            for key, val in updates[b_id].items():
                row[key] = val
        rows.append(row)

with open(matrix_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Siege and Eucharistic Stillness successfully updated in matrix!")
