import re

with open("Rehearsal_Soundboard.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS
old_css = """.volume-wrapper { display: flex; align-items: center; flex-grow: 1; gap: 5px; }
  input[type=range].vol-slider { flex-grow: 1; accent-color: #d4af37; cursor: pointer; }"""

new_css = """.sliders-column { display: flex; flex-direction: column; flex-grow: 1; gap: 5px; }
  .slider-wrapper { display: flex; align-items: center; gap: 5px; }
  input[type=range].vol-slider, input[type=range].speed-slider { flex-grow: 1; accent-color: #d4af37; cursor: pointer; height: 4px; }
  .speed-slider { accent-color: #3498db !important; }"""
html = html.replace(old_css, new_css)

# 2. Update HTML injection
old_html = """        <div class="controls-row">
          <button id="btn-${sound.id}" onclick="toggleAudio('${sound.id}')">PLAY</button>
          <div class="volume-wrapper">
            <span>🔈</span>
            <input type="range" class="vol-slider" min="0" max="1" step="0.01" value="1" oninput="state['${sound.id}'].audio.volume = this.value">
          </div>
        </div>"""

new_html = """        <div class="controls-row">
          <button id="btn-${sound.id}" onclick="toggleAudio('${sound.id}')">PLAY</button>
          <div class="sliders-column">
            <div class="slider-wrapper">
              <span style="font-size:0.9em;" title="Volume">🔈</span>
              <input type="range" class="vol-slider" min="0" max="1" step="0.01" value="1" oninput="state['${sound.id}'].audio.volume = this.value">
              <span style="width: 35px;"></span>
            </div>
            <div class="slider-wrapper">
              <span style="font-size:0.9em;" title="Playback Speed">⏱️</span>
              <input type="range" class="speed-slider" min="0.1" max="3" step="0.05" value="1" oninput="updateSpeed('${sound.id}', this.value)">
              <span id="speed-val-${sound.id}" style="font-size:0.75em; color:#aaa; width: 35px; text-align:right;">1.00x</span>
            </div>
          </div>
        </div>"""
html = html.replace(old_html, new_html)

# 3. Add JS function
js_injection = """function updateSpeed(id, val) {
  const s = state[id];
  s.audio.playbackRate = parseFloat(val);
  // Optional: Set preservesPitch to false to allow tape-stop/demonic slowing effects
  if (s.audio.preservesPitch !== undefined) s.audio.preservesPitch = false; 
  if (s.audio.mozPreservesPitch !== undefined) s.audio.mozPreservesPitch = false;
  if (s.audio.webkitPreservesPitch !== undefined) s.audio.webkitPreservesPitch = false;
  
  document.getElementById(`speed-val-${id}`).innerText = parseFloat(val).toFixed(2) + 'x';
}

function updateLoop"""

html = html.replace("function updateLoop", js_injection)

with open("Rehearsal_Soundboard.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Speed sliders added!")
