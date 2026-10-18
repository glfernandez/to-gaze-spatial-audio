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

def format_sharda(action_text):
    if not action_text or action_text == "HOLD":
        act = "HOLD"
    else:
        act = action_text
    return f"Position: TBD - DIRECTORIAL | Orientation: TBD - DIRECTORIAL | Action: {act} | Physical State: TBD - DIRECTORIAL | Internal State: TBD - DIRECTORIAL"

def determine_scene(chap, text, current_scene):
    tl = text.lower()
    
    # 1. Enforce Chapter Baselines (Fixes boundary leaking)
    if chap == "ACT I" and not current_scene.startswith("A"):
        return "A1 — The Meeting of Francis"
    if chap == "ACT II" and not current_scene.startswith("B"):
        return "B1 — Rebuilding San Damiano"
    if chap == "ACT III" and not current_scene.startswith("C"):
        return "C1 — The Fire Within"
    if chap == "ACT IV" and not current_scene.startswith("D"):
        return "D1 — First Letter"
    if chap == "EPILOGUE" and not current_scene.startswith("E"):
        return "E1 — The Final Gaze"
        
    # 2. Sequential intra-chapter triggers
    if chap == "PROLOGUE":
        if current_scene == "P1 — Opening Breath / Modern World" and "clare slowly gets off the bed" in tl: return "P2 — The Gaze / Prayer"
        if current_scene in ["P1 — Opening Breath / Modern World", "P2 — The Gaze / Prayer"] and "when i came to know him" in tl: return "P3 — Clare Introduces Herself"
        if current_scene in ["P1 — Opening Breath / Modern World", "P2 — The Gaze / Prayer", "P3 — Clare Introduces Herself"] and ("but i was loved" in tl or "mama ortolana" in tl): return "P4 — Mother / God in the Poor"
        
    elif chap == "ACT I":
        if current_scene == "A1 — The Meeting of Francis" and ("the treasure of blessed poverty" in tl or "i didn't see this madness" in tl): return "A2 — The Passion"
        if current_scene in ["A1 — The Meeting of Francis", "A2 — The Passion"] and ("it was palm sunday" in tl or "(holding a palm" in tl): return "A3 — Palm Sunday / The Escape"
        if current_scene in ["A1 — The Meeting of Francis", "A2 — The Passion", "A3 — Palm Sunday / The Escape"] and ("the swinging of the scissors" in tl or "once this is cut" in tl): return "A4 — The Tonsure / Dedication"
        
    elif chap == "ACT II":
        if current_scene == "B1 — Rebuilding San Damiano" and ("sound of the cicadas begins" in tl or "if you listen closely to the sound of the cicadas" in tl): return "B2 — Solitude & Cicadas"
        if current_scene in ["B1 — Rebuilding San Damiano", "B2 — Solitude & Cicadas"] and "and then one day, as i slowly came out" in tl: return "B3 — Agnes Follows"
        
    elif chap == "ACT III":
        if current_scene == "C1 — The Fire Within" and ("our sisterhood was growing" in tl or "other women of my time" in tl): return "C2 — The Sisterhood / Foot Washing"
        if current_scene in ["C1 — The Fire Within", "C2 — The Sisterhood / Foot Washing"] and "through it all, i had francis" in tl: return "C3 — Caring for Francis"
        if current_scene in ["C1 — The Fire Within", "C2 — The Sisterhood / Foot Washing", "C3 — Caring for Francis"] and ("and then one day, francis was gone" in tl or "when francis passed on" in tl): return "C4 — Death & Grief"
        
    elif chap == "ACT IV":
        if current_scene == "D1 — First Letter" and ("sound of the soldiers" in tl or ("sound:" in tl and "soldiers" in tl)): return "D2 — Soldiers / Siege"
        if current_scene == "D2 — Soldiers / Siege" and ("scene 2:" in tl or "she kneels in prayer" in tl): return "D3 — Eucharistic Stillness"
        if current_scene in ["D1 — First Letter", "D2 — Soldiers / Siege", "D3 — Eucharistic Stillness"] and "multi media older clare (letter 2)" in tl: return "D4 — Second Letter / Mirror"
        if current_scene == "D4 — Second Letter / Mirror" and ("sister agnes comes onto stage" in tl or ("agnes:" in tl and "sister, please eat" in tl)): return "D5 — Agnes Tries to Feed Clare"
        if current_scene == "D5 — Agnes Tries to Feed Clare" and ("let us get ready for christmas eve mass" in tl or "a holy light begins" in tl): return "D6 — Christmas Mass / Wonder"
        if current_scene == "D6 — Christmas Mass / Wonder" and "older clare (letter three):" in tl: return "D7 — Third Letter"
        if current_scene == "D7 — Third Letter" and ("you might wonder, ‘but why clare?" in tl or "clare:\nwe are coming close" in tl): return "D8 — Poverty / The Rule"
        if current_scene == "D8 — Poverty / The Rule" and "clare ( fourth letter)" in tl: return "D9 — Fourth Letter"
        
    return current_scene

rows = []
scene_counters = {}
current_scene = "P1 — Opening Breath / Modern World"

for beat in raw_beats:
    b_id, chap, old_scene, text = beat
    
    current_scene = determine_scene(chap, text, current_scene)
    
    if current_scene not in scene_counters:
        scene_counters[current_scene] = 1
        
    prefix = current_scene.split(" — ")[0]
    new_b_id = f"{prefix}.{str(scene_counters[current_scene]).zfill(3)}"
    scene_counters[current_scene] += 1
    
    # 1. ALWAYS populate Full Script Text with original text
    full_script = text.replace("\n", " ")
    
    act_txt, script_txt = extract_dialogue(text)
    
    sharda_act = "HOLD"
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
    ref_txt = act_txt.replace("\n", " ") if act_txt else text.replace("\n", " ")

    if act_txt or not script_txt:
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
                sharda_act = ref_txt
        status = "CUE"
        
    if new_b_id == "P1.001":
        op_notes = ref_txt
        other_pos = "HOLD"
        sharda_act = "HOLD"

    words = full_script.split()
    if words:
        cin = " ".join(words[:5]) + "..."
    else:
        cin = "TBD"
        
    rows.append({
        "Beat ID": new_b_id,
        "Chapter": chap,
        "Production Scene": current_scene,
        "Full Script Text": full_script,
        "Dramatic Purpose / Emotional State": "TBD - DIRECTORIAL",
        "SHARDA / CLARE — Position & Performance State": format_sharda(sharda_act),
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
    
print(f"Successfully generated matrix with strict chapter boundaries.")
