import csv
import os

# 1. Expand the Asset Register
asset_manifest = [
    # GLOBAL
    {"id": "SFX-01A", "name": "Breathing - Sleep", "folder": "GLOBAL/breathing"},
    {"id": "SFX-01B", "name": "Breathing - Awake", "folder": "GLOBAL/breathing"},
    {"id": "SFX-01C", "name": "Breathing - Pressure", "folder": "GLOBAL/breathing"},
    {"id": "SFX-01D", "name": "Breathing - Running", "folder": "GLOBAL/breathing"},
    {"id": "SFX-01E", "name": "Breathing - Relief", "folder": "GLOBAL/breathing"},
    {"id": "SFX-01F", "name": "Breathing - Frail", "folder": "GLOBAL/breathing"},
    {"id": "SFX-33A", "name": "Heartbeat - Canonical", "folder": "GLOBAL/heartbeat", "status": "SHORTLIST"},
    
    # P1 WORLD
    {"id": "SFX-02", "name": "Mouse Clicks", "folder": "P1_WORLD/clicks", "status": "SHORTLIST"},
    {"id": "SFX-03", "name": "City Traffic", "folder": "P1_WORLD/traffic", "status": "SHORTLIST"},
    {"id": "SFX-05", "name": "Ambulance Siren", "folder": "P1_WORLD/emergency", "status": "SHORTLIST"},
    {"id": "SFX-07", "name": "Sub-bass rumble overload", "folder": "P1_WORLD/rumble", "query": "low frequency cinematic rumble sound effect royalty free"},
    
    # ACT I
    {"id": "SFX-08", "name": "Marketplace Ambience", "folder": "ACT_I/market", "query": "medieval market crowd ambience field recording royalty free"},
    {"id": "SFX-09", "name": "Coins on Table", "folder": "ACT_I/market", "query": "heavy coins dropping on wooden table sound effect royalty free"},
    {"id": "SFX-10", "name": "Heavy Door Open/Close", "folder": "ACT_I/escape", "query": "heavy old wooden door opening closing sound effect royalty free"},
    {"id": "SFX-11", "name": "Footsteps on Stone", "folder": "ACT_I/escape", "query": "footsteps running on stone cobblestone sound effect royalty free"},
    {"id": "SFX-12", "name": "Door of the Dead Impact", "folder": "ACT_I/escape", "query": "heavy massive door slam impact sound effect royalty free"},
    {"id": "SFX-13", "name": "Iron Shears Cutting", "folder": "ACT_I/tonsure", "query": "heavy iron scissors shears cutting hair cloth sound effect royalty free"},
    
    # ACT II & III
    {"id": "SFX-15", "name": "Cicadas", "folder": "ACT_II_III/san_damiano", "query": "cicadas summer night field recording royalty free"},
    {"id": "SFX-16", "name": "Water Pouring into Bowl", "folder": "ACT_II_III/washing", "query": "water pouring into ceramic wooden bowl sound effect royalty free"},
    {"id": "SFX-17", "name": "Wet Cloth Washing", "folder": "ACT_II_III/washing", "query": "wet cloth squeezing washing sound effect royalty free"},
    
    # ACT IV
    {"id": "SFX-18", "name": "Distant Soldiers Marching", "folder": "ACT_IV/siege", "query": "medieval soldiers marching armor clanking royalty free"},
    {"id": "SFX-19", "name": "Timeless War Bleed", "folder": "ACT_IV/siege", "query": "distant battle sounds chaotic war royalty free"},
    {"id": "SFX-20", "name": "Christmas Church Bells", "folder": "ACT_IV/mass", "query": "distant church bells ringing mass royalty free"},
    {"id": "SFX-21", "name": "Congregation Murmur", "folder": "ACT_IV/mass", "query": "church congregation background murmur royalty free"}
]

# Ensure folders exist
for item in asset_manifest:
    os.makedirs(f"SFX/{item['folder']}", exist_ok=True)

# Write full register
with open("sfx_asset_register_COMPLETE.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Asset ID", "Category", "Description", "Status", "Filename", "Notes"])
    for item in asset_manifest:
        status = item.get("status", "NOT SOURCED")
        cat = item['folder'].split('/')[0]
        writer.writerow([item["id"], cat, item["name"], status, "", ""])

# 2. Build the bash script to fetch them all
with open("fetch_all_sfx.sh", "w") as f:
    f.write("#!/bin/bash\n")
    for item in asset_manifest:
        if "query" in item:
            folder = f"SFX/{item['folder']}"
            f.write(f'echo "Fetching {item["name"]}..."\n')
            f.write(f'yt-dlp --no-check-certificate -f "bestaudio/best" "ytsearch1:{item["query"]}" -o "{folder}/{item["id"]}_REC_v01_RAW.%(ext)s"\n')
    
    # Add the conversion block
    f.write('''
echo "Converting all to 48kHz 24-bit WAV..."
for file in SFX/*/*/*.webm SFX/*/*/*.m4a SFX/*/*/*.mp3 SFX/*/*/*.opus; do
  if [ -f "$file" ]; then
    out="${file%.*}.wav"
    ffmpeg -y -i "$file" -ar 48000 -acodec pcm_s24le -loglevel error "$out"
    rm "$file"
  fi
done
echo "Complete!"
''')

os.chmod("fetch_all_sfx.sh", 0o755)
print("Pipeline built. Ready to execute fetch_all_sfx.sh.")
