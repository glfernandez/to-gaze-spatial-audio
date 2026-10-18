import os

items = {
    "SFX-01": {"folder": "SFX/P1_PROLOGUE", "q2": "vintage radio switch click sound effect", "q3": "old television clunky power button sound effect"},
    "SFX-02": {"folder": "SFX/P1_PROLOGUE", "q2": "rapid mouse clicking typing sound effect", "q3": "modern UI interface blips and clicks"},
    "SFX-03": {"folder": "SFX/P1_PROLOGUE", "q2": "busy city street traffic noise sound effect", "q3": "distant highway traffic drone sound effect"},
    "SFX-05": {"folder": "SFX/P1_PROLOGUE", "q2": "distant police siren wailing sound effect", "q3": "european ambulance siren passing sound effect"},
    "SFX-07": {"folder": "SFX/P1_PROLOGUE", "q2": "deep low frequency bass rumble drone", "q3": "ominous cinematic low synth hum sound effect"},
    "SFX-33A": {"folder": "SFX/00_GLOBAL", "q2": "slow steady human heartbeat sound effect", "q3": "fast racing heartbeat pulse sound effect"},
    "SFX-08": {"folder": "SFX/A1_MARKET", "q2": "medieval village atmosphere sound effect", "q3": "quiet historical town ambience sound effect"},
    "SFX-09": {"folder": "SFX/A1_MARKET", "q2": "horse hooves cobblestone cart sound effect", "q3": "busy medieval market merchants shouting"},
    "SFX-10": {"folder": "SFX/A3_ESCAPE", "q2": "large joyful crowd cheering procession", "q3": "ancient religious festival crowd ambience"},
    "SFX-11": {"folder": "SFX/A3_ESCAPE", "q2": "running footsteps on dirt path sound effect", "q3": "stealthy slow footsteps on stone sound effect"},
    "SFX-12": {"folder": "SFX/A3_ESCAPE", "q2": "woman heavy breathing running sound effect", "q3": "panicked exhausted breathing sound effect"},
    "SFX-14": {"folder": "SFX/A3_ESCAPE", "q2": "aggressive pounding on heavy wooden door", "q3": "dungeon door banging knocking sound effect"},
    "SFX-13": {"folder": "SFX/A4_TONSURE", "q2": "heavy metal scissors snipping sound effect", "q3": "rusty iron shears cutting thick fabric sound effect"},
    "SFX-15": {"folder": "SFX/B1_SAN_DAMIANO", "q2": "night crickets and cicadas field ambience", "q3": "dense summer cicadas forest sound effect"},
    "SFX-35": {"folder": "SFX/B1_SAN_DAMIANO", "q2": "huge thunderclap lightning strike sound effect", "q3": "rolling thunder heavy rain storm sound effect"},
    "SFX-36": {"folder": "SFX/B1_SAN_DAMIANO", "q2": "eerie vibrating alien drone sound effect", "q3": "supernatural ringing buzzing tone sound effect"},
    "SFX-16": {"folder": "SFX/C2_SISTERHOOD", "q2": "wet cloth wringing washing sound effect", "q3": "scrubbing fabric in water basin sound effect"},
    "SFX-17": {"folder": "SFX/C2_SISTERHOOD", "q2": "pouring water from pitcher to clay bowl", "q3": "water splashing softly in bucket sound effect"},
    "SFX-23": {"folder": "SFX/D1_LETTER", "q2": "feather quill writing fast on paper", "q3": "heavy pen scratching on rough parchment"},
    "SFX-19": {"folder": "SFX/D2_SIEGE", "q2": "distant chaotic medieval battle ambience", "q3": "muffled war explosions shouting drone"},
    "SFX-24": {"folder": "SFX/D2_SIEGE", "q2": "large army marching in armor sound effect", "q3": "rhythmic military boots marching on dirt"},
    "SFX-27": {"folder": "SFX/D2_SIEGE", "q2": "panicked crowd running away sound effect", "q3": "soldiers yelling falling back retreat sound effect"},
    "SFX-28": {"folder": "SFX/D6_CHRISTMAS_MASS", "q2": "heavy thud body hitting ground sound effect", "q3": "person collapsing on stone floor foley"},
    "SFX-29": {"folder": "SFX/D6_CHRISTMAS_MASS", "q2": "tolling large church bell ringing slowly", "q3": "multiple distant church bells ringing mass"},
    "SFX-30": {"folder": "SFX/D6_CHRISTMAS_MASS", "q2": "monks chanting gregorian choir background", "q3": "catholic mass murmuring prayers ambience"},
    "SFX-31": {"folder": "SFX/D6_CHRISTMAS_MASS", "q2": "triumphant church pipe organ music", "q3": "dark ominous pipe organ chord held long"}
}

script = "#!/bin/bash\n"
for sfx_id, data in items.items():
    folder = data['folder']
    
    # Option 2
    script += f'echo "Fetching {sfx_id} v02..."\n'
    script += f'yt-dlp --no-check-certificate -f "bestaudio/best" "ytsearch1:{data["q2"]} short" -o "{folder}/{sfx_id}_REC_v02_RAW.%(ext)s"\n'
    
    # Option 3
    script += f'echo "Fetching {sfx_id} v03..."\n'
    script += f'yt-dlp --no-check-certificate -f "bestaudio/best" "ytsearch1:{data["q3"]} short" -o "{folder}/{sfx_id}_REC_v03_RAW.%(ext)s"\n'

script += '''
echo "Converting all to 48kHz 24-bit WAV..."
for file in SFX/*/*.* ; do
  if [[ "$file" == *.webm || "$file" == *.m4a || "$file" == *.mp3 ]]; then
    out="${file%.*}.wav"
    ffmpeg -y -i "$file" -t 120 -ar 48000 -acodec pcm_s24le -loglevel error "$out"
    rm "$file"
  fi
done
echo "Complete!"
'''

with open("fetch_options.sh", "w") as f:
    f.write(script)

os.chmod("fetch_options.sh", 0o755)
print("fetch_options.sh generated")
