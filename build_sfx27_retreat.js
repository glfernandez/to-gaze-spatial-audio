const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('=== Engineering True Theatrical Sound Design for SFX-27: Soldiers Retreating & Screaming ===');

const outDir = 'SFX/D2_SIEGE';
const sfx19 = 'SFX/D2_SIEGE/SFX-19_REC_v01_RAW.wav';
const sfx11 = 'SFX/A3_ESCAPE/SFX-11_REC_v01_RAW.wav';
const sfx24 = 'SFX/D2_SIEGE/SFX-24_SOLDIERS_REC_v01_RAW.wav';
const sfx12 = 'SFX/A3_ESCAPE/SFX-12_REC_v01_RAW.wav';

// Take 1 (Option 1): Standard Balanced Panicked Withdrawal
// Screaming men in panic retreat, rapid scrambled footsteps on stone, armor clattering, receding away
console.log('Rendering Take 1 (Option 1: Balanced Withdrawal)...');
execSync(`ffmpeg -y \
  -ss 251 -t 20 -i "${sfx19}" \
  -ss 1 -t 20 -i "${sfx11}" \
  -i "${sfx24}" \
  -i "${sfx12}" \
  -filter_complex "\
    [0:a]volume=1.6,highpass=f=120,lowpass=f=4200[shouts];\
    [1:a]volume=1.5,asetrate=48000*1.15,aresample=48000,highpass=f=90[running_boots];\
    [2:a]aloop=loop=-1:size=288000,volume=1.1,highpass=f=120[armor];\
    [3:a]aloop=loop=-1:size=203407,volume=0.8,highpass=f=150[gasps];\
    [shouts][running_boots][armor][gasps]amix=inputs=4:duration=first:dropout_transition=0,\
    lowpass=f=2600,afade=t=out:st=11:d=9,\
    aecho=0.8:0.7:90|210:0.32|0.2,\
    loudnorm=I=-18.0:TP=-1.0:LRA=9[out]\
  " -map "[out]" -ar 48000 -c:a pcm_s16le "${outDir}/SFX-27_REC_v01_RAW.wav"`);

// Take 2 (Option 2): Dynamic Pan Sweep (Stage Right to Far Stage Left Escape)
// Men flee from the breach point (Stage Right) across the stage and vanish down the left valley
console.log('Rendering Take 2 (Option 2: Dynamic Pan Sweep Right -> Left)...');
execSync(`ffmpeg -y \
  -ss 251 -t 20 -i "${sfx19}" \
  -ss 3 -t 20 -i "${sfx11}" \
  -i "${sfx24}" \
  -filter_complex "\
    [0:a]volume=1.5,highpass=f=120,lowpass=f=4000[shouts];\
    [1:a]volume=1.6,asetrate=48000*1.2,aresample=48000,highpass=f=90[running_boots];\
    [2:a]aloop=loop=-1:size=288000,volume=1.0,highpass=f=120[armor];\
    [shouts][running_boots][armor]amix=inputs=3:duration=first:dropout_transition=0,\
    pan=stereo|c0=0.25*c0+0.95*c1|c1=0.95*c0+0.15*c1,\
    lowpass=f=2400,afade=t=out:st=10:d=10,\
    aecho=0.8:0.7:110|240:0.3|0.2,\
    loudnorm=I=-18.0:TP=-1.0:LRA=9[out]\
  " -map "[out]" -ar 48000 -c:a pcm_s16le "${outDir}/SFX-27_REC_v02_RAW.wav"`);

// Take 3 (Option 3): Distant Wall Echo & Valley Dissipation (Biased Left)
// Echoing shouts bouncing off the San Damiano stone walls into the vast outdoor valley below
console.log('Rendering Take 3 (Option 3: Distant Wall Echo & Valley Dissipation)...');
execSync(`ffmpeg -y \
  -ss 253 -t 20 -i "${sfx19}" \
  -ss 5 -t 20 -i "${sfx11}" \
  -i "${sfx24}" \
  -filter_complex "\
    [0:a]volume=1.4,highpass=f=140,lowpass=f=3200[shouts];\
    [1:a]volume=1.3,highpass=f=100[running_boots];\
    [2:a]aloop=loop=-1:size=288000,volume=0.9,highpass=f=150[armor];\
    [shouts][running_boots][armor]amix=inputs=3:duration=first:dropout_transition=0,\
    pan=stereo|c0=0.85*c0+0.2*c1|c1=0.35*c0+0.35*c1,\
    lowpass=f=2000,afade=t=out:st=9:d=11,\
    aecho=0.85:0.8:160|320|480:0.4|0.3|0.2,\
    loudnorm=I=-18.0:TP=-1.0:LRA=9[out]\
  " -map "[out]" -ar 48000 -c:a pcm_s16le "${outDir}/SFX-27_REC_v03_RAW.wav"`);

console.log('=== All 3 SFX-27 Soldiers Retreat Takes Successfully Rendered! ===');
