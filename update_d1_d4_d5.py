import csv

matrix_file = "master_production_cue_matrix.csv"

updates = {
    # D1 Updates - First Letter to Agnes
    "D1.001": {
        "Dramatic Purpose / Emotional State": "Frailty -> Intellectual/Spiritual Vitality",
        "SFX / Playback Layer": "CUE - Pen and paper scratching (primary sound)",
        "Analog Synth Layer": "NONE (or extremely faint stable writing harmonic)",
        "SHARDA / CLARE — Position & Performance State": "Position: Desk | Orientation: Toward paper | Action: Writing | Physical State: Weak body, alive mind (liberated by writing) | Internal State: Intimacy"
    },
    "D1.002": {
        "Dramatic Purpose / Emotional State": "Transmissible interior life",
        "SHARDA / CLARE — Position & Performance State": "Position: Desk | Orientation: Toward paper/Audience | Action: Narrating letter | Physical State: Mentally energized | Internal State: Affectionate, intimate"
    },
    "D1.004": {
        "Dramatic Purpose / Emotional State": "Completion -> Invasion (Soldiers arrive next)",
        "SFX / Playback Layer": "Hold on silence after final thought",
        "SHARDA / CLARE — Position & Performance State": "Position: Desk | Orientation: Rest | Action: Stops writing | Physical State: Weakness returns | Internal State: Finished"
    },

    # D4 Updates - Second Letter / Mirror
    "D4.001": {
        "Dramatic Purpose / Emotional State": "Relief -> Reflection",
        "SFX / Playback Layer": "CUE - Fast breathing and heartbeat remain from Siege aftermath",
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Font/Mirror | Orientation: Down | Action: Staring | Physical State: Bodily weakness | Internal State: Relief"
    },
    "D4.002": {
        "Dramatic Purpose / Emotional State": "Interior steadiness -> Contemplation",
        "SFX / Playback Layer": "Heartbeat gradually slows, breathing settles -> FADES TO SILENCE on 'Contemplate Him'",
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Font/Mirror | Orientation: Down | Action: Gaze | Physical State: Settling | Internal State: Contemplation"
    },

    # D5 Updates - Frailty / Agnes
    "D4.003": {
        "Dramatic Purpose / Emotional State": "Transition",
        "Choir / Vocal Layer": "CUE - Christmas Hymn transition (very faint)",
        "Analog Synth Layer": "NONE"
    },
    "D5.001": {
        "Dramatic Purpose / Emotional State": "Care -> Resistance",
        "SFX / Playback Layer": "CUE - 100% Acoustic. Bowl, food, fabric, feet. No Synth.",
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell/Bed | Orientation: Toward Agnes | Action: Refusing | Physical State: Extremely depleted | Internal State: Lucid but exhausted"
    },
    "D5.002": {
        "Dramatic Purpose / Emotional State": "Attempt -> Failure",
        "SFX / Playback Layer": "Sound of physical help, effort, falling",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Down | Action: Falling | Physical State: Failing body | Internal State: Frustration"
    },
    "D5.003": {
        "Dramatic Purpose / Emotional State": "Acceptance -> Abandonment",
        "SFX / Playback Layer": "Breath, voice, effort",
        "Analog Synth Layer": "NONE (No emotional underscore)",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Toward Agnes | Action: Attempting to rise -> Fails | Physical State: Depleted | Internal State: Acceptance of limit"
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

print("D1, D4, D5 successfully updated in matrix!")
