#!/bin/bash

# Trim traffic
ffmpeg -y -i "SFX/P1_PROLOGUE/SFX-03_TRAFFIC_CITYBED_REC_v01_RAW.wav" -t 60 -acodec copy temp_traffic.wav && mv temp_traffic.wav "SFX/P1_PROLOGUE/SFX-03_TRAFFIC_CITYBED_REC_v01_RAW.wav"

# Trim Shears (was 1 hour)
ffmpeg -y -i "SFX/A4_TONSURE/SFX-13_REC_v01_RAW.wav" -t 60 -acodec copy temp_shears.wav && mv temp_shears.wav "SFX/A4_TONSURE/SFX-13_REC_v01_RAW.wav"

# Trim Cicadas (was 1 hour)
ffmpeg -y -i "SFX/B1_SAN_DAMIANO/SFX-15_REC_v01_RAW.wav" -t 120 -acodec copy temp_cicadas.wav && mv temp_cicadas.wav "SFX/B1_SAN_DAMIANO/SFX-15_REC_v01_RAW.wav"

# Re-download Timeless War Bleed safely
echo "Redownloading SFX-19 Timeless War Bleed..."
yt-dlp --no-check-certificate -f "bestaudio/best" "ytsearch1:distant battle sounds 5 minutes royalty free" -o "SFX/D2_SIEGE/SFX-19_REC_v01_RAW.%(ext)s"
for file in SFX/D2_SIEGE/SFX-19_*.webm SFX/D2_SIEGE/SFX-19_*.m4a; do
  if [ -f "$file" ]; then
    out="${file%.*}.wav"
    ffmpeg -y -i "$file" -ar 48000 -acodec pcm_s24le -loglevel error "$out"
    rm "$file"
  fi
done

echo "Trimming complete."
