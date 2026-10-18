import re
import csv

# 1. Update SFX_Master_Production_Cue_Sheet.csv
csv_file = 'SFX_Master_Production_Cue_Sheet.csv'
with open(csv_file, 'r', encoding='utf-8') as f:
    rows = list(csv.reader(f))

header = rows[0]
act_scene_idx = header.index('ACT / SCENE')
sfx_id_idx = header.index('SFX ID')

# Mapping logic based on Cue #, SFX ID, or old Act/Scene
for r in rows[1:]:
    cue_no = r[0]
    act_sc = r[act_scene_idx]
    sfx_id = r[sfx_id_idx]
    
    if 'P1' in act_sc:
        r[act_scene_idx] = '[Act 0, Sc 1] Christ on the Cross'
    elif 'A1' in act_sc:
        r[act_scene_idx] = '[Act I, Sc 2] The Meeting of Francis'
    elif 'A2' in act_sc:
        r[act_scene_idx] = '[Act I, Sc 3] The Escape'
    elif 'B1' in act_sc:
        r[act_scene_idx] = '[Act II, Sc 4] San Damiano'
    elif 'C2' in act_sc:
        r[act_scene_idx] = '[Act II, Sc 5] Sisterhood & Passing'
    elif 'D1' in act_sc:
        r[act_scene_idx] = '[Act III, Sc 6] Letters to Prague'
    elif 'D2' in act_sc:
        r[act_scene_idx] = '[Act III, Sc 7] The Siege'
    elif 'D6' in act_sc:
        if sfx_id in ('SFX-38', 'SFX-38_CHRISTMAS_MASS', 'SFX-23_PAPAL'):
            r[act_scene_idx] = '[Act IV, Sc 8] The Christmas Vision'
        elif sfx_id in ('SFX-30', 'SFX-30_CAUSTIC'):
            r[act_scene_idx] = '[Act IV, Sc 9] Final Gaze & Blackout'
        else:
            r[act_scene_idx] = '[Act IV, Sc 8] The Christmas Vision'
    elif 'FINAL' in act_sc:
        r[act_scene_idx] = '[Act IV, Sc 9] Final Gaze & Blackout'

with open(csv_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("SFX_Master_Production_Cue_Sheet.csv updated successfully!")

