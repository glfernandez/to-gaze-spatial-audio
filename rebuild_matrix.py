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
    script_val = ""
    
    tl = text.lower().strip()
    is_pure = False
    
    if tl.startswith("media:") or tl.startswith("media :") or tl.startswith("multi media"):
        media = text
        is_pure = True
    elif tl.startswith("sound:") or tl.startswith("sound design:") or tl.startswith("sound ") or tl.startswith("sfx"):
        sfx = text
        is_pure = True
    elif tl.startswith("action:") or tl.startswith("movement:") or tl.startswith("movement piece:"):
        if "francis" in tl or "agnes" in tl or "choir" in tl:
            other = text
        else:
            sharda = text
        is_pure = True
    elif tl.startswith("lighting action:") or tl.startswith("light:"):
        l1 = text
        l2 = text
        is_pure = True
    elif tl.startswith("choir:") or tl.startswith("song:") or tl.startswith("music:"):
        choir = text
        is_pure = True
    elif tl.startswith("voice of christ"):
        script_val = text
        is_pure = True # wait, this is dialogue, so we want it in script_val. We set is_pure=True to bypass the default assignment, but wait, if it's dialogue, it shouldn't be pure. Let's handle it properly.
        is_pure = False
    elif tl.startswith("clare walks") or tl.startswith("clare slowly") or tl.startswith("she drops") or tl.startswith("clare is") or tl.startswith("clare weaves") or tl.startswith("she watches") or tl.startswith("she gives") or tl.startswith("she kneels") or tl.startswith("she laughs"):
        sharda = text
        is_pure = True
    elif tl.startswith("francis ") or tl.startswith("agnes ") or tl.startswith("a male choir") or tl.startswith("sean "):
        if ":" not in text.split(" ")[0] and "francis:" not in tl:
            other = text
            is_pure = True
    elif tl == "beat." or tl == "silence." or tl == "(silence)":
        sharda = text
        is_pure = True
    elif tl.startswith("(") and tl.endswith(")"):
        sharda = text
        is_pure = True
    elif "stage settings" in tl or "scene 1:" in tl or "scene 2" in tl or "scene 3" in tl or "scene 4" in tl or tl == "act 2" or tl == "act 3" or tl == "act 4" or tl.startswith("epilogue"):
        other = text
        is_pure = True
    elif tl.startswith("11 august") or tl.startswith("two days earlier") or tl.startswith("pope innocent") or tl.startswith("the first rule"):
        media = text
        is_pure = True
    elif tl.startswith("replicate a 13th"):
        sfx = text
        is_pure = True
        
    if not is_pure:
        parts = text.split("\n", 1)
        if len(parts) > 1:
            first_tl = parts[0].lower().strip()
            if first_tl in ["she smiles.", "she looks at the audience.", "she becomes more solemn.", "she is quiet", "beat.", "silence."]:
                sharda = parts[0]
                script_val = parts[1]
            elif first_tl.startswith("(") and first_tl.endswith(")"):
                sharda = parts[0]
                script_val = parts[1]
            else:
                script_val = text
        else:
            script_val = text

    if b_id == "P1.001":
        other = text
        script_val = ""
        is_pure = True
    
    if media != "NONE" or sfx != "NONE" or choir != "NONE" or sharda != "HOLD" or other != "HOLD" or l1 != "HOLD":
        status = "CUE"
        
    # Replace newlines with spaces for clean CSV
    script_val = script_val.replace("\n", "  ")
    media = media.replace("\n", "  ")
    sfx = sfx.replace("\n", "  ")
    choir = choir.replace("\n", "  ")
    sharda = sharda.replace("\n", "  ")
    other = other.replace("\n", "  ")
    l1 = l1.replace("\n", "  ")
    l2 = l2.replace("\n", "  ")
    
    words = script_val.split()
    cin = " ".join(words[:5]) + "..." if words else "TBD"
    if not words:
        if sharda != "HOLD": cin = "On Action"
        elif media != "NONE": cin = "On Media"
        elif sfx != "NONE": cin = "On Sound"
        elif choir != "NONE": cin = "On Choir"
        elif other != "HOLD": cin = "On Action"
        
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
    
print("Successfully regenerated master_production_cue_matrix.csv with separated columns!")
