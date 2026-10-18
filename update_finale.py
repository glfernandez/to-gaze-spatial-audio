import csv

matrix_file = "master_production_cue_matrix.csv"

updates = {
    # D6 Updates - Christmas Mass / Wonder
    "D6.001": {
        "SFX / Playback Layer": "Dry room, sobbing/breath",
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Inward | Action: Sobbing | Physical State: Abandoned, physically spent | Internal State: Exhausted"
    },
    "D6.008": {
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Toward Christ | Action: Laughs through tears | Physical State: Vulnerable | Internal State: Almost ironic"
    },
    "D6.009": {
        "SFX / Playback Layer": "Absolute room tone",
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Inward | Action: Silence | Physical State: Emptiness | Internal State: Emptiness"
    },
    "D6.010": {
        "SFX / Playback Layer": "Bells + distant congregation/liturgy",
        "Analog Synth Layer": "CUE - Very faint harmonic floor enters -> gradually opens into wide harmonic space",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Upward | Action: Listens | Physical State: Disbelief | Internal State: Wonder overwhelms physical weakness"
    },
    "D6.011": {
        "Choir / Vocal Layer": "CUE - Full human sacred presence (vibrant mass hymn)",
        "Analog Synth Layer": "Support breadth (wide sustained harmonic field, long attack, enormous release, subtle detuning)",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Upward | Action: Rises instinctively -> stops -> kneels | Physical State: Kneeling | Internal State: Wonder"
    },
    "D6.012": {
        "SFX / Playback Layer": "HARD CUT / collapse to silence",
        "Analog Synth Layer": "HARD CUT TO NONE",
        "Choir / Vocal Layer": "HARD CUT TO NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Kneeling | Orientation: Upward | Action: Stillness | Physical State: Grounded | Internal State: Recognition"
    },
    "D6.013": {
        "SFX / Playback Layer": "Bare voice",
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Kneeling | Orientation: Looking around | Action: Looks around cell | Physical State: Astonished | Internal State: Quiet astonishment"
    },
    "D6.015": {
        "SFX / Playback Layer": "Dry",
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Kneeling | Orientation: Upward | Action: Praying | Physical State: Frail | Internal State: Gratitude"
    },
    "D6.016": {
        "SFX / Playback Layer": "Fades to breathing + heartbeat",
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Kneeling | Orientation: Inward | Action: Breathing | Physical State: Returns to frail body | Internal State: Spent"
    },

    # D7 Updates - Third Letter (Frailty)
    "D6.018": {
        "SFX / Playback Layer": "Primary sound: voice, coughing, feet, breath, body",
        "Analog Synth Layer": "NONE",
        "Choir / Vocal Layer": "Transition out, then dry Clare"
    },
    "D7.001": {
        "Analog Synth Layer": "NONE"
    },
    "D7.002": {
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Toward Christ | Action: Struggles to stand | Physical State: Failing body is the rhythm | Internal State: Determined but dying"
    },

    # D8 Updates - Poverty / The Rule
    "D8.001": {
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Stool | Orientation: Toward Audience | Action: Sits | Physical State: Old, frail | Internal State: Still alive -> still pushing"
    },
    "D8.009": {
        "Analog Synth Layer": "CUE - Mature 'resolve pulse' (slow, firm, single low note)",
        "SHARDA / CLARE — Position & Performance State": "Position: Stool | Orientation: Toward Audience | Action: Reciting Rule | Physical State: Frail but commanding | Internal State: Determination + mortality"
    },
    "D8.010": {
        "Analog Synth Layer": "Pulse SLOWS (does not accelerate)",
        "SHARDA / CLARE — Position & Performance State": "Position: Stool | Orientation: Toward Audience | Action: Admits frailty | Physical State: Time running out | Internal State: Acknowledging death"
    },
    "D8.011": {
        "Projector / Multimedia": "CUE - Visual callback to P1 noise, but Clare is no longer trapped inside it."
    },

    # D9 Updates - Fourth Letter
    "D9.001": {
        "Analog Synth Layer": "Resolve pulse survives for opening"
    },
    "D9.003": {
        "Analog Synth Layer": "FADES TO SILENCE (Handing practice to the audience)",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Toward Audience | Action: Teaching | Physical State: Weak but open | Internal State: Most spacious and generous internal state"
    },
    "D9.007": {
        "Analog Synth Layer": "NONE",
        "SHARDA / CLARE — Position & Performance State": "Position: Stage | Orientation: Toward Audience | Action: Teaching | Physical State: Weak but open | Internal State: Wisdom, compassion"
    },
    "D9.009": {
        "Choir / Vocal Layer": "CUE - Canticle of Creatures in a traditional tone. Final communal musical arrival.",
        "Analog Synth Layer": "NONE"
    },

    # E1 Updates - Epilogue
    "E1.001": {
        "Choir / Vocal Layer": "Canticle finishes / thins",
        "Analog Synth Layer": "NONE",
        "SFX / Playback Layer": "Room tone"
    },
    "E1.002": {
        "Choir / Vocal Layer": "FADES OUT",
        "Analog Synth Layer": "NONE",
        "SFX / Playback Layer": "Room tone thins -> SILENCE on 'Only to remain'",
        "SHARDA / CLARE — Position & Performance State": "Position: Font | Orientation: Toward Christ | Action: Gazing | Physical State: Absolute stillness | Internal State: Consummation"
    },
    "E1.003": {
        "Analog Synth Layer": "NONE",
        "SFX / Playback Layer": "SILENCE"
    },
    "E1.004": {
        "Analog Synth Layer": "NONE",
        "SFX / Playback Layer": "SILENCE"
    },
    "E1.005": {
        "Analog Synth Layer": "NONE",
        "SFX / Playback Layer": "SILENCE"
    },
    "E1.006": {
        "SFX / Playback Layer": "BLACKOUT. Hold 3-5 seconds of absolute darkness and silence before applause. No sting, no resolution chord.",
        "Analog Synth Layer": "NONE",
        "Choir / Vocal Layer": "NONE"
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

print("Finale (D6 - E1) successfully updated in matrix!")
