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

pure_actions = [
    "francis slowly rises from his seat",
    "clare slowly gets off the bed",
    "clare walks to francis",
    "slowly all the noises",
    "francis bows and takes his seat",
    "clare gazes at christ",
    "she watches him",
    "she gives a little disbelieving laugh",
    "clare weaves in and out",
    "francis turns to see clare",
    "a male choir member hands clare",
    "clare walks into her cell",
    "clare walks slowly into her cell",
    "she is quiet",
    "francis and her gaze at each other",
    "francis remains on stage",
    "agnes places the bowl",
    "clare gestures to agnes",
    "she becomes more solemn",
    "she dries the audience members",
    "clare smiles, followed by silence",
    "francis walks and sits",
    "the song is sung and she washes",
    "and then one day, francis was gone",
    "once francis is completely",
    "clare walks to her desk",
    "she looks towards christ",
    "clare is deteriorating physically",
    "the media plays",
    "she kneels down",
    "clare hears the voice",
    "the only sound left",
    "she is writing but is frail",
    "she drops her pen",
    "clare’s sister agnes comes onto stage",
    "clare falls down each time",
    "agnes leaves",
    "she laughs softly",
    "a moment of silence",
    "then—a holy light begins",
    "she kneels in prayer",
    "clare is looking up",
    "clare looks at the audience"
]

def extract_dialogue(text):
    tl = text.lower().strip()
    
    if tl.startswith("media:") or tl.startswith("media :") or tl.startswith("multi media") or tl.startswith("projector") or tl.startswith("replicate a") or "stage settings" in tl or tl.startswith("scene 1") or tl.startswith("scene 2") or tl.startswith("scene 3") or tl.startswith("scene 4") or tl.startswith("act ") or tl.startswith("epilogue") or tl.startswith("11 august") or tl.startswith("two days earlier") or tl.startswith("pope innocent") or tl.startswith("the first rule") or tl.startswith("action:") or tl.startswith("movement:") or tl.startswith("lighting") or tl.startswith("light:") or tl.startswith("sound:") or tl.startswith("sound design:") or tl.startswith("sound ") or tl.startswith("sfx") or tl.startswith("choir:") or tl.startswith("song:") or tl.startswith("music:"):
        if "francis:" in tl: return ("Francis signs his dialogue.", text)
        if "sound of voices :" in tl: return ("", text)
        return (text, "")
        
    if tl.startswith("(") and tl.endswith(")"):
        return (text, "")
    if tl == "beat." or tl == "silence." or tl == "(silence)":
        return (text, "")
        
    for pa in pure_actions:
        if tl.startswith(pa):
            parts = text.split("\n", 1)
            if len(parts) > 1: return (parts[0], parts[1])
            else: return (text, "")
            
    if tl.startswith("she smiles.") or tl.startswith("she looks at the audience."):
        parts = text.split("\n", 1)
        if len(parts) > 1: return (parts[0], parts[1])
        else: return (text, "")
        
    if text.startswith("CLARE: (Holding a Palm"):
        parts = text.split("\n", 1)
        if len(parts) > 1: return ("Clare holds a Palm and waves it.", parts[1])
        return ("Clare holds a Palm and waves it.", "")
        
    return ("", text)

for beat in raw_beats:
    b_id, chap, scene, text = beat
    
    if not current_row:
        current_row = create_row(chap, scene)
        
    if current_row["Chapter"] != chap or current_row["Production Scene"] != scene:
        if current_row["Full Script Text"] or current_row["Action / Stage Directions"]:
            if not current_row["Full Script Text"]:
                current_row["Full Script Text"] = "[Scene Action / Transition]"
            rows.append(current_row)
        current_row = create_row(chap, scene)
        
    act_txt, script_txt = extract_dialogue(text)
    
    if act_txt:
        atl = act_txt.lower()
        if atl.startswith("media:") or atl.startswith("media :") or atl.startswith("multi media") or atl.startswith("11 august") or atl.startswith("two days earlier") or atl.startswith("pope innocent") or atl.startswith("the first rule"):
            current_row["Projector / Multimedia"].append("CUE - " + act_txt)
        elif atl.startswith("sound:") or atl.startswith("sound design:") or atl.startswith("sound ") or atl.startswith("sfx") or atl.startswith("replicate a 13th"):
            current_row["SFX / Playback Layer"].append("CUE - " + act_txt)
        elif atl.startswith("choir:") or atl.startswith("song:") or atl.startswith("music:") or atl.startswith("hymn"):
            current_row["Choir / Vocal Layer"].append("CUE - " + act_txt)
        elif atl.startswith("lighting action:") or atl.startswith("light:"):
            current_row["Profile Light 1"] = "CUE"
            current_row["Profile Light 2"] = "CUE"
            current_row["Action / Stage Directions"].append(act_txt)
        elif "francis signs" in atl:
            current_row["Action / Stage Directions"].append("Francis signs his dialogue.")
            current_row["Other Performer / Staging Action"].append("Francis: (Signs his dialogue)")
            current_row["Choir / Vocal Layer"].append("CUE - Choir voices Francis.")
        else:
            current_row["Action / Stage Directions"].append(act_txt)
            if "francis" in atl or "agnes" in atl or "choir" in atl:
                current_row["Other Performer / Staging Action"].append(act_txt)
            else:
                current_row["SHARDA / CLARE — Position & Performance State"].append(act_txt)
                
    if script_txt:
        current_row["Full Script Text"] += (" " if current_row["Full Script Text"] else "") + script_txt.replace("\n", " ")
        rows.append(current_row)
        current_row = create_row(chap, scene)

if current_row and (current_row["Full Script Text"] or current_row["Action / Stage Directions"]):
    if not current_row["Full Script Text"]:
        current_row["Full Script Text"] = "[Scene Action / Transition]"
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
    
print("Successfully regenerated master_production_cue_matrix.csv with strict dialogue separation!")
