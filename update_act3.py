import csv

matrix_file = "master_production_cue_matrix.csv"

updates = {
    # C1 Updates - Mirrors / The Fire Within
    "C1.001": {
        "Dramatic Purpose / Emotional State": "Reflection",
        "SHARDA / CLARE — Position & Performance State": "Position: Circling | Orientation: Toward Francis | Action: Circling | Physical State: Flowing | Internal State: Reflection",
        "Analog Synth Layer": "CUE - Matured version of A2 Francis/fire motif (slower, spacious, long gate, low movement)"
    },
    "C1.002": {
        "Dramatic Purpose / Emotional State": "Reflection",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Toward Audience | Action: Gazes out | Physical State: Grounded | Internal State: Clarifying"
    },
    "C1.006": {
        "Dramatic Purpose / Emotional State": "Reflection -> The Fire Within",
        "SHARDA / CLARE — Position & Performance State": "Position: At font | Orientation: Down at water | Action: Gazing | Physical State: Deep stillness | Internal State: Contemplation",
        "Analog Synth Layer": "FADE TO SILENCE (Youthful fire becomes understanding)"
    },
    "C1.007": {
        "Dramatic Purpose / Emotional State": "Human abundance",
        "Projector / Multimedia": "CUE - AI Timelapse of women converging"
    },
    "C1.008": {
        "Dramatic Purpose / Emotional State": "Sisterhood",
        "SFX / Playback Layer": "CUE - Physical sound (footsteps, bodies)"
    },
    "C1.009": {
        "Dramatic Purpose / Emotional State": "Sisterhood / Service",
        "SFX / Playback Layer": "CUE - Water poured into bowl, cloth. (Highly acoustic/physical)"
    },

    # C2 Updates - Sisterhood / Service
    "C2.001": {
        "Dramatic Purpose / Emotional State": "Sisterhood / Service",
        "Analog Synth Layer": "NONE"
    },
    "C2.006": {
        "Dramatic Purpose / Emotional State": "Human abundance / Service",
        "SHARDA / CLARE — Position & Performance State": "Position: In audience | Orientation: Toward audience member | Action: Washes foot | Physical State: Service | Internal State: Joy/Service",
        "Analog Synth Layer": "NONE"
    },
    "C2.007": {
        "Dramatic Purpose / Emotional State": "Humor / Dry",
        "SHARDA / CLARE — Position & Performance State": "Position: In audience | Orientation: Toward audience | Action: Jokes | Physical State: Light | Internal State: Amused",
        "SFX / Playback Layer": "Audience laughter/breath (Natural room acoustic)"
    },
    "C2.008": {
        "Dramatic Purpose / Emotional State": "Responsibility",
        "SHARDA / CLARE — Position & Performance State": "Position: In audience | Orientation: Toward audience | Action: Solemn | Physical State: Grounded | Internal State: Gravity of leadership"
    },
    "C2.012": {
        "Dramatic Purpose / Emotional State": "Stillness"
    },
    "C2.014": {
        "Dramatic Purpose / Emotional State": "Warmth",
        "SHARDA / CLARE — Position & Performance State": "Position: Moving back to stage | Orientation: Toward audience | Action: Smiles | Physical State: Warm | Internal State: Warmth"
    },
    "C2.015": {
        "Dramatic Purpose / Emotional State": "Transition to Fragility",
        "SFX / Playback Layer": "CUE - Canticle on Guitar begins"
    },

    # C3 Updates - Francis Returns / Physical Decline
    "C3.001": {
        "Dramatic Purpose / Emotional State": "Fragility",
        "Analog Synth Layer": "CUE - One faint pitch from the old Clare-Francis motif beneath the guitar (Same bond, older body)"
    },
    "C3.004": {
        "Dramatic Purpose / Emotional State": "Fragility",
        "SHARDA / CLARE — Position & Performance State": "Position: Near Francis | Orientation: Toward Francis | Action: Caring | Physical State: Gentle, attentive | Internal State: Compassion / Sorrow"
    },
    "C3.005": {
        "Dramatic Purpose / Emotional State": "Final service",
        "SFX / Playback Layer": "CUE - Water, cloth",
        "Analog Synth Layer": "Sustain faint pitch"
    },

    # C4 Updates - Death & Grief
    "C4.001": {
        "Dramatic Purpose / Emotional State": "Absence",
        "Analog Synth Layer": "FADE OUT (if any remained)"
    },
    "C4.002": {
        "Choir / Vocal Layer": "CUE - Canticle choir"
    },
    "C4.004": {
        "Dramatic Purpose / Emotional State": "Absence",
        "SFX / Playback Layer": "FADE Canticle out. Transition to SILENCE."
    },
    "C4.005": {
        "Dramatic Purpose / Emotional State": "Grief",
        "SHARDA / CLARE — Position & Performance State": "Position: Desk/Window | Orientation: Outward | Action: Staring | Physical State: Hollow | Internal State: Profound grief",
        "Analog Synth Layer": "NONE (dry grief)"
    },
    "C4.007": {
        "Dramatic Purpose / Emotional State": "Grief",
        "Analog Synth Layer": "NONE (Text is musical enough)"
    },
    "C4.010": {
        "Dramatic Purpose / Emotional State": "Release",
        "SHARDA / CLARE — Position & Performance State": "Position: Desk | Orientation: Toward Christ | Action: Looks up | Physical State: Releasing tension | Internal State: Acceptance",
        "Analog Synth Layer": "CUE - Faint high harmonic or warm air-like tone returns"
    },
    "C4.011": {
        "Dramatic Purpose / Emotional State": "Mortality",
        "SHARDA / CLARE — Position & Performance State": "Position: Desk | Orientation: Down | Action: Deteriorating | Physical State: Weaker stature | Internal State: Accepting mortality"
    },
    "C4.019": {
        "Dramatic Purpose / Emotional State": "Mirror returns",
        "SHARDA / CLARE — Position & Performance State": "Position: Font | Orientation: Down at water | Action: Gazing | Physical State: Matured, frail | Internal State: Reflective"
    },
    "C4.021": {
        "Choir / Vocal Layer": "CUE - Hymn transition to Act 4"
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

print("Act III successfully updated in matrix!")
