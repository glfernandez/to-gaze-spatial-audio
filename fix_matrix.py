import csv
from build_matrix import raw_beats

headers = [
    "Beat ID", "Chapter", "Production Scene", "Full Script Text / Action",
    "Dramatic Purpose / Emotional State", "SHARDA / CLARE — Position & Performance State",
    "Other Performer / Staging Action", "Profile Light 1", "Profile Light 2",
    "Projector / Multimedia", "Choir / Vocal Layer", "SFX / Playback Layer",
    "Analog Synth Layer", "Cue IN Trigger", "Development / Behaviour",
    "Cue OUT Trigger", "Transition / Next State", "Standby / Operator Notes",
    "Design Status"
]

rows = []

for beat in raw_beats:
    b_id, chap, scene, text = beat
    
    purpose = "TBD - DIRECTORIAL"
    sharda = "HOLD"
    other = "HOLD"
    l1 = "HOLD"
    l2 = "HOLD"
    media = "NONE"
    choir = "NONE"
    sfx = "NONE"
    synth = "TBD"
    status = "TBD"
    
    tl = text.lower().strip()
    
    # We restore the full text to the script column to prevent any empty rows.
    # The column will act as a continuous read of the script, while cues are also broken out.
    script_val = text.replace("\n", "  ")
    
    # Parse Media
    if "media:" in tl or "media :" in tl or "multi media" in tl or "projector" in tl or "screen" in tl:
        media = "CUE - " + text.replace("\n", "  ")[:150]
        status = "CUE"
        
    # Parse SFX
    if "sound:" in tl or "sound design:" in tl or "sound " in tl or "sfx" in tl or "replicate a 13th" in tl:
        sfx = "CUE - " + text.replace("\n", "  ")[:150]
        status = "CUE"
        
    # Parse Choir & Francis Signing
    if "choir:" in tl or "song:" in tl or "music:" in tl or "hymn" in tl:
        choir = "CUE - " + text.replace("\n", "  ")[:150]
        status = "CUE"
        
    if "francis:" in tl:
        # Francis signs his dialogue!
        other = "Francis: (Signs his dialogue)"
        # The choir voices it.
        choir = "CUE - Choir voices Francis: " + text.replace("\n", "  ")[:100]
        status = "CUE"
        
    # Parse Lighting
    if "lighting action:" in tl or "light:" in tl:
        l1 = "CUE"
        l2 = "CUE"
        status = "CUE"
        
    # Parse Action/Staging
    if "action:" in tl or "movement:" in tl or "movement piece:" in tl or "beat." in tl or "silence." in tl:
        if "francis" in tl or "agnes" in tl or "choir" in tl:
            other = text.replace("\n", "  ")[:150]
        else:
            sharda = text.replace("\n", "  ")[:150]
        status = "CUE"
        
    if tl.startswith("(") and tl.endswith(")"):
        sharda = text.replace("\n", "  ")
        status = "CUE"
        
    # Specific overrides
    if b_id == "P1.001":
        other = "Francis seated stage right. Choir stage left."
        sharda = "Intermittently between 3 stations"
        status = "LOCKED"
    
    # Cue IN
    words = script_val.split()
    cin = " ".join(words[:5]) + "..." if words else "TBD"
        
    rows.append({
        "Beat ID": b_id,
        "Chapter": chap,
        "Production Scene": scene,
        "Full Script Text / Action": script_val,
        "Dramatic Purpose / Emotional State": purpose,
        "SHARDA / CLARE — Position & Performance State": sharda,
        "Other Performer / Staging Action": other,
        "Profile Light 1": l1,
        "Profile Light 2": l2,
        "Projector / Multimedia": media,
        "Choir / Vocal Layer": choir,
        "SFX / Playback Layer": sfx,
        "Analog Synth Layer": synth,
        "Cue IN Trigger": cin,
        "Development / Behaviour": "TBD",
        "Cue OUT Trigger": "TBD",
        "Transition / Next State": "TBD",
        "Standby / Operator Notes": "",
        "Design Status": status
    })

with open("master_production_cue_matrix.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)
    
print("Successfully regenerated master_production_cue_matrix.csv with fixed text and Francis signing!")
