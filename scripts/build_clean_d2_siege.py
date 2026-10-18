import wave
import numpy as np
import subprocess
import os

sr = 48000
duration = 25.0
n_samples = int(duration * sr)

def load_audio(path, start_sec=0, dur_sec=None):
    with wave.open(path, 'rb') as w:
        n_channels = w.getnchannels()
        src_sr = w.getframerate()
        start_frame = int(start_sec * src_sr)
        w.setpos(min(start_frame, w.getnframes() - 1))
        frames_to_read = int(dur_sec * src_sr) if dur_sec else (w.getnframes() - start_frame)
        data = w.readframes(frames_to_read)
        audio = np.frombuffer(data, dtype=np.int16).reshape(-1, n_channels).astype(np.float32) / 32768.0
        if n_channels == 1:
            audio = np.repeat(audio, 2, axis=1)
        return audio

def fit_to_len(audio, target_len):
    if len(audio) < target_len:
        reps = int(np.ceil(target_len / len(audio)))
        audio = np.tile(audio, (reps, 1))
    return audio[:target_len]

# Load organic assets and enforce exactly n_samples
crowd = fit_to_len(load_audio("SFX/A3_ESCAPE/SFX-10_REC_v01_RAW.wav", start_sec=2, dur_sec=25), n_samples)
shouts = fit_to_len(load_audio("SFX/D2_SIEGE/SFX-27_REC_v01_RAW.wav", start_sec=0, dur_sec=20), n_samples)
breath = fit_to_len(load_audio("SFX/A3_ESCAPE/SFX-12_REC_v01_RAW.wav", start_sec=0, dur_sec=4), n_samples)

metal_coins = fit_to_len(load_audio("SFX/A1_MARKET/SFX-09_REC_v01_RAW.wav", start_sec=5, dur_sec=25), n_samples)
shears = fit_to_len(load_audio("SFX/A4_TONSURE/SFX-13_REC_v01_RAW.wav", start_sec=10, dur_sec=25), n_samples)

door_impact = load_audio("SFX/A3_ESCAPE/SFX-14_DOOR_BANG_REC_v01_RAW.wav", start_sec=0, dur_sec=5)
footsteps = fit_to_len(load_audio("SFX/A3_ESCAPE/SFX-11_REC_v01_RAW.wav", start_sec=2, dur_sec=25), n_samples)

print(f"All source stems loaded cleanly ({n_samples} samples = {duration}s). Zero gunfire or explosive sources used.")

