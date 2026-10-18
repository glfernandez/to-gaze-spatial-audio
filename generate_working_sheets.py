import csv

master_file = "master_production_cue_matrix_v1.0_REHEARSAL_LOCK.csv"
rule_text = "# RULE: Do not add sound simply because a moment feels empty. Empty space is often the designed cue.\n"

def write_derived_sheet(filename, columns):
    with open(master_file, "r", encoding="utf-8") as f_in:
        reader = csv.DictReader(f_in)
        
        with open(filename, "w", newline="", encoding="utf-8") as f_out:
            f_out.write(rule_text)
            writer = csv.DictWriter(f_out, fieldnames=columns)
            writer.writeheader()
            
            for row in reader:
                filtered_row = {col: row[col] for col in columns}
                writer.writerow(filtered_row)
    print(f"Generated {filename}")

# 1. Stage Manager Cue Sheet
sm_cols = ["Beat ID", "Cue IN Trigger", "Standby / Operator Notes", "Cue OUT Trigger", "Transition / Next State"]
write_derived_sheet("SM_Cue_Sheet.csv", sm_cols)

# 2. Sound/Choir/Synth Sheet
sound_cols = ["Beat ID", "Full Script Text", "SFX / Playback Layer", "Analog Synth Layer", "Choir / Vocal Layer", "Design Status"]
write_derived_sheet("Sound_Choir_Synth_Sheet.csv", sound_cols)

# 3. Sharda Performance Score
sharda_cols = ["Beat ID", "Full Script Text", "Dramatic Purpose / Emotional State", "SHARDA / CLARE — Position & Performance State"]
write_derived_sheet("Sharda_Performance_Score.csv", sharda_cols)
