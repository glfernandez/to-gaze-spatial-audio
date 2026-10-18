import asyncio
import os
import subprocess
import edge_tts

async def synthesize(text, voice, out_path, rate="+0%", pitch="+0Hz"):
    tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await tts.save(out_path)

def run_cmd(cmd):
    subprocess.run(cmd, shell=True, check=True)

async def main():
    os.makedirs("scratch/neural_stems", exist_ok=True)
    os.makedirs("SFX/P1_PROLOGUE", exist_ok=True)

    print("--- 1. Generating SFX-04A: Breaking Headline News ---")
    # Voices: Christopher (Authority Anchor) + Aria (News Co-Anchor)
    await synthesize(
        "We interrupt our scheduled programming with breaking news from our international desk. Markets have halted trading as emergency meetings convene across global capitals.",
        "en-US-ChristopherNeural",
        "scratch/neural_stems/4a_voice1.mp3",
        rate="+5%"
    )
    await synthesize(
        "Officials are advising citizens to remain indoors as unconfirmed reports indicate severe disruptions worldwide.",
        "en-US-AriaNeural",
        "scratch/neural_stems/4a_voice2.mp3",
        rate="+8%"
    )

    # Option 1: Direct Studio Broadcast (Anchor 1 + Anchor 2 overlapping slightly)
    run_cmd(
        'ffmpeg -y -i scratch/neural_stems/4a_voice1.mp3 -i scratch/neural_stems/4a_voice2.mp3 '
        '-filter_complex "[0:a]volume=1.0[v1];[1:a]adelay=4200|4200,volume=0.9[v2];[v1][v2]amix=inputs=2:dropout_transition=0,highpass=f=70,loudnorm=I=-18.0:TP=-1.0:LRA=7" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-04A_REC_v01_RAW.wav'
    )
    # Option 2: Live Newsroom Floor (Subtle room reverberation + studio warmth)
    run_cmd(
        'ffmpeg -y -i SFX/P1_PROLOGUE/SFX-04A_REC_v01_RAW.wav '
        '-filter_complex "aecho=0.8:0.7:25|45:0.25|0.15,highpass=f=80,loudnorm=I=-18.0:TP=-1.0:LRA=7" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-04A_REC_v02_RAW.wav'
    )
    # Option 3: AM Radio Broadcast EQ (Bandpass 300Hz-3400Hz telephone/broadcast speaker)
    run_cmd(
        'ffmpeg -y -i SFX/P1_PROLOGUE/SFX-04A_REC_v01_RAW.wav '
        '-filter_complex "highpass=f=350,lowpass=f=3600,volume=1.5,loudnorm=I=-18.0:TP=-1.0:LRA=6" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-04A_REC_v03_RAW.wav'
    )

    print("--- 2. Generating SFX-04B: News of War & Conflict Sirens ---")
    # Voices: Guy (Urgent Field Correspondent) + Ryan (BBC British Correspondent)
    await synthesize(
        "Air raid sirens have sounded across the border for the fourth consecutive night as heavy artillery strikes continue along the defensive perimeter.",
        "en-US-GuyNeural",
        "scratch/neural_stems/4b_voice1.mp3",
        rate="+6%"
    )
    await synthesize(
        "Civil defense authorities are directing non-essential personnel into underground bunkers amidst escalating regional conflict.",
        "en-GB-RyanNeural",
        "scratch/neural_stems/4b_voice2.mp3",
        rate="+4%"
    )

    # Option 1: Live Field Dispatch with Sirens (Wailing siren tone under voices)
    run_cmd(
        'ffmpeg -y -i scratch/neural_stems/4b_voice1.mp3 -i scratch/neural_stems/4b_voice2.mp3 '
        '-f lavfi -i "sine=frequency=750:duration=10" '
        '-filter_complex "[2:a]tremolo=f=0.5:d=0.7,volume=0.25,highpass=f=300[siren];[0:a]volume=1.0[v1];[1:a]adelay=4500|4500,volume=0.9[v2];[v1][v2][siren]amix=inputs=3:dropout_transition=0,highpass=f=60,loudnorm=I=-18.0:TP=-1.0:LRA=7" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-04B_REC_v01_RAW.wav'
    )
    # Option 2: Deep Bunker / War Room Acoustic (Low rumble + acoustic enclosure)
    run_cmd(
        'ffmpeg -y -i SFX/P1_PROLOGUE/SFX-04B_REC_v01_RAW.wav '
        '-filter_complex "aecho=0.8:0.7:35|70:0.3|0.2,lowpass=f=4500,loudnorm=I=-18.0:TP=-1.0:LRA=7" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-04B_REC_v02_RAW.wav'
    )
    # Option 3: Shortwave Military Radio Transmission
    run_cmd(
        'ffmpeg -y -i SFX/P1_PROLOGUE/SFX-04B_REC_v01_RAW.wav '
        '-filter_complex "highpass=f=400,lowpass=f=3200,volume=1.6,loudnorm=I=-18.0:TP=-1.0:LRA=6" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-04B_REC_v03_RAW.wav'
    )

    print("--- 3. Generating SFX-04C: Floods & Climate Disaster News ---")
    # Voices: Christopher (Emergency EAS) + Sonia (UK International Reporter)
    await synthesize(
        "A catastrophic flash flood emergency has been declared. Torrential rainfall has overwhelmed riverbanks and municipal drainage systems.",
        "en-US-ChristopherNeural",
        "scratch/neural_stems/4c_voice1.mp3",
        rate="+5%"
    )
    await synthesize(
        "Severe weather warnings remain active across three coastal regions as emergency rescue boats navigate flooded highways.",
        "en-GB-SoniaNeural",
        "scratch/neural_stems/4c_voice2.mp3",
        rate="+5%"
    )

    # Option 1: EAS Emergency Broadcast with Two-Tone Header
    run_cmd(
        'ffmpeg -y -i scratch/neural_stems/4c_voice1.mp3 -i scratch/neural_stems/4c_voice2.mp3 '
        '-f lavfi -i "sine=frequency=853:duration=0.8" -f lavfi -i "sine=frequency=960:duration=0.8" '
        '-filter_complex "[2:a][3:a]amix=inputs=2,volume=0.4[eastone];[0:a]adelay=900|900,volume=1.0[v1];[1:a]adelay=5200|5200,volume=0.9[v2];[eastone][v1][v2]amix=inputs=3:dropout_transition=0,highpass=f=60,loudnorm=I=-18.0:TP=-1.0:LRA=7" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-04C_REC_v01_RAW.wav'
    )
    # Option 2: Torrential Rain Storm Bed & Echo
    run_cmd(
        'ffmpeg -y -i SFX/P1_PROLOGUE/SFX-04C_REC_v01_RAW.wav '
        '-filter_complex "aecho=0.8:0.7:20|50:0.25|0.15,highpass=f=80,loudnorm=I=-18.0:TP=-1.0:LRA=7" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-04C_REC_v02_RAW.wav'
    )
    # Option 3: Emergency Transistor Radio Filter
    run_cmd(
        'ffmpeg -y -i SFX/P1_PROLOGUE/SFX-04C_REC_v01_RAW.wav '
        '-filter_complex "highpass=f=450,lowpass=f=3500,volume=1.5,loudnorm=I=-18.0:TP=-1.0:LRA=6" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-04C_REC_v03_RAW.wav'
    )

    print("--- 4. Generating SFX-06: Commercials & Shopping Advertisements ---")
    # Voices: Roger (Hyper-commercial energetic announcer) + Ava (Cheerful mobile app announcer)
    await synthesize(
        "Super savings madness! Fifty percent off storewide today only! Don't wait, tap to buy now before midnight!",
        "en-US-RogerNeural",
        "scratch/neural_stems/6_voice1.mp3",
        rate="+12%"
    )
    await synthesize(
        "Download now and get instant cashback on all grocery and luxury items! Exclusive rewards unlocked daily!",
        "en-US-AvaNeural",
        "scratch/neural_stems/6_voice2.mp3",
        rate="+10%"
    )

    # Option 1: Fast-paced TV Ad Collage with Scanner Beep
    run_cmd(
        'ffmpeg -y -i scratch/neural_stems/6_voice1.mp3 -i scratch/neural_stems/6_voice2.mp3 '
        '-f lavfi -i "sine=frequency=2400:duration=0.08" '
        '-filter_complex "[2:a]adelay=1500|1500,volume=0.3[beep1];[0:a]volume=1.0[v1];[1:a]adelay=3800|3800,volume=0.9[v2];[v1][v2][beep1]amix=inputs=3:dropout_transition=0,highpass=f=80,loudnorm=I=-18.0:TP=-1.0:LRA=7" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-06_REC_v01_RAW.wav'
    )
    # Option 2: Commercial Mall P.A. System (Reverberant acoustic reflection)
    run_cmd(
        'ffmpeg -y -i SFX/P1_PROLOGUE/SFX-06_REC_v01_RAW.wav '
        '-filter_complex "aecho=0.8:0.7:40|80:0.3|0.2,loudnorm=I=-18.0:TP=-1.0:LRA=7" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-06_REC_v02_RAW.wav'
    )
    # Option 3: Hyper-Compressed Radio Promo Punch
    run_cmd(
        'ffmpeg -y -i SFX/P1_PROLOGUE/SFX-06_REC_v01_RAW.wav '
        '-filter_complex "highpass=f=120,lowpass=f=7500,acompressor=threshold=-15dB:ratio=6:attack=5:release=50,loudnorm=I=-18.0:TP=-1.0:LRA=6" '
        '-ar 48000 -c:a pcm_s16le SFX/P1_PROLOGUE/SFX-06_REC_v03_RAW.wav'
    )

    print("All neural newscaster cues successfully generated, layered, and normalized!")

if __name__ == "__main__":
    asyncio.run(main())
