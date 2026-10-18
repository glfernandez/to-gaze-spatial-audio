import csv

matrix_file = "master_production_cue_matrix.csv"

# Define the precise updates for P1
p1_updates = {
    "P1.001": {
        "Dramatic Purpose / Emotional State": "Void / expectation",
        "SHARDA / CLARE — Position & Performance State": "Position: Mat | Orientation: TBD - DIRECTORIAL | Action: Asleep | Physical State: Fully released | Internal State: Already Clare. Dormant.",
        "SFX / Playback Layer": "NONE",
        "Analog Synth Layer": "NONE",
        "Profile Light 1": "Black",
        "Profile Light 2": "Black",
        "Projector / Multimedia": "Black",
        "Cue IN Trigger": "Pre-show state"
    },
    "P1.002": {
        "Dramatic Purpose / Emotional State": "Life appearing in darkness",
        "SHARDA / CLARE — Position & Performance State": "Position: Mat | Orientation: TBD - DIRECTORIAL | Action: Still asleep | Physical State: Minimal visible breath | Internal State: Dormant",
        "SFX / Playback Layer": "CUE - Human breathing begins",
        "Analog Synth Layer": "NONE",
        "Profile Light 1": "Black / near-black",
        "Profile Light 2": "Black / near-black",
        "Cue IN Trigger": "On house clear"
    },
    "P1.003": {
        "Dramatic Purpose / Emotional State": "The room itself begins to breathe",
        "SHARDA / CLARE — Position & Performance State": "Position: Mat | Orientation: TBD - DIRECTORIAL | Action: Dormant, still | Physical State: Still | Internal State: Unaware",
        "SFX / Playback Layer": "Breathing continues",
        "Analog Synth Layer": "CUE - Low filtered-noise swell, almost subliminal",
        "Cue IN Trigger": "Follows SFX breath"
    },
    "P1.004": {
        "Dramatic Purpose / Emotional State": "Modern world invades",
        "SHARDA / CLARE — Position & Performance State": "Position: Mat | Orientation: TBD - DIRECTORIAL | Action: Small involuntary body reaction (shoulder/fingers) | Physical State: Initial tension | Internal State: Intrusion",
        "SFX / Playback Layer": "CUE - Clicks, news, traffic, ambulance, voices accumulate",
        "Analog Synth Layer": "CUE - Low unstable pressure enters",
        "Projector / Multimedia": "CUE - Media fragmentation begins",
        "Cue IN Trigger": "On Media Clicks"
    },
    "P1.005": {
        "Dramatic Purpose / Emotional State": "Sensory overload",
        "SHARDA / CLARE — Position & Performance State": "Position: Mat | Orientation: TBD - DIRECTORIAL | Action: Wakes, cups ears, tries to resist | Physical State: Contracts | Internal State: Overwhelm",
        "SFX / Playback Layer": "Maximum density",
        "Analog Synth Layer": "CUE - Rising upper frequency / resonance",
        "Projector / Multimedia": "Media intensifies"
    },
    "P1.006": {
        "Dramatic Purpose / Emotional State": "Something interrupts the panic",
        "SHARDA / CLARE — Position & Performance State": "Position: Mat | Orientation: Toward Francis | Action: Attention shifts toward Francis | Physical State: Still contracted | Internal State: Interruption",
        "SFX / Playback Layer": "World still present but beginning to thin",
        "Analog Synth Layer": "CUE - High tension bends downward into low resonance",
        "Other Performer / Staging Action": "Francis rises toward cross",
        "Cue IN Trigger": "On Francis rising"
    },
    "P1.007": {
        "Dramatic Purpose / Emotional State": "Rupture / relief",
        "SHARDA / CLARE — Position & Performance State": "Position: Mat | Orientation: Toward Francis | Action: Freezes for one breath | Physical State: Frozen | Internal State: Rupture / Relief",
        "SFX / Playback Layer": "HARD CUT",
        "Analog Synth Layer": "HARD CUT",
        "Projector / Multimedia": "Media cuts",
        "Cue IN Trigger": "On Francis reaching cross",
        "Cue OUT Trigger": "IMMEDIATE CUT ALL AUDIO"
    },
    "P1.008": {
        "Dramatic Purpose / Emotional State": "Gaze / stillness",
        "SHARDA / CLARE — Position & Performance State": "Position: Mat | Orientation: Toward Francis/Christ | Action: Hands lower, eyes fix | Physical State: Breath settles, gradual release | Internal State: Gaze / Stillness",
        "SFX / Playback Layer": "NONE",
        "Analog Synth Layer": "NONE",
        "Profile Light 1": "CUE - Francis/Christ profile",
        "Profile Light 2": "CUE - Clare revealed",
        "Cue IN Trigger": "Auto-follow silence"
    }
}

rows = []
with open(matrix_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        b_id = row["Beat ID"]
        if b_id in p1_updates:
            for key, val in p1_updates[b_id].items():
                row[key] = val
        rows.append(row)

with open(matrix_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("P1 successfully updated in matrix!")