def export_take(audio_data, out_path, filter_desc):
    tmp_path = f"scratch/tmp_{os.path.basename(out_path)}"
    clipped = np.clip(audio_data * 32767.0, -32768, 32767).astype(np.int16)
    with wave.open(tmp_path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(clipped.tobytes())

    cmd = [
        "/opt/homebrew/opt/ffmpeg@4/bin/ffmpeg",
        "-y",
        "-i", tmp_path,
        "-af", f"{filter_desc},loudnorm=I=-18.0:LRA=11:tp=-1.0",
        "-ar", "48000",
        "-c:a", "pcm_s16le",
        out_path
    ]
    subprocess.run(cmd, check=True, capture_output=True)

    cmd_probe = ["/opt/homebrew/opt/ffmpeg@4/bin/ffmpeg", "-i", out_path, "-af", "volumedetect", "-f", "null", "-"]
    res = subprocess.run(cmd_probe, capture_output=True, text=True)
    vlines = [l.strip() for l in res.stderr.splitlines() if "volume:" in l]
    print(f"✓ {out_path}: {', '.join(vlines)}")

# =========================================================================
# 1. LAYER 1: HUMAN CHAOS (Vocals, Shouts & Valley Wall of Sound)
# =========================================================================
print("\n--- Generating Clean SFX-D2_VOCALS ---")
voc_base = crowd * 0.45 + shouts * 0.55 + breath * 0.25

# Take 1: Convent Interior (Stone wall muffled: 650Hz LPF, warm low-end)
export_take(voc_base, "SFX/D2_SIEGE/SFX-D2_VOCALS_v01_RAW.wav", "lowpass=f=650,bass=g=5:f=110,aecho=0.8:0.7:120|240:0.3|0.2")

# Take 2: Window Proximity (Sharp, dry yells right outside window, breath close)
voc_prox = crowd * 0.3 + shouts * 0.75 + breath * 0.4
export_take(voc_prox, "SFX/D2_SIEGE/SFX-D2_VOCALS_v02_RAW.wav", "highpass=f=160,equalizer=f=2800:t=q:w=1:g=2.5,aecho=0.8:0.6:40|85:0.2|0.1")

# Take 3: Valley Panorama (Wide stereo: horses/crowd spread, shouting reverberating across valley)
voc_pano = np.zeros_like(voc_base)
voc_pano[:, 0] = crowd[:, 0] * 0.6 + shouts[:, 0] * 0.3
voc_pano[:, 1] = crowd[:, 1] * 0.3 + shouts[:, 1] * 0.6
export_take(voc_pano, "SFX/D2_SIEGE/SFX-D2_VOCALS_v03_RAW.wav", "aecho=0.85:0.75:180|360:0.35|0.22")

# =========================================================================
# 2. LAYER 2: WEAPONRY & ARMOR (Chainmail, Blade Draws, Medieval Crossbow)
# =========================================================================
print("\n--- Generating Clean SFX-D2_WEAPONRY ---")

crossbow_stem = np.zeros((n_samples, 2), dtype=np.float32)
bow_click = door_impact[:int(0.25 * sr)] * 0.7
t5 = int(5.0 * sr)
crossbow_stem[t5:t5+len(bow_click)] += bow_click
t16 = int(16.0 * sr)
crossbow_stem[t16:t16+len(bow_click)] += bow_click

# Take 1: Convent Interior (Muffled dull iron clangs & chainmail body shifts)
wep_interior = metal_coins * 0.6 + shears * 0.35 + crossbow_stem * 0.4
export_take(wep_interior, "SFX/D2_SIEGE/SFX-D2_WEAPONRY_v01_RAW.wav", "lowpass=f=800,bass=g=4:f=130")

# Take 2: Window Proximity (Tactile chainmail jingling, sword draws)
wep_prox = metal_coins * 0.7 + shears * 0.6 + crossbow_stem * 0.5
export_take(wep_prox, "SFX/D2_SIEGE/SFX-D2_WEAPONRY_v02_RAW.wav", "highpass=f=200,equalizer=f=3500:t=q:w=1:g=2.5")

# Take 3: Crossbow Volley & Iron Flank Sweep (Panned chainmail left, blade draw right, occasional shot)
wep_panned = np.zeros_like(wep_interior)
wep_panned[:, 0] = metal_coins[:, 0] * 0.7 + shears[:, 0] * 0.2 + crossbow_stem[:, 0] * 0.2
wep_panned[:, 1] = metal_coins[:, 1] * 0.2 + shears[:, 1] * 0.7 + crossbow_stem[:, 1] * 0.6
export_take(wep_panned, "SFX/D2_SIEGE/SFX-D2_WEAPONRY_v03_RAW.wav", "aecho=0.8:0.7:60|130:0.25|0.15")

# =========================================================================
# 3. LAYER 3: SIEGE & CLIMBING (Ladders, Stone Grabs, Door Battering)
# =========================================================================
print("\n--- Generating Clean SFX-D2_BREACH ---")

ram_pattern = np.zeros((n_samples, 2), dtype=np.float32)
impact_len = min(len(door_impact), int(2.5 * sr))
for hit_sec in [0.5, 3.8, 7.2, 10.6, 14.1, 17.5, 21.0]:
    idx = int(hit_sec * sr)
    if idx + impact_len <= n_samples:
        ram_pattern[idx:idx+impact_len] += door_impact[:impact_len] * 1.1

climb_stem = footsteps * 0.7

# Take 1: Convent Interior (Door Battering focus - massive wooden door blows, splintering wood)
breach_int = ram_pattern * 0.85 + climb_stem * 0.3
export_take(breach_int, "SFX/D2_SIEGE/SFX-D2_BREACH_v01_RAW.wav", "lowpass=f=720,bass=g=6:f=95,aecho=0.8:0.65:50|120:0.3|0.2")

# Take 2: Window Proximity (Ladder slam on stone sill, boots scrambling rungs, gauntlet scratches)
breach_prox = ram_pattern * 0.4 + climb_stem * 0.8
export_take(breach_prox, "SFX/D2_SIEGE/SFX-D2_BREACH_v02_RAW.wav", "highpass=f=140,equalizer=f=2600:t=q:w=1:g=2.2")

# Take 3: Full Perimeter Assault (Door Center, Ladders Right, Climbing Left)
breach_full = np.zeros_like(breach_int)
breach_full[:, 0] = ram_pattern[:, 0] * 0.5 + climb_stem[:, 0] * 0.7
breach_full[:, 1] = ram_pattern[:, 1] * 0.5 + climb_stem[:, 1] * 0.3
export_take(breach_full, "SFX/D2_SIEGE/SFX-D2_BREACH_v03_RAW.wav", "aecho=0.8:0.7:70|150:0.25|0.18")

print("\nAll 9 D2 siege takes successfully re-rendered with pure 1240 AD medieval acoustic Foley!")
