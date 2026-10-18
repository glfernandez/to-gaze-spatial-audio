#!/bin/bash
echo "Fetching Palm Sunday Crowd..."
yt-dlp --no-check-certificate -f "bestaudio/best" "ytsearch1:ancient crowd cheering procession palm sunday royalty free" -o "SFX/A3_ESCAPE/SFX-10_REC_v01_RAW.%(ext)s"
echo "Fetching Lightning Strike..."
yt-dlp --no-check-certificate -f "bestaudio/best" "ytsearch1:loud thunder lightning strike sound effect royalty free" -o "SFX/B1_SAN_DAMIANO/SFX-18_REC_v01_RAW.%(ext)s"
echo "Fetching Cicada Transformation Stem..."
yt-dlp --no-check-certificate -f "bestaudio/best" "ytsearch1:cicadas weird eerie ambient processed sound effect royalty free" -o "SFX/B1_SAN_DAMIANO/SFX-20_REC_v01_RAW.%(ext)s"
echo "Fetching Pen/Paper Scratching..."
yt-dlp --no-check-certificate -f "bestaudio/best" "ytsearch1:quill pen writing on parchment paper sound effect royalty free" -o "SFX/D1_LETTER/SFX-23_REC_v01_RAW.%(ext)s"
echo "Fetching Soldiers Retreating..."
yt-dlp --no-check-certificate -f "bestaudio/best" "ytsearch1:army soldiers retreating running away royalty free" -o "SFX/D2_SIEGE/SFX-27_REC_v01_RAW.%(ext)s"
echo "Fetching Bowl/Falling Body Foley..."
yt-dlp --no-check-certificate -f "bestaudio/best" "ytsearch1:heavy body falling on stone floor sound effect royalty free" -o "SFX/D6_CHRISTMAS_MASS/SFX-28_REC_v01_RAW.%(ext)s"
echo "Fetching Great Organ Layer..."
yt-dlp --no-check-certificate -f "bestaudio/best" "ytsearch1:massive church pipe organ chord royalty free" -o "SFX/D6_CHRISTMAS_MASS/SFX-31_REC_v01_RAW.%(ext)s"

echo "Converting all to 48kHz 24-bit WAV..."
for file in SFX/*/*.* ; do
  if [[ "$file" == *.webm || "$file" == *.m4a || "$file" == *.mp3 || "$file" == *.opus ]]; then
    out="${file%.*}.wav"
    ffmpeg -y -i "$file" -ar 48000 -acodec pcm_s24le -loglevel error "$out"
    rm "$file"
  fi
done
echo "Complete!"
