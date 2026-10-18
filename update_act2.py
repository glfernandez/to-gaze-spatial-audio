import csv

matrix_file = "master_production_cue_matrix.csv"

updates = {
    # B1 Updates - Rebuilding San Damiano
    "B1.001": {
        "Dramatic Purpose / Emotional State": "Threshold into new life",
        "SHARDA / CLARE — Position & Performance State": "Position: Moving to font | Orientation: Toward Francis | Action: Moves | Physical State: Quieter, post-tonsure | Internal State: Surrendered",
        "SFX / Playback Layer": "NONE",
        "Analog Synth Layer": "NONE",
        "Choir / Vocal Layer": "NONE"
    },
    "B1.002": {
        "Dramatic Purpose / Emotional State": "Revelation arrives",
        "SHARDA / CLARE — Position & Performance State": "Position: Near font | Orientation: Upward / Alert | Action: Freezes | Physical State: Still | Internal State: Attention caught",
        "SFX / Playback Layer": "CUE - ONE brief, decisive lightning strike. NOT a cinematic roll.",
        "Analog Synth Layer": "Very low sub impact only if needed"
    },
    "B1.003": {
        "Dramatic Purpose / Emotional State": "Divine instruction",
        "SHARDA / CLARE — Position & Performance State": "Position: Near font | Orientation: Toward Voice | Action: Listening | Physical State: Still | Internal State: Listening",
        "SFX / Playback Layer": "Lightning tail gone",
        "Analog Synth Layer": "NONE",
        "Choir / Vocal Layer": "CUE - Voice of Christ: 'Rebuild my house' (completely bare/dry)"
    },
    "B1.004": {
        "Dramatic Purpose / Emotional State": "Francis receives command",
        "SHARDA / CLARE — Position & Performance State": "Position: Near font | Orientation: Toward Francis | Action: Witnesses | Physical State: Still | Internal State: Witnessing",
        "Analog Synth Layer": "NONE"
    },
    "B1.005": {
        "Dramatic Purpose / Emotional State": "Clare inherits the place",
        "SHARDA / CLARE — Position & Performance State": "Position: Kneeling at font | Orientation: Toward Cross | Action: Kneels | Physical State: Inheriting space | Internal State: Inheriting",
        "Analog Synth Layer": "NONE"
    },
    "B1.006": {
        "Dramatic Purpose / Emotional State": "San Damiano is established",
        "SHARDA / CLARE — Position & Performance State": "Position: Kneeling/Station | Orientation: Toward Audience | Action: Narrates | Physical State: Settling | Internal State: Reflective",
        "SFX / Playback Layer": "Minimal environmental world",
        "Analog Synth Layer": "NONE (optional very faint stable tone)"
    },
    "B1.008": {
        "Dramatic Purpose / Emotional State": "...my home.",
        "SHARDA / CLARE — Position & Performance State": "Position: Kneeling/Station | Orientation: Toward Audience | Action: Reflects | Physical State: Body settles | Internal State: Settling",
        "Analog Synth Layer": "Perhaps first almost inaudible warm floor"
    },
    "B1.009": {
        "SFX / Playback Layer": "CUE - Cicadas begin"
    },
    "B1.010": {
        "Dramatic Purpose / Emotional State": "Nature takes over",
        "SHARDA / CLARE — Position & Performance State": "Position: Moving to cell | Orientation: Toward window | Action: Walks slowly | Physical State: Peaceful | Internal State: Peaceful",
        "Analog Synth Layer": "NONE"
    },
    
    # B2 Updates - Solitude & Cicadas
    "B2.001": {
        "Dramatic Purpose / Emotional State": "Nature / Order inside nature",
        "SHARDA / CLARE — Position & Performance State": "Position: Window/Cell | Orientation: Listening | Action: Listens | Physical State: Peaceful | Internal State: Reflective",
        "SFX / Playback Layer": "Cicadas - very subtle filtering/resonance change to reveal order/chant. NO literal choir.",
        "Analog Synth Layer": "Maybe a distant tonal bed appears almost imperceptibly"
    },
    "B2.002": {
        "Dramatic Purpose / Emotional State": "Peace / Absence",
        "Analog Synth Layer": "NONE"
    },
    "B2.003": {
        "SHARDA / CLARE — Position & Performance State": "Position: Window/Cell | Orientation: Outward | Action: Quiet | Physical State: Peaceful | Internal State: Peaceful"
    },
    "B2.005": {
        "Dramatic Purpose / Emotional State": "Loneliness",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Inward | Action: Reflects | Physical State: Still | Internal State: Lonely",
        "Analog Synth Layer": "CUE - Mature loneliness tone (stable, slower, darker version of P3 Emptiness Motif)"
    },
    "B2.008": {
        "Dramatic Purpose / Emotional State": "Trust",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Upward/Outward | Action: Resolves | Physical State: Relaxing | Internal State: Trusting",
        "Analog Synth Layer": "Tone becomes a little more present on 'alone', then RELEASES on 'looking after me'"
    },
    "B2.009": {
        "SFX / Playback Layer": "Cicadas fade with sunrise"
    },
    
    # B3 Updates - Agnes Follows
    "B3.001": {
        "Dramatic Purpose / Emotional State": "Solitude",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Turning | Action: Coming out of prayer | Physical State: Prayerful | Internal State: Prayerful",
        "SFX / Playback Layer": "Cicadas faintly present or faded",
        "Analog Synth Layer": "NONE"
    },
    "B3.002": {
        "Dramatic Purpose / Emotional State": "Recognition",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Toward Agnes | Action: Sees Agnes | Physical State: Surprised | Internal State: Surprised",
        "Analog Synth Layer": "NONE (Let recognition be human)"
    },
    "B3.003": {
        "Dramatic Purpose / Emotional State": "Companionship",
        "Choir / Vocal Layer": "CUE - Agnes sings 'Jesus loves me' in Italian (Another human voice enters the world)",
        "Analog Synth Layer": "NONE"
    },
    "B3.004": {
        "Dramatic Purpose / Emotional State": "Companionship",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Toward Agnes | Action: Speaks | Physical State: Softened | Internal State: Disbelief / Joy",
        "Analog Synth Layer": "NONE (Keep dry)"
    },
    "B3.006": {
        "Dramatic Purpose / Emotional State": "Belonging",
        "SHARDA / CLARE — Position & Performance State": "Position: Cell | Orientation: Toward Agnes | Action: Dresses Agnes, embrace | Physical State: Connected | Internal State: Joyful / Connected",
        "Analog Synth Layer": "Optional very subtle warm sustained tone only if needed post-rehearsal"
    },
    "B3.007": {
        "Dramatic Purpose / Emotional State": "Belonging",
        "Choir / Vocal Layer": "CUE - Song Interlude ('Story of St Clare')"
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

print("Act II successfully updated in matrix!")
