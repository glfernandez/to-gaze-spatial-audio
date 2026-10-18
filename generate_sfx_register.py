import csv

file_path = "sfx_asset_register.csv"
columns = [
    "Asset ID", "Scenes", "What we need", "Best source / Method", 
    "Generated/Recorded", "Filename", "Variation", "Duration", 
    "License/Provenance", "Approved", "Notes"
]

assets = [
    ("SFX-01 Human breathing", "P1, D4, D6", "Low isolated breathing, several intensities", "Record Sharda / performer"),
    ("SFX-02 Modern mouse/click/interface sounds", "P1", "Clicking, typing/interface fragments", "Record / CC0"),
    ("SFX-03 Traffic/city bed", "P1, D2", "Contemporary city texture", "Licensed field recording"),
    ("SFX-04 News/media fragments", "P1", "Speech fragments suggesting information overload", "Record custom voices, then abstract/process"),
    ("SFX-05 Ambulance/emergency texture", "P1", "Siren fragments, not dominant", "Licensed/recorded"),
    ("SFX-06 Modern human voice fragments", "P1", "Ads, roles, instructions, consumer chatter", "Custom-recorded"),
    ("SFX-07 P1 overload composite", "P1", "Designed accumulation of 02–06", "Build composite, not one AI file"),
    ("SFX-08 Historical/medieval atmosphere", "P3", "Very subtle period-world texture", "Library/field + design"),
    ("SFX-09 Assisi marketplace", "A1", "Horses, market, footsteps, distant activity", "Library + custom layering"),
    ("SFX-10 Palm Sunday crowd", "A2/A3", "Joyful public gathering with slightly ominous undertone", "Library/custom crowd"),
    ("SFX-11 Night escape footsteps", "A3", "Fast feet on earth/stone", "Record Foley"),
    ("SFX-12 Clare's running breath", "A3", "Increasing exertion", "Record performer"),
    ("SFX-13 Rocky/muddy terrain", "A3", "Scrape, dirt, stone, footing", "Foley"),
    ("SFX-14 Door of the Dead impacts", "A3", "The critical BANG BANG BANG", "Record/design specifically"),
    ("SFX-15 Distant pursuit/guards", "A3", "Very restrained sense of pursuit", "Custom voices + Foley"),
    ("SFX-16 Shears/scissors hitting floor", "A4", "Heavy metallic impact with church resonance", "Record real prop in venue if possible"),
    ("SFX-17 Tonsure cutting", "A4", "Hair/shears/fabric/breath", "Foley/live acoustic"),
    ("SFX-18 Lightning strike", "B1", "One short decisive event, no cinematic rolling thunder", "Library/design"),
    ("SFX-19 Cicada field", "B1/B2/B3", "Long clean nature recording", "High-quality field recording"),
    ("SFX-20 Cicada transformation stem", "B2", "Filterable/resonant derivative for “Deus Deus Deus” perception", "Process SFX-19"),
    ("SFX-21 Water pour/bowl", "C1/C2/C3", "Intimate pouring/washing", "Prefer live/onstage sound + optional reinforcement"),
    ("SFX-22 Cloth/fabric/foot washing", "C2/C3", "Subtle tactile acoustic detail", "Live/Foley"),
    ("SFX-23 Pen/paper scratching", "D1", "Very intimate writing texture", "Live or Foley recording"),
    ("SFX-24 Siege soldiers/mercenaries", "D2", "Approaching armed force", "Custom-designed composite"),
    ("SFX-25 Sisters' panic voices", "D2", "“What do we do…”, fear around Clare", "Record cast/choir"),
    ("SFX-26 Timeless war/modern bleed", "D2", "War mixed with traffic/phone traces; P1 callback", "AI/design excellent here"),
    ("SFX-27 Soldiers retreating", "D3", "Density withdrawing into distance", "Derived from siege stems"),
    ("SFX-28 Bowl/food/falling-body Foley", "D5", "Human frailty: bowl, fabric, foot shifts, falls", "Live/Foley"),
    ("SFX-29 Distant Christmas bells", "D6", "First impossible signal from outside", "Licensed recording / recorded church bells"),
    ("SFX-30 Mass congregation/liturgy atmosphere", "D6", "Distant→present congregation/prayer", "Record bespoke ensemble if possible"),
    ("SFX-31 Great organ layer", "D6", "Large sacred-space expansion", "Licensed/recorded"),
    ("SFX-32 Christmas Mass composite", "D6", "Bells + liturgy + congregation + organ + spatial expansion", "Full designed composite"),
    ("SFX-33 Clare heartbeat", "A2/A3/D4/D6", "One recurring biological identity with variants", "Record/design one canonical source"),
    ("SFX-34 Venue room tone", "Entire show", "Actual church acoustic at silence moments", "Record in the actual church")
]

with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    for asset in assets:
        row = [
            asset[0], asset[1], asset[2], asset[3],
            "", "", "", "", "", "NO", ""
        ]
        writer.writerow(row)

print(f"Created {file_path} with 34 master asset stems.")
