import json
import os

files = [
    "SFX/P1_PROLOGUE/SFX-01_TV_TURN_ON_REC_v01_RAW.wav",
    "SFX/P1_PROLOGUE/SFX-02_MOUSE_CLICKS_INTERFACE_REC_v01_RAW.wav",
    "SFX/P1_PROLOGUE/SFX-03_TRAFFIC_CITYBED_REC_v01_RAW.wav",
    "SFX/P1_PROLOGUE/SFX-05_AMBULANCE_EMERGENCY_REC_v01_RAW.wav",
    "SFX/P1_PROLOGUE/SFX-07_REC_v01_RAW.wav",
    "SFX/00_GLOBAL/SFX-33A_HB_CANONICAL_REC_v01_RAW.wav",
    "SFX/A1_MARKET/SFX-08_REC_v01_RAW.wav",
    "SFX/A1_MARKET/SFX-09_REC_v01_RAW.wav",
    "SFX/A3_ESCAPE/SFX-10_REC_v01_RAW.wav",
    "SFX/A3_ESCAPE/SFX-11_REC_v01_RAW.wav",
    "SFX/A3_ESCAPE/SFX-12_REC_v01_RAW.wav",
    "SFX/A3_ESCAPE/SFX-14_DOOR_BANG_REC_v01_RAW.wav",
    "SFX/A4_TONSURE/SFX-13_REC_v01_RAW.wav",
    "SFX/B1_SAN_DAMIANO/SFX-15_REC_v01_RAW.wav",
    "SFX/B1_SAN_DAMIANO/SFX-35_LIGHTNING_REC_v01_RAW.wav",
    "SFX/B1_SAN_DAMIANO/SFX-36_CICADA_TRANSFORM_REC_v01_RAW.wav",
    "SFX/C2_SISTERHOOD/SFX-16_REC_v01_RAW.wav",
    "SFX/C2_SISTERHOOD/SFX-17_REC_v01_RAW.wav",
    "SFX/D1_LETTER/SFX-23_REC_v01_RAW.wav",
    "SFX/D2_SIEGE/SFX-19_REC_v01_RAW.wav",
    "SFX/D2_SIEGE/SFX-24_SOLDIERS_REC_v01_RAW.wav",
    "SFX/D2_SIEGE/SFX-27_REC_v01_RAW.wav",
    "SFX/D6_CHRISTMAS_MASS/SFX-28_REC_v01_RAW.wav",
    "SFX/D6_CHRISTMAS_MASS/SFX-29_BELLS_REC_v01_RAW.wav",
    "SFX/D6_CHRISTMAS_MASS/SFX-30_CONGREGATION_REC_v01_RAW.wav",
    "SFX/D6_CHRISTMAS_MASS/SFX-31_REC_v01_RAW.wav"
]

labels = {
    "SFX-01": "TV Turn On", "SFX-02": "Mouse Clicks", "SFX-03": "Traffic City Bed",
    "SFX-05": "Ambulance Siren", "SFX-07": "Low Resonance Drone", "SFX-33A": "Canonical Heartbeat",
    "SFX-08": "Medieval Atmosphere", "SFX-09": "Assisi Market", "SFX-10": "Palm Sunday Crowd",
    "SFX-11": "Footsteps on Stone", "SFX-12": "Clare Running Breath", "SFX-14": "Door BANG BANG BANG",
    "SFX-13": "Shears", "SFX-15": "Cicadas", "SFX-35": "Lightning Strike",
    "SFX-36": "Cicada Transformation", "SFX-16": "Cloth/Foot Washing", "SFX-17": "Water Pouring",
    "SFX-23": "Quill Pen Scratching", "SFX-19": "Timeless War Bleed", "SFX-24": "Soldiers Marching",
    "SFX-27": "Soldiers Retreating", "SFX-28": "Body Falling Foley", "SFX-29": "Distant Christmas Bells",
    "SFX-30": "Congregation Liturgy", "SFX-31": "Great Organ Chord"
}

