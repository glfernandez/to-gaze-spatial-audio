import csv

matrix_file = "master_production_cue_matrix.csv"

updates = {
    # P2 Updates
    "P2.001": {
        "Dramatic Purpose / Emotional State": "Discover stillness physically",
        "SHARDA / CLARE — Position & Performance State": "Position: Mat -> Floor | Orientation: Toward Francis | Action: Slowly rises | Physical State: Body recovering from P1 contraction; movement deliberate | Internal State: Arrested attention -> Curiosity",
        "SFX / Playback Layer": "NONE",
        "Analog Synth Layer": "NONE",
        "Choir / Vocal Layer": "NONE"
    },
    "P2.002": {
        "Dramatic Purpose / Emotional State": "Attraction / curiosity",
        "SHARDA / CLARE — Position & Performance State": "Position: Moving | Orientation: Toward Francis | Action: Walks | Physical State: Directed | Internal State: Attention increasingly external",
        "SFX / Playback Layer": "NONE",
        "Analog Synth Layer": "NONE",
        "Choir / Vocal Layer": "NONE"
    },
    "P2.003": {
        "Dramatic Purpose / Emotional State": "Silence holds",
        "SHARDA / CLARE — Position & Performance State": "Position: Moving | Orientation: Toward Francis | Action: HOLD | Physical State: Directed | Internal State: Recognition",
        "SFX / Playback Layer": "NONE",
        "Analog Synth Layer": "NONE",
        "Choir / Vocal Layer": "NONE"
    },
    "P2.004": {
        "Dramatic Purpose / Emotional State": "Francis becomes pathway, not destination",
        "SHARDA / CLARE — Position & Performance State": "Position: Near sanctuary | Orientation: Focus transfers to Christ | Action: HOLD | Physical State: Still | Internal State: Recognition"
    },
    "P2.005": {
        "Dramatic Purpose / Emotional State": "First true contemplation",
        "SHARDA / CLARE — Position & Performance State": "Position: Moving to chair | Orientation: Toward Christ | Action: Gazes at Christ, walks | Physical State: Complete attentiveness | Internal State: Attraction"
    },
    "P2.006": {
        "Dramatic Purpose / Emotional State": "Sacred presence materializes",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Christ | Action: Moves toward prayer | Physical State: Stops moving | Internal State: Surrender into prayer",
        "Choir / Vocal Layer": "Choir hum slowly emerges",
        "Analog Synth Layer": "Optional extremely low harmonic support later"
    },
    "P2.007": {
        "Dramatic Purpose / Emotional State": "Sacred presence materializes",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Christ | Action: Prayer | Physical State: Still | Internal State: Interior absorption",
        "Choir / Vocal Layer": "Full a cappella prayer emerges"
    },
    "P2.008": {
        "Dramatic Purpose / Emotional State": "Community enters Clare's solitude",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Christ | Action: Prayer (not toward audience) | Physical State: Still | Internal State: Interior absorption",
        "Choir / Vocal Layer": "Full a cappella prayer",
        "Analog Synth Layer": "NONE or near-imperceptible tonal foundation"
    },
    "P2.009": {
        "Dramatic Purpose / Emotional State": "Completion / suspension",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Audience | Action: Comes out of prayer, looks at audience | Physical State: Stillness remains | Internal State: Awareness of audience",
        "Choir / Vocal Layer": "Resolves naturally",
        "Analog Synth Layer": "Fade / NONE"
    },
    
    # P3 Updates
    "P3.001": {
        "Dramatic Purpose / Emotional State": "Intimate confession",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Audience | Action: Small gesture to heart | Physical State: Open | Internal State: Remembering privately, intimate",
        "Analog Synth Layer": "NONE"
    },
    "P3.002": {
        "Dramatic Purpose / Emotional State": "Humour / Storytelling",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Audience | Action: Smiles, direct eye contact | Physical State: Body opens | Internal State: Warm, conversational, spontaneous",
        "Analog Synth Layer": "NONE"
    },
    "P3.003": {
        "Dramatic Purpose / Emotional State": "Humour / Storytelling",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Sweeping gaze | Action: Jokes | Physical State: Playful | Internal State: Warm, conversational",
        "Analog Synth Layer": "NONE"
    },
    "P3.004": {
        "Dramatic Purpose / Emotional State": "Social constraint begins",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Audience | Action: Storytelling | Physical State: Body becomes slightly more contained | Internal State: Recollection of constraint",
        "Analog Synth Layer": "NONE"
    },
    "P3.005": {
        "Dramatic Purpose / Emotional State": "Social constraint",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Audience | Action: Storytelling | Physical State: Contained | Internal State: Recollection of constraint",
        "Analog Synth Layer": "NONE"
    },
    "P3.006": {
        "Dramatic Purpose / Emotional State": "World building",
        "Projector / Multimedia": "CUE - Medieval imagery"
    },
    "P3.007": {
        "Dramatic Purpose / Emotional State": "World building",
        "SFX / Playback Layer": "CUE - Light historical/period SFX",
        "Analog Synth Layer": "NONE"
    },
    "P3.008": {
        "Dramatic Purpose / Emotional State": "Storytelling",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Audience | Action: Storytelling | Physical State: Contained | Internal State: Recollection",
        "Analog Synth Layer": "NONE"
    },
    "P3.009": {
        "Dramatic Purpose / Emotional State": "Unease / First discomfort",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Audience | Action: Beat | Physical State: Stillness | Internal State: Unease / Resistance",
        "Analog Synth Layer": "CUE - One low sustained tone enters almost unnoticed (emptiness motif)"
    },
    "P3.010": {
        "Dramatic Purpose / Emotional State": "Confinement",
        "Analog Synth Layer": "CUE - Tone subtly constricts (filter/resonance shift)"
    },
    "P3.011": {
        "Dramatic Purpose / Emotional State": "Confinement",
        "Analog Synth Layer": "CUE - Tone subtly constricts (filter/resonance shift)"
    },
    "P3.012": {
        "Dramatic Purpose / Emotional State": "Confinement"
    },
    "P3.013": {
        "Dramatic Purpose / Emotional State": "Confinement"
    },
    "P3.014": {
        "Dramatic Purpose / Emotional State": "Confinement",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Audience | Action: Looks at audience | Physical State: Stillness | Internal State: Resistance"
    },
    "P3.015": {
        "Dramatic Purpose / Emotional State": "Interior absence",
        "SHARDA / CLARE — Position & Performance State": "Position: Chair/Station | Orientation: Toward Audience | Action: Smiles | Physical State: Complete stillness | Internal State: Interior absence / Emptiness",
        "Analog Synth Layer": "CUE - Emptiness motif holds/decays into next scene"
    },
    "P3.016": {
        "Dramatic Purpose / Emotional State": "Transition to Mother",
        "Analog Synth Layer": "CUE - Decay / Transition"
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

print("P2 and P3 successfully updated in matrix!")
