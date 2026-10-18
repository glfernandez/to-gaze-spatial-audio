import subprocess
import os

out_dir = "SFX/D2_SIEGE"
os.makedirs(out_dir, exist_ok=True)

src_war = "scratch/medieval_war_sfx.wav"
src_drums = "scratch/medieval_war_drums.wav"

def render_take(src, out_name, af_filter):
    out_path = os.path.join(out_dir, out_name)
    filter_chain = f"{af_filter},loudnorm=I=-18.0:LRA=11:tp=-1.0" if af_filter else "loudnorm=I=-18.0:LRA=11:tp=-1.0"
    cmd = [
        "/opt/homebrew/opt/ffmpeg@4/bin/ffmpeg",
        "-y",
        "-i", src,
        "-af", filter_chain,
        "-ar", "48000",
        "-c:a", "pcm_s16le",
        out_path
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    
    # Probe
    cmd_probe = ["/opt/homebrew/opt/ffmpeg@4/bin/ffmpeg", "-i", out_path, "-af", "volumedetect", "-f", "null", "-"]
    res = subprocess.run(cmd_probe, capture_output=True, text=True)
    vlines = [l.strip() for l in res.stderr.splitlines() if "volume:" in l]
    print(f"✓ {out_path}: {', '.join(vlines)}")

print("=== Rendering Medieval War Soundscape (SoundofTime) ===")
# Opt 1: Canonical Master
render_take(src_war, "SFX-D2_WAR_v01_RAW.wav", "")
# Opt 2: Convent Interior Muffled (Stone wall transmission)
render_take(src_war, "SFX-D2_WAR_v02_RAW.wav", "lowpass=f=750,bass=g=4:f=110,aecho=0.8:0.7:100|200:0.25|0.15")
# Opt 3: Wide Valley Reverb
render_take(src_war, "SFX-D2_WAR_v03_RAW.wav", "aecho=0.85:0.75:180|360:0.35|0.2")

print("\n=== Rendering Medieval War Drums (Der Wikinger) ===")
# Opt 1: Full War Drums (Canonical Master)
render_take(src_drums, "SFX-D2_DRUMS_v01_RAW.wav", "")
# Opt 2: Heavy Sub-Bass Pulsing Drums
render_take(src_drums, "SFX-D2_DRUMS_v02_RAW.wav", "equalizer=f=90:t=q:w=1.2:g=5.0,acompressor=threshold=-16dB:ratio=4:attack=10:release=100")
# Opt 3: Distant Valley Siege Drums
render_take(src_drums, "SFX-D2_DRUMS_v03_RAW.wav", "lowpass=f=1200,aecho=0.85:0.75:220|440:0.35|0.22")

print("\nAll 6 D2 YouTube war takes successfully rendered!")
