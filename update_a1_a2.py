import csv

matrix_file = "master_production_cue_matrix.csv"

updates = {
    # A1 Updates
    "A1.001": {
        "Dramatic Purpose / Emotional State": "Yearning inwardly -> attention outwardly",
        "SHARDA / CLARE — Position & Performance State": "Position: Moving | Orientation: Toward Stage | Action: Changing costume | Physical State: Lighter, quicker | Internal State: Returning to the world",
        "Analog Synth Layer": "FADE TO SILENCE"
    },
    "A1.002": {
        "Projector / Multimedia": "CUE - The town of Assisi",
        "SFX / Playback Layer": "CUE - Assisi ambience if needed"
    },
    "A1.003": {
        "Dramatic Purpose / Emotional State": "Human encounter",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage/Pews | Orientation: Toward Francis | Action: Observing | Physical State: Mobile, alert | Internal State: Curious"
    },
    "A1.004": {
        "SFX / Playback Layer": "Optional worldly atmosphere",
        "Analog Synth Layer": "NONE"
    },
    "A1.005": {
        "Dramatic Purpose / Emotional State": "Human encounter",
        "Analog Synth Layer": "NONE"
    },
    "A1.006": {
        "Choir / Vocal Layer": "CUE - Choir voices Francis's signs",
        "Analog Synth Layer": "NONE"
    },
    "A1.007": {
        "Dramatic Purpose / Emotional State": "Observation -> Fascination",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage/Pews | Orientation: Toward Francis | Action: Watching | Physical State: Socially alive | Internal State: Amused / Evaluating"
    },
    "A1.008": {
        "SHARDA / CLARE — Position & Performance State": "Position: Stage/Pews | Orientation: Toward Audience | Action: Whispers to audience | Physical State: Relaxed, light | Internal State: Amused / Evaluating"
    },
    "A1.009": {
        "Dramatic Purpose / Emotional State": "Humor / Dry observation",
        "SHARDA / CLARE — Position & Performance State": "Position: Moving | Orientation: Toward Audience/Francis | Action: Laughs | Physical State: Lighter, athletic | Internal State: Highly amused",
        "Analog Synth Layer": "NONE (Completely dry)"
    },
    "A1.010": {
        "Dramatic Purpose / Emotional State": "Studying Francis",
        "SHARDA / CLARE — Position & Performance State": "Position: Weaving through pews | Orientation: Sweeping / At Francis | Action: Weaves | Physical State: Mobile, fast | Internal State: Studying, increasingly magnetized"
    },
    
    # A2 Updates
    "A2.001": {
        "Dramatic Purpose / Emotional State": "Human encounter continues",
        "Analog Synth Layer": "NONE (Francis remains sonically simple)"
    },
    "A2.002": {
        "Analog Synth Layer": "NONE"
    },
    "A2.003": {
        "Dramatic Purpose / Emotional State": "Bodily recognition -> Ignition",
        "SHARDA / CLARE — Position & Performance State": "Position: Pews/Stage | Orientation: Focused on Francis | Action: Movement reduces, gaze sharpens | Physical State: Breathing changes, center settles | Internal State: Inward ignition",
        "Analog Synth Layer": "CUE - One low pulse returns: clearer, warmer, faster, defined attack (recognition/ignition)"
    },
    "A2.004": {
        "Analog Synth Layer": "CUE - Pulse builds into clear sequencer pattern / Heartbeat",
        "SFX / Playback Layer": "NONE (Handled by Synth)"
    },
    "A2.005": {
        "Dramatic Purpose / Emotional State": "Ignition -> Expansion",
        "SHARDA / CLARE — Position & Performance State": "Position: Pews/Stage | Orientation: Focused on Francis | Action: Stillness | Physical State: Focused | Internal State: Visceral internal growth",
        "Analog Synth Layer": "Sequence gradually increases tempo, filter openness, resonance, and harmonic density, mapping biological growth"
    },
    "A2.006": {
        "Dramatic Purpose / Emotional State": "Irreversible attraction",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Toward Francis | Action: Eyes meet | Physical State: Locked | Internal State: Complete magnetization"
    },
    "A2.007": {
        "Dramatic Purpose / Emotional State": "Irreversible attraction",
        "SHARDA / CLARE — Position & Performance State": "Position: Circling | Orientation: Toward Francis | Action: Circles | Physical State: Fluid, focused | Internal State: Deep connection"
    },
    "A2.008": {
        "Projector / Multimedia": "CUE - Night imagery / stars / union"
    },
    "A2.009": {
        "Analog Synth Layer": "Peak of the sequence's formation / Full heartbeat and harmonic density",
        "Projector / Multimedia": "Cosmic imagery expands"
    },
    "A2.012": {
        "Dramatic Purpose / Emotional State": "Mutual recognition",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Toward Francis | Action: Stops, nods | Physical State: Still, grounded | Internal State: Resolute"
    },
    "A2.013": {
        "Dramatic Purpose / Emotional State": "Suspension",
        "Analog Synth Layer": "Fade or hold as a drone"
    },
    "A2.015": {
        "Dramatic Purpose / Emotional State": "Decision",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Forward | Action: Stops circling | Physical State: Resolved | Internal State: Determination"
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

print("A1 and A2 successfully updated in matrix!")
