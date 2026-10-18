import csv
import re
from build_matrix import raw_beats
from strict_merge import extract_dialogue

headers = [
    "Beat ID", "Chapter", "Production Scene", "Full Script Text", 
    "Dramatic Purpose / Emotional State", "SHARDA / CLARE — Position & Performance State",
    "Other Performer / Staging Action", "Profile Light 1", "Profile Light 2",
    "Projector / Multimedia", "Choir / Vocal Layer", "SFX / Playback Layer",
    "Analog Synth Layer", "Cue IN Trigger", "Development / Behaviour",
    "Cue OUT Trigger", "Transition / Next State", "Standby / Operator Notes",
    "Design Status"
]

def get_new_scene(b_id):
    if b_id.startswith("P1."):
        n = int(b_id.split(".")[1])
        if n <= 8: return "P1 — Opening Breath / Modern World"
        if n <= 17: return "P2 — The Gaze / Prayer"
        if n <= 33: return "P3 — Clare Introduces Herself"
        return "P4 — Mother / God in the Poor"
    elif b_id.startswith("A1."):
        n = int(b_id.split(".")[1])
        if n <= 10: return "A1 — The Calling"
        return "A2 — The Passion"
    elif b_id.startswith("A2."):
        n = int(b_id.split(".")[1])
        if n <= 9: return "A3 — Palm Sunday / The Escape"
        return "A4 — The Tonsure / Dedication"
    elif b_id.startswith("B1."):
        n = int(b_id.split(".")[1])
        if n <= 10: return "B1 — Rebuilding San Damiano"
        return "B2 — Solitude & Cicadas"
    elif b_id.startswith("B2."):
        return "B3 — Agnes Follows"
    elif b_id.startswith("C1."):
        return "C1 — The Fire Within"
    elif b_id.startswith("C2."):
        return "C2 — The Sisterhood / Foot Washing"
    elif b_id.startswith("C3."):
        return "C3 — Caring for Francis"
    elif b_id.startswith("C4."):
        return "C4 — Death & Grief"
    elif b_id.startswith("D1."):
        n = int(b_id.split(".")[1])
        if n <= 7: return "D1 — First Letter"
        return "D2 — Soldiers / Siege"
    elif b_id.startswith("D2."):
        n = int(b_id.split(".")[1])
        if n <= 2: return "D3 — Eucharistic Stillness"
        return "D4 — Second Letter / Mirror"
    elif b_id.startswith("D3."):
        n = int(b_id.split(".")[1])
        if n <= 4: return "D5 — Agnes Tries to Feed Clare"
        return "D6 — Christmas Mass / Wonder"
    elif b_id.startswith("D4."):
        n = int(b_id.split(".")[1])
        if n <= 9: return "D7 — Third Letter"
        if n <= 20: return "D8 — Poverty / The Rule"
        return "D9 — Fourth Letter"
    elif b_id.startswith("E1."):
        return "E1 — The Final Gaze"
    return "UNKNOWN SCENE"

rows = []
scene_counters = {}

for beat in raw_beats:
    b_id, chap, old_scene, text = beat
    
    new_scene = get_new_scene(b_id)
    if new_scene not in scene_counters:
        scene_counters[new_scene] = 1
        
    prefix = new_scene.split(" — ")[0]
    new_b_id = f"{prefix}.{str(scene_counters[new_scene]).zfill(3)}"
    scene_counters[new_scene] += 1
    
    act_txt, script_txt = extract_dialogue(text)
    
    full_script = script_txt.replace("\n", " ") if script_txt else ""
    sharda_pos = "TBD - DIRECTORIAL | TBD - DIRECTORIAL | HOLD | TBD - DIRECTORIAL | TBD - DIRECTORIAL"
    other_pos = "HOLD"
    l1 = "HOLD"
    l2 = "HOLD"
    media = "NONE"
    choir = "NONE"
    sfx = "NONE"
    synth = "TBD"
    status = "TBD"
    op_notes = ""
    
    tl = act_txt.lower().strip() if act_txt else text.lower().strip()
    ref_txt = act_txt if act_txt else text
    ref_txt = ref_txt.replace("\n", " ")

    if act_txt or not script_txt:
        # Categorize the action
        if "media:" in tl or "multi media" in tl or "projector" in tl:
            if "lightning" in tl or "whisper" in tl:
                if "lightning" in tl:
                    l1 = "CUE - Lightning"
                    l2 = "CUE - Lightning"
                if "whisper" in tl:
                    sfx = "CUE - Possible whisper"
            else:
                media = "CUE - " + ref_txt
        elif "sound:" in tl or "sound design:" in tl or "sfx" in tl or "replicate a" in tl or "cicadas" in tl:
            sfx = "CUE - " + ref_txt
        elif "choir:" in tl or "song:" in tl or "music:" in tl or "hymn:" in tl:
            choir = "CUE - " + ref_txt
        elif "light:" in tl or "lighting action:" in tl or "black out" in tl:
            l1 = "CUE"
            l2 = "CUE"
            op_notes = ref_txt
        elif "francis signs" in tl or ("francis" in tl and "signs" in tl):
            other_pos = "Francis: (Signs his dialogue)"
            choir = "CUE - Choir voices Francis."
        else:
            if "francis" in tl or "agnes" in tl or "choir" in tl or "voice" in tl or "stage settings" in tl or "scene" in tl:
                other_pos = ref_txt
            else:
                sharda_pos = f"TBD - DIRECTORIAL | TBD - DIRECTORIAL | {ref_txt} | TBD - DIRECTORIAL | TBD - DIRECTORIAL"
        
        status = "CUE"
        
    if new_b_id == "P1.001":
        op_notes = ref_txt
        other_pos = "HOLD"
        sharda_pos = "TBD - DIRECTORIAL | TBD - DIRECTORIAL | HOLD | TBD - DIRECTORIAL | TBD - DIRECTORIAL"

    words = full_script.split()
    if words:
        cin = " ".join(words[:5]) + "..."
    else:
        if media != "NONE": cin = "On Media"
        elif sfx != "NONE": cin = "On Sound"
        elif choir != "NONE": cin = "On Choir"
        elif "HOLD" not in sharda_pos: cin = "On Action"
        elif other_pos != "HOLD": cin = "On Action"
        elif l1 != "HOLD": cin = "On Light"
        else: cin = "TBD"
        
    rows.append({
        "Beat ID": new_b_id,
        "Chapter": chap,
        "Production Scene": new_scene,
        "Full Script Text": full_script,
        "Dramatic Purpose / Emotional State": "TBD - DIRECTORIAL",
        "SHARDA / CLARE — Position & Performance State": sharda_pos,
        "Other Performer / Staging Action": other_pos,
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
        "Standby / Operator Notes": op_notes,
        "Design Status": status
    })

with open("master_production_cue_matrix.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)
    
print(f"Successfully generated 26-scene structured matrix with {len(rows)} beats.")
