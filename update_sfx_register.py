import csv

file_path = "sfx_asset_register.csv"
columns = [
    "Asset ID", "Scenes", "What we need", "Best source / Method", 
    "Generated/Recorded", "Filename", "Variation", "Duration", 
    "License/Provenance", "Approved", "Notes"
]

# We are updating the register to include the explicit sub-assets for Heartbeat and Breathing, 
# and setting all default approval statuses to 'NOT SOURCED'.

assets = [
    ("SFX-01A BREATH_SLEEP", "P1", "Low isolated breathing", "Record performer (temp/Sharda)"),
    ("SFX-01B BREATH_AWAKE", "P1", "Waking breath", "Record performer (temp/Sharda)"),
    ("SFX-01C BREATH_PRESSURE", "D2", "Breathing under stress", "Record performer (temp/Sharda)"),
    ("SFX-01D BREATH_RUNNING", "A3", "Increasing exertion", "Record performer (temp/Sharda)"),
    ("SFX-01E BREATH_RELIEF", "D4", "Post-siege aftermath", "Record performer (temp/Sharda)"),
    ("SFX-01F BREATH_FRAIL", "D6, D7", "Weak, failing breath", "Record performer (temp/Sharda)"),
    
    ("SFX-02 Modern mouse/click/interface", "P1", "Clicking, typing/interface fragments", "Record / CC0"),
    ("SFX-03 Traffic/city bed", "P1, D2", "Contemporary city texture", "AI/Licensed"),
    ("SFX-04 News/media fragments", "P1", "Speech fragments suggesting info overload", "Record custom voices!"),
    ("SFX-05 Ambulance/emergency", "P1", "Siren fragments, not dominant", "AI/Licensed"),
    ("SFX-06 Modern human voice fragments", "P1", "Ads, roles, instructions", "Record custom voices!"),
    ("SFX-07 P1 overload composite", "P1", "Designed accumulation of 02–06", "Build composite"),
    
    ("SFX-08 Historical/medieval atmosphere", "P3", "Very subtle period-world texture", "Library/field + design"),
    ("SFX-09 Assisi marketplace", "A1", "Horses, market, footsteps, distant activity", "Library + custom layering"),
    ("SFX-10 Palm Sunday crowd", "A2/A3", "Joyful public gathering + ominous undertone", "Library/custom crowd"),
    ("SFX-11 Night escape footsteps", "A3", "Fast feet on earth/stone", "Record Foley"),
    ("SFX-12 Clare's running breath", "A3", "Moved to SFX-01D", "Merged"),
    ("SFX-13 Rocky/muddy terrain", "A3", "Scrape, dirt, stone, footing", "Foley"),
    ("SFX-14 Door of the Dead impacts", "A3", "The critical BANG BANG BANG", "Record/design specifically"),
    ("SFX-15 Distant pursuit/guards", "A3", "Very restrained sense of pursuit", "Custom voices + Foley"),
    ("SFX-16 Shears/scissors hitting floor", "A4", "Heavy metallic impact with church resonance", "Record real prop in venue"),
    ("SFX-17 Tonsure cutting", "A4", "Hair/shears/fabric/breath", "Foley/live acoustic"),
    ("SFX-18 Lightning strike", "B1", "One short decisive event", "Library/design"),
    ("SFX-19 Cicada field", "B1/B2/B3", "Long clean nature recording", "High-quality field recording"),
    ("SFX-20 Cicada transformation stem", "B2", "Filterable/resonant derivative", "Process SFX-19"),
    ("SFX-21 Water pour/bowl", "C1/C2/C3", "Intimate pouring/washing", "Live/onstage + optional reinforcement"),
    ("SFX-22 Cloth/fabric/foot washing", "C2/C3", "Subtle tactile acoustic detail", "Live/Foley"),
    ("SFX-23 Pen/paper scratching", "D1", "Very intimate writing texture", "Live/Foley"),
    ("SFX-24 Siege soldiers/mercenaries", "D2", "Approaching armed force", "Custom-designed composite"),
    ("SFX-25 Sisters' panic voices", "D2", "“What do we do…”, fear", "Record cast/choir"),
    ("SFX-26 Timeless war/modern bleed", "D2", "War mixed with traffic/phone traces", "AI/design"),
    ("SFX-27 Soldiers retreating", "D3", "Density withdrawing into distance", "Derived from siege stems"),
    ("SFX-28 Bowl/food/falling-body Foley", "D5", "Human frailty", "Live/Foley"),
    ("SFX-29 Distant Christmas bells", "D6", "First impossible signal", "Licensed recording"),
    ("SFX-30 Mass congregation/liturgy", "D6", "Distant→present congregation/prayer", "Record bespoke ensemble"),
    ("SFX-31 Great organ layer", "D6", "Large sacred-space expansion", "Licensed/recorded"),
    ("SFX-32 Christmas Mass composite", "D6", "Bells + liturgy + congregation + organ", "Full designed composite"),
    
    ("SFX-33A HB_CANONICAL_SOURCE", "A2/A3/D4/D6", "The master heartbeat recording", "Record/Design"),
    ("SFX-33B HB_FORMATION", "A2", "Slow, warm, soft attack", "Process SFX-33A"),
    ("SFX-33C HB_ALIVE", "A2", "Clearer and slightly stronger", "Process SFX-33A"),
    ("SFX-33D HB_ESCAPE", "A3", "Faster, tighter, more percussive", "Process SFX-33A"),
    ("SFX-33E HB_AFTERMATH", "D3/D4", "Fast but decelerating", "Process SFX-33A"),
    ("SFX-33F HB_FRAILTY", "D6/D8", "Slow, weak, intimate", "Process SFX-33A"),

    ("SFX-34 Venue room tone", "Entire show", "Actual church acoustic", "Record in the actual church")
]

with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    for asset in assets:
        row = [
            asset[0], asset[1], asset[2], asset[3],
            "", "", "", "", "Source/License/URL:", "NOT SOURCED", ""
        ]
        writer.writerow(row)

print(f"Updated {file_path} with Batch 1 granular breakdown and NOT SOURCED statuses.")
