import csv

matrix_file = "master_production_cue_matrix.csv"

updates = {
    # A3 Updates - Palm Sunday / Escape
    "A3.001": {
        "Dramatic Purpose / Emotional State": "Palm Sunday begins",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage/Pews | Orientation: Outward | Action: Waving palm | Physical State: Outwardly composed | Internal State: Internally decided",
        "SFX / Playback Layer": "CUE - Crowd / festive street environment",
        "Analog Synth Layer": "NONE initially or very faint pulse"
    },
    "A3.002": {
        "Dramatic Purpose / Emotional State": "The world before departure",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage/Pews | Orientation: Outward | Action: Composed | Physical State: Composed | Internal State: Determined",
        "SFX / Playback Layer": "Festival ambience continues",
        "Analog Synth Layer": "CUE - Pulse starts to return beneath"
    },
    "A3.003": {
        "Dramatic Purpose / Emotional State": "Resolve hardens",
        "SHARDA / CLARE — Position & Performance State": "Position: Moving | Orientation: Forward | Action: Preparation | Physical State: Decision lands | Internal State: Stillness / Resolve",
        "SFX / Playback Layer": "Crowd begins to fall away",
        "Analog Synth Layer": "Heartbeat becomes clearer"
    },
    "A3.004": {
        "Dramatic Purpose / Emotional State": "Secret departure",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Forward | Action: Moving in dark | Physical State: Stealthy | Internal State: Concealment",
        "SFX / Playback Layer": "Exterior ambience drops",
        "Analog Synth Layer": "Heartbeat becomes dominant (higher tempo, shorter gate, more percussive)"
    },
    "A3.005": {
        "Dramatic Purpose / Emotional State": "Fear + momentum / Physical shock",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Forward | Action: Running | Physical State: Forward-driven | Internal State: Fear + determination",
        "SFX / Playback Layer": "Footsteps / breath / environmental texture. HARD CUE: BANG BANG BANG on 'Door of the dead'",
        "Analog Synth Layer": "Tempo rises gradually. Short impact/pulse disruption on BANG BANG BANG"
    },
    "A3.006": {
        "Dramatic Purpose / Emotional State": "Adrenaline / fear / forward drive",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Forward | Action: Running | Physical State: Athletic, fast | Internal State: Adrenaline",
        "SFX / Playback Layer": "Breath, terrain, distant pursuit",
        "Analog Synth Layer": "Faster, tighter sequencer (nervous system running)",
        "Projector / Multimedia": "CUE - POV Clare running down slope"
    },
    
    # A4 Updates - The Tonsure / Dedication (Spans A3.007 to A4.002 logically)
    "A3.007": {
        "Dramatic Purpose / Emotional State": "Recommitment / Surrender (The Tonsure)",
        "SHARDA / CLARE — Position & Performance State": "Position: Foot of Francis | Orientation: Toward Francis | Action: Retrieves scissors repeatedly | Physical State: Stillness, grounded | Internal State: I am choosing this again / Recommitment",
        "SFX / Playback Layer": "CUE - Shears hitting floor, fabric, breath, room tone. NO SYNTH.",
        "Analog Synth Layer": "HARD CUT TO SILENCE (Kill the pulse)"
    },
    "A3.008": {
        "Dramatic Purpose / Emotional State": "The irreversible act is complete",
        "SHARDA / CLARE — Position & Performance State": "Position: Foot of Francis | Orientation: Down | Action: Receives habit | Physical State: Submitting | Internal State: Surrender",
        "SFX / Playback Layer": "Fabric rustle",
        "Analog Synth Layer": "NONE",
        "Choir / Vocal Layer": "NONE"
    },
    "A3.009": {
        "Dramatic Purpose / Emotional State": "Communal sacred meaning returns",
        "Choir / Vocal Layer": "CUE - Full sacred choral entrance ('Make me a channel of your peace')",
        "Analog Synth Layer": "NONE (or extremely low sustained tone only if acoustically needed after rehearsal)"
    },
    "A4.001": {
        "Dramatic Purpose / Emotional State": "Vow formalized",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell/Stage | Orientation: Toward Audience | Action: Final declaration | Physical State: Stillness | Internal State: Giving life to God"
    },
    "A4.002": {
        "Dramatic Purpose / Emotional State": "Separation from world complete",
        "SHARDA / CLARE — Position & Performance State": "Position: Moving to cell | Orientation: Away | Action: Walks | Physical State: Resolute | Internal State: Separation complete"
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

print("A3 and A4 successfully updated in matrix!")
