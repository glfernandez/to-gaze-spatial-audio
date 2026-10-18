import csv
import re
from build_matrix import raw_beats

headers = [
    "Beat ID", "Chapter", "Production Scene", "Full Script Text", "Action / Stage Directions",
    "Dramatic Purpose / Emotional State", "SHARDA / CLARE — Position & Performance State",
    "Other Performer / Staging Action", "Profile Light 1", "Profile Light 2",
    "Projector / Multimedia", "Choir / Vocal Layer", "SFX / Playback Layer",
    "Analog Synth Layer", "Cue IN Trigger", "Development / Behaviour",
    "Cue OUT Trigger", "Transition / Next State", "Standby / Operator Notes",
    "Design Status"
]

rows = []

def create_row(chap, scene):
    return {
        "Beat ID": "", "Chapter": chap, "Production Scene": scene, "Full Script Text": "", 
        "Action / Stage Directions": [], "Dramatic Purpose / Emotional State": "TBD - DIRECTORIAL", 
        "SHARDA / CLARE — Position & Performance State": [], "Other Performer / Staging Action": [], 
        "Profile Light 1": "HOLD", "Profile Light 2": "HOLD", "Projector / Multimedia": [], 
        "Choir / Vocal Layer": [], "SFX / Playback Layer": [], "Analog Synth Layer": "TBD", 
        "Cue IN Trigger": "TBD", "Development / Behaviour": "TBD", "Cue OUT Trigger": "TBD", 
        "Transition / Next State": "TBD", "Standby / Operator Notes": "", "Design Status": "TBD"
    }

current_row = None
beat_counter = 1

for beat in raw_beats:
    b_id, chap, scene, text = beat
    
    if not current_row:
        current_row = create_row(chap, scene)
        
    if current_row["Chapter"] != chap or current_row["Production Scene"] != scene:
        if current_row["Full Script Text"] or current_row["Action / Stage Directions"]:
            if not current_row["Full Script Text"]:
                current_row["Full Script Text"] = "[Scene Action]"
            rows.append(current_row)
        current_row = create_row(chap, scene)
        beat_counter = 1
        
    tl = text.lower().strip()
    is_script = True
    
    # Classify
    if tl.startswith("media:") or tl.startswith("media :") or tl.startswith("multi media") or tl.startswith("projector") or tl.startswith("screen") or tl.startswith("11 august") or tl.startswith("two days earlier") or tl.startswith("pope innocent") or tl.startswith("the first rule"):
        current_row["Projector / Multimedia"].append(text)
        is_script = False
    elif tl.startswith("sound:") or tl.startswith("sound design:") or tl.startswith("sound ") or tl.startswith("sfx") or tl.startswith("replicate a 13th"):
        current_row["SFX / Playback Layer"].append(text)
        is_script = False
    elif tl.startswith("choir:") or tl.startswith("song:") or tl.startswith("music:") or tl.startswith("hymn"):
        current_row["Choir / Vocal Layer"].append(text)
        is_script = False
    elif "francis:" in tl:
        current_row["Action / Stage Directions"].append("Francis signs his dialogue.")
        current_row["Other Performer / Staging Action"].append("Francis: (Signs his dialogue)")
        current_row["Choir / Vocal Layer"].append("Choir voices Francis: " + text)
        current_row["Full Script Text"] += (" " if current_row["Full Script Text"] else "") + text
        rows.append(current_row)
        current_row = create_row(chap, scene)
        is_script = False 
    elif tl.startswith("lighting action:") or tl.startswith("light:"):
        current_row["Profile Light 1"] = "CUE"
        current_row["Profile Light 2"] = "CUE"
        current_row["Action / Stage Directions"].append(text)
        is_script = False
    elif tl.startswith("action:") or tl.startswith("movement:") or tl.startswith("movement piece:") or tl.startswith("(") or tl == "beat." or tl == "silence." or tl == "(silence)" or "stage settings" in tl or "scene " in tl or "act " in tl or tl.startswith("epilogue") or tl.startswith("clare walks") or tl.startswith("she drops") or tl.startswith("clare slowly") or tl.startswith("clare weaves") or tl.startswith("she watches") or tl.startswith("she gives") or tl.startswith("she kneels") or tl.startswith("she laughs"):
        current_row["Action / Stage Directions"].append(text)
        if "francis" in tl or "agnes" in tl or "choir" in tl:
            current_row["Other Performer / Staging Action"].append(text)
        else:
            current_row["SHARDA / CLARE — Position & Performance State"].append(text)
        is_script = False
        
    if is_script:
        parts = text.split("\n", 1)
        if len(parts) > 1:
            first_tl = parts[0].lower().strip()
            if first_tl in ["she smiles.", "she looks at the audience.", "she becomes more solemn.", "she is quiet", "beat.", "silence."] or (first_tl.startswith("(") and first_tl.endswith(")")):
                current_row["Action / Stage Directions"].append(parts[0])
                current_row["SHARDA / CLARE — Position & Performance State"].append(parts[0])
                current_row["Full Script Text"] += (" " if current_row["Full Script Text"] else "") + parts[1].replace("\n", " ")
            else:
                current_row["Full Script Text"] += (" " if current_row["Full Script Text"] else "") + text.replace("\n", " ")
        else:
            current_row["Full Script Text"] += (" " if current_row["Full Script Text"] else "") + text.replace("\n", " ")
            
        rows.append(current_row)
        current_row = create_row(chap, scene)

if current_row and (current_row["Full Script Text"] or current_row["Action / Stage Directions"]):
    if not current_row["Full Script Text"]:
        current_row["Full Script Text"] = "[Scene Action]"
    rows.append(current_row)

for i, r in enumerate(rows):
    prefix = "X"
    if r["Chapter"] == "PROLOGUE": prefix = "P"
    elif r["Chapter"] == "ACT I": prefix = "A"
    elif r["Chapter"] == "ACT II": prefix = "B"
    elif r["Chapter"] == "ACT III": prefix = "C"
    elif r["Chapter"] == "ACT IV": prefix = "D"
    elif r["Chapter"] == "EPILOGUE": prefix = "E"
    
    m = re.search(r'Scene (\d+)', r["Production Scene"])
    s_num = m.group(1) if m else "1"
    r["Beat ID"] = f"{prefix}{s_num}.{str(i+1).zfill(3)}"
    
    for k in ["Action / Stage Directions", "SHARDA / CLARE — Position & Performance State", "Other Performer / Staging Action", "Projector / Multimedia", "Choir / Vocal Layer", "SFX / Playback Layer"]:
        r[k] = " | ".join(r[k]) if r[k] else ("NONE" if k in ["Projector / Multimedia", "Choir / Vocal Layer", "SFX / Playback Layer"] else "HOLD")
        
    if r["Action / Stage Directions"] != "HOLD" or r["Projector / Multimedia"] != "NONE" or r["Choir / Vocal Layer"] != "NONE" or r["SFX / Playback Layer"] != "NONE":
        r["Design Status"] = "CUE"
        
    words = r["Full Script Text"].split()
    if words and words[0] != "[Scene":
        r["Cue IN Trigger"] = " ".join(words[:5]) + "..."
    else:
        r["Cue IN Trigger"] = "On Action/Media"

with open("master_production_cue_matrix.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)
    
print("Successfully regenerated master_production_cue_matrix.csv with merged script rows and Action column!")