scenes = {}
for file in files:
    parts = file.split("/")
    scene = parts[1].replace("_", " ")
    filename = parts[-1]
    sfx_id = filename.split("_")[0]
    label = f"[{sfx_id}] " + labels.get(sfx_id, filename)
    
    if scene not in scenes: scenes[scene] = []
    scenes[scene].append({"id": sfx_id, "label": label, "file": file})

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>To Gaze - Visual Trimmer Soundboard</title>
<style>
  body {{ background-color: #121212; color: #e0e0e0; font-family: 'Segoe UI', Tahoma, sans-serif; padding: 20px; margin: 0; }}
  h1 {{ color: #d4af37; border-bottom: 1px solid #333; padding-bottom: 10px; margin:0; }}
  h2 {{ color: #a9a9a9; margin-top: 30px; font-weight: 300; letter-spacing: 1px; }}
  .scene-container {{ margin-bottom: 30px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 20px; }}
  .sound-box {{ 
    background-color: #1e1e1e; border: 2px solid #333; border-radius: 8px; padding: 15px; 
    transition: all 0.2s ease; display: flex; flex-direction: column; gap: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
  }}
  .sound-box.active {{ border-color: #d4af37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.3); background-color: #2a2411; }}
  .sound-title {{ font-size: 1.05em; font-weight: 600; color: #fff; display: flex; justify-content: space-between; }}
  .controls-row {{ display: flex; align-items: center; justify-content: space-between; gap: 10px; }}
  
  button {{ 
    padding: 8px 15px; cursor: pointer; background: #333; color: white; 
    border: none; border-radius: 4px; font-weight: bold; transition: 0.2s;
    text-align: center; width: 80px;
  }}
  button:hover {{ background: #444; }}
  button.playing {{ background: #c0392b; }}
  button.playing:hover {{ background: #e74c3c; }}
  
  .volume-wrapper {{ display: flex; align-items: center; flex-grow: 1; gap: 5px; }}
  input[type=range].vol-slider {{ flex-grow: 1; accent-color: #d4af37; cursor: pointer; }}
  
  /* Visual Trimmer CSS */
  .trimmer-container {{ background: #111; padding: 15px 10px 10px 10px; border-radius: 6px; display: flex; flex-direction: column; gap: 5px; }}
  .trimmer-wrapper {{ position: relative; width: 100%; height: 24px; margin-bottom: 5px; }}
  .trimmer-track {{ position: absolute; width: 100%; height: 8px; background: #333; top: 8px; border-radius: 4px; }}
  .trimmer-fill {{ position: absolute; height: 8px; background: rgba(212, 175, 55, 0.5); border: 1px solid #d4af37; top: 7px; border-radius: 4px; z-index: 1; box-sizing: border-box; }}
  .playhead {{ position: absolute; width: 2px; height: 24px; background: #e74c3c; top: 0; z-index: 2; box-shadow: 0 0 4px #000; left: 0%; transition: left 0.05s linear; }}
  
  input[type=range].trim-slider {{
    position: absolute; width: 100%; height: 8px; top: 8px; margin: 0;
    -webkit-appearance: none; appearance: none; background: transparent;
    pointer-events: none; z-index: 3;
  }}
  input[type=range].trim-slider::-webkit-slider-thumb {{
    -webkit-appearance: none; appearance: none;
    width: 14px; height: 24px; background: #d4af37; border-radius: 3px;
    cursor: ew-resize; pointer-events: auto;
    border: 1px solid #000;
  }}
  input[type=range].trim-slider::-moz-range-thumb {{
    width: 14px; height: 24px; background: #d4af37; border-radius: 3px;
    cursor: ew-resize; pointer-events: auto; border: 1px solid #000;
  }}

  .time-labels {{ display: flex; justify-content: space-between; font-size: 0.75em; color: #888; }}
  
  .master-controls {{ position: sticky; top: 0; background: rgba(18,18,18,0.95); padding: 15px 0; z-index: 100; border-bottom: 1px solid #333; display: flex; justify-content: space-between; align-items: center; }}
  .stop-all {{ background: #c0392b; font-size: 1.1em; padding: 12px 24px; width: auto; }}
</style>
</head>
<body>

<div class="master-controls">
  <h1>To Gaze - Visual Soundboard</h1>
  <button class="stop-all" onclick="stopAll()">STOP ALL AUDIO</button>
</div>

<div id="app"></div>

<script>
const scenesData = {json.dumps(scenes)};
const state = {{}}; 

function init() {{
  const app = document.getElementById('app');
  
  for (const [sceneName, sounds] of Object.entries(scenesData)) {{
    const section = document.createElement('div');
    section.className = 'scene-container';
    section.innerHTML = `<h2>${{sceneName}}</h2>`;
    const grid = document.createElement('div');
    grid.className = 'grid';
    
    sounds.forEach(sound => {{
      const audio = new Audio(sound.file);
      state[sound.id] = {{ audio: audio, interval: null, isPlaying: false, loop: true }};
      
      const box = document.createElement('div');
      box.className = 'sound-box';
      box.id = 'box-' + sound.id;
      
      box.innerHTML = `
        <div class="sound-title">
          <span>${{sound.label}}</span>
          <label style="font-size: 0.8em; font-weight: normal; cursor: pointer;">
            <input type="checkbox" id="loop-${{sound.id}}" checked onchange="updateLoop('${{sound.id}}', this.checked)"> Loop
          </label>
        </div>
        
        <div class="controls-row">
          <button id="btn-${{sound.id}}" onclick="toggleAudio('${{sound.id}}')">PLAY</button>
          <div class="volume-wrapper">
            <span>🔈</span>
            <input type="range" class="vol-slider" min="0" max="1" step="0.01" value="1" oninput="state['${{sound.id}}'].audio.volume = this.value">
          </div>
        </div>
        
        <div class="trimmer-container">
          <div class="trimmer-wrapper">
            <div class="trimmer-track"></div>
            <div class="trimmer-fill" id="fill-${{sound.id}}"></div>
            <div class="playhead" id="head-${{sound.id}}"></div>
            <input type="range" class="trim-slider" id="start-${{sound.id}}" value="0" min="0" max="10" step="0.01" oninput="onTrimInput('${{sound.id}}', 'start')">
            <input type="range" class="trim-slider" id="end-${{sound.id}}" value="10" min="0" max="10" step="0.01" oninput="onTrimInput('${{sound.id}}', 'end')">
          </div>
          <div class="time-labels">
            <span id="label-start-${{sound.id}}">0.0s</span>
            <span id="label-current-${{sound.id}}" style="color: #fff; font-weight: bold;">0.0s</span>
            <span id="label-end-${{sound.id}}">...</span>
          </div>
        </div>
      `;
      
      grid.appendChild(box);
      
      // Once audio loads, set up the visual trimmer limits
      audio.addEventListener('loadedmetadata', () => {{
        const duration = audio.duration;
        const startSlider = document.getElementById(`start-${{sound.id}}`);
        const endSlider = document.getElementById(`end-${{sound.id}}`);
        
        startSlider.max = duration;
        endSlider.max = duration;
        endSlider.value = duration;
        
        document.getElementById(`label-end-${{sound.id}}`).innerText = duration.toFixed(1) + 's';
        updateVisuals(sound.id);
      }});
    }});
    
    section.appendChild(grid);
    app.appendChild(section);
  }}
}}

function onTrimInput(id, type) {{
  const startSlider = document.getElementById(`start-${{id}}`);
  const endSlider = document.getElementById(`end-${{id}}`);
  
  let startV = parseFloat(startSlider.value);
  let endV = parseFloat(endSlider.value);
  
  // Prevent passing each other
  if (startV >= endV) {{
    if (type === 'start') {{
      startSlider.value = endV - 0.1;
    }} else {{
      endSlider.value = startV + 0.1;
    }}
  }}
  
  updateVisuals(id);
  
  // If playing, maybe jump playhead? Not necessary, it'll catch naturally
}}

function updateVisuals(id) {{
  const startSlider = document.getElementById(`start-${{id}}`);
  const endSlider = document.getElementById(`end-${{id}}`);
  const fill = document.getElementById(`fill-${{id}}`);
  
  let startV = parseFloat(startSlider.value);
  let endV = parseFloat(endSlider.value);
  let maxV = parseFloat(startSlider.max);
  
  if (maxV === 0) return;
  
  let startPct = (startV / maxV) * 100;
  let endPct = (endV / maxV) * 100;
  
  fill.style.left = startPct + '%';
  fill.style.width = (endPct - startPct) + '%';
  
  document.getElementById(`label-start-${{id}}`).innerText = startV.toFixed(1) + 's';
  document.getElementById(`label-end-${{id}}`).innerText = endV.toFixed(1) + 's';
}}

function updateLoop(id, isLooping) {{
  state[id].loop = isLooping;
}}

function toggleAudio(id) {{
  const s = state[id];
  const btn = document.getElementById('btn-' + id);
  const box = document.getElementById('box-' + id);
  const startSlider = document.getElementById(`start-${{id}}`);
  const endSlider = document.getElementById(`end-${{id}}`);
  const playhead = document.getElementById(`head-${{id}}`);
  const labelCurrent = document.getElementById(`label-current-${{id}}`);
  
  if (s.isPlaying) {{
    // Stop
    s.audio.pause();
    clearInterval(s.interval);
    s.isPlaying = false;
    btn.innerText = 'PLAY';
    btn.classList.remove('playing');
    box.classList.remove('active');
  }} else {{
    // Play
    let startT = parseFloat(startSlider.value) || 0;
    let endT = parseFloat(endSlider.value) || s.audio.duration;
    
    s.audio.currentTime = startT;
    s.audio.play().catch(e => console.error(e));
    s.isPlaying = true;
    
    btn.innerText = 'STOP';
    btn.classList.add('playing');
    box.classList.add('active');
    
    s.interval = setInterval(() => {{
      const current = s.audio.currentTime;
      let currentEnd = parseFloat(endSlider.value);
      let currentStart = parseFloat(startSlider.value);
      let maxV = parseFloat(startSlider.max);
      
      // Update playhead visual
      if (maxV > 0) {{
        let pct = (current / maxV) * 100;
        playhead.style.left = pct + '%';
      }}
      labelCurrent.innerText = current.toFixed(1) + 's';
      
      // Loop or Stop logic
      if (current >= currentEnd) {{
        if (s.loop) {{
          s.audio.currentTime = currentStart;
        }} else {{
          toggleAudio(id);
        }}
      }}
    }}, 30);
  }}
}}

function stopAll() {{
  for (const [id, s] of Object.entries(state)) {{
    if (s.isPlaying) toggleAudio(id);
  }}
}}

window.onload = init;
</script>

</body>
</html>
"""

with open("Rehearsal_Soundboard.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Visual QuickTime-style trimmer dashboard created successfully!")
