import csv

matrix_file = "master_production_cue_matrix.csv"

updates = {
    "P4.001": {
        "Dramatic Purpose / Emotional State": "The emptiness is held inside love, not erased",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Audience | Action: Softens | Physical State: Relaxed | Internal State: Remembering, personal warmth",
        "Analog Synth Layer": "Emptiness tone still faintly present, but warmer / less constricted",
        "Projector / Multimedia": "CUE - Mama imagery",
        "SFX / Playback Layer": "NONE"
    },
    "P4.002": {
        "Dramatic Purpose / Emotional State": "Perception expands",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Sweeping | Action: Storytelling | Physical State: Still | Internal State: Inward, seeing through mother's eyes",
        "Analog Synth Layer": "Add a very subtle upper harmonic / widen filter",
        "Projector / Multimedia": "CUE - Mother / world images",
        "SFX / Playback Layer": "NONE"
    },
    "P4.003": {
        "Dramatic Purpose / Emotional State": "Her personal memory becomes universal / Space opens",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Media/Audience | Action: Observes | Physical State: Still | Internal State: Morally awakened",
        "Analog Synth Layer": "Sustain / bloom slightly, broadens but not louder",
        "Projector / Multimedia": "CUE - Poverty / contemporary landscapes",
        "SFX / Playback Layer": "Optional subtle environmental texture"
    },
    "P4.004": {
        "Dramatic Purpose / Emotional State": "First moral/spiritual orientation",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Audience | Action: Direct emotional recognition | Physical State: Grounded | Internal State: Compassion",
        "Analog Synth Layer": "Tone becomes clearer but remains restrained",
        "Projector / Multimedia": "HOLD image",
        "SFX / Playback Layer": "NONE"
    },
    "P4.005": {
        "Dramatic Purpose / Emotional State": "Something is about to arrive",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Shift focus | Action: Shifts toward discovery | Physical State: Anticipatory | Internal State: Yearning",
        "Analog Synth Layer": "Emptiness motif begins to change timbre / pitch center",
        "Projector / Multimedia": "CUE - Media begins moving backward toward Assisi",
        "SFX / Playback Layer": "Transitional SFX if desired"
    },
    "P4.006": {
        "Dramatic Purpose / Emotional State": "Emptiness becomes yearning / Runway to Act I",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Forward | Action: Attention sharpens | Physical State: Attentive | Internal State: Anticipation",
        "Analog Synth Layer": "Return to core tone, but with a faint slow pulse/movement. Fade/prepare cut at end.",
        "Projector / Multimedia": "CUE - Transition into Assisi",
        "SFX / Playback Layer": "NONE"
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

print("P4 successfully updated in matrix!")
