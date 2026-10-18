import re

with open('Rehearsal_Soundboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS for Immersive Mode
spat_css = '''
  /* IMMERSIVE SPATIAL AUDIO STYLES (TO-GAZE-SPATIAL-AUDIO-V1) */
  .immersive-strip {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    background: #16181d;
    border: 1px solid #28303d;
    border-radius: 6px;
    padding: 7px 12px;
    margin-top: 8px;
    font-size: 0.8em;
    flex-wrap: wrap;
  }
  .spat-left-controls {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }
  .btn-immersive-toggle {
    background: #1b263b;
    color: #4cc9f0;
    border: 1px solid #3a506b;
    border-radius: 4px;
    padding: 5px 10px;
    font-size: 0.85em;
    font-weight: 700;
    letter-spacing: 0.3px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s ease;
  }
  .btn-immersive-toggle:hover {
    background: #24344d;
    color: #70e000;
    border-color: #4cc9f0;
  }
  .badge-prof {
    background: rgba(76, 201, 240, 0.15);
    color: #4cc9f0;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.78em;
    font-family: monospace;
    font-weight: 600;
  }
  .lbl-fallback {
    color: #e0a96d;
    font-size: 0.78em;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
  .spat-fader-grp {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-size: 0.76em;
    color: #8892b0;
  }
  .spat-fader {
    width: 65px;
    height: 3px;
    cursor: pointer;
    accent-color: #4cc9f0;
  }
  .spat-val {
    font-family: monospace;
    color: #ccd6f6;
    min-width: 32px;
  }
  .spat-right-actions {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .btn-spat-aux {
    background: #20242c;
    color: #ccd6f6;
    border: 1px solid #3a4250;
    border-radius: 4px;
    padding: 5px 9px;
    font-size: 0.78em;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.15s ease;
  }
  .btn-spat-aux:hover {
    background: #2b323e;
    color: #fff;
    border-color: #5b667a;
  }
  .btn-spat-panel-toggle {
    background: #20242c;
    border-color: #3a506b;
    color: #d4af37;
  }
  .btn-spat-panel-toggle:hover {
    background: #2a2512;
    border-color: #d4af37;
    color: #ffd700;
  }

  /* Expandable Spatial Radar & Siege Deck Panel */
  .immersive-panel {
    background: #11141a;
    border: 1px solid #28303d;
    border-radius: 8px;
    padding: 14px;
    margin-top: 10px;
    display: grid;
    grid-template-columns: 260px 1fr 280px;
    gap: 14px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.6);
  }
  @media (max-width: 1050px) {
    .immersive-panel { grid-template-columns: 1fr; }
  }
  .spat-col {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .spat-col-title {
    color: #d4af37;
    font-size: 0.85em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #232b36;
    padding-bottom: 5px;
    margin: 0;
  }
  .spat-select {
    background: #1b2028;
    color: #ccd6f6;
    border: 1px solid #3a4454;
    padding: 6px 8px;
    border-radius: 4px;
    font-size: 0.82em;
    width: 100%;
    cursor: pointer;
  }
  .spat-speaker-list {
    background: #0d0f13;
    border: 1px solid #1f2530;
    border-radius: 4px;
    padding: 8px;
    font-size: 0.72em;
    color: #8892b0;
    max-height: 140px;
    overflow-y: auto;
    font-family: monospace;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .spat-speaker-item {
    display: flex;
    justify-content: space-between;
    padding: 2px 4px;
    border-radius: 2px;
  }
  .spat-speaker-item.testing {
    background: #2ecc71;
    color: #111;
    font-weight: bold;
  }
  .radar-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: #0b0d10;
    border: 1px solid #202631;
    border-radius: 6px;
    padding: 8px;
  }
  .radar-canvas {
    width: 100%;
    max-width: 380px;
    height: 240px;
    background: #0f1115;
    border-radius: 4px;
  }
  .radar-legend {
    display: flex;
    gap: 12px;
    font-size: 0.7em;
    color: #8892b0;
    margin-top: 6px;
    flex-wrap: wrap;
    justify-content: center;
  }
  .radar-legend span {
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
  .dot-legend {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    display: inline-block;
  }
  .dot-front { background: #3498db; }
  .dot-surr { background: #2ecc71; }
  .dot-sub { background: #e67e22; }
  .dot-height { background: #9b59b6; }
  .dot-source { background: #e74c3c; }

  /* Siege 5-State Automation Sequencer Buttons */
  .siege-states-grid {
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .btn-siege-state {
    background: #181d24;
    color: #a0aec0;
    border: 1px solid #2d3748;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 0.74em;
    text-align: left;
    cursor: pointer;
    transition: all 0.15s ease;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .btn-siege-state:hover {
    background: #232b36;
    color: #fff;
    border-color: #4a5568;
  }
  .btn-siege-state.active {
    background: #2b1d1d;
    color: #ff6b6b;
    border-color: #e74c3c;
    box-shadow: 0 0 8px rgba(231, 76, 60, 0.4);
    font-weight: bold;
  }
  .safety-deck {
    display: flex;
    gap: 6px;
    margin-top: 6px;
  }
  .btn-safety-blackout {
    flex: 1;
    background: #3b1818;
    color: #ff8787;
    border: 1px solid #c0392b;
    border-radius: 4px;
    padding: 6px;
    font-size: 0.75em;
    font-weight: 700;
    cursor: pointer;
    text-align: center;
  }
  .btn-safety-blackout:hover {
    background: #501e1e;
    color: #fff;
  }

  /* Sound Card Spatial Location Tag */
  .spat-tag {
    font-size: 0.69em;
    color: #4cc9f0;
    background: rgba(76, 201, 240, 0.08);
    border: 1px solid rgba(76, 201, 240, 0.25);
    border-radius: 3px;
    padding: 2px 6px;
    margin-top: 4px;
    font-family: monospace;
    letter-spacing: 0.2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
'''

content = content.replace('/* Sticky Header Wrapper & 9 Script-Aligned Tabs */', spat_css + '\n  /* Sticky Header Wrapper & 9 Script-Aligned Tabs */')

# 2. Add Immersive HTML Ribbon & Panel into sticky-top-header
old_top_markup = '''  <div class="scene-tab-bar" id="scene-tab-bar"></div>
</header>'''

new_top_markup = '''  <div class="scene-tab-bar" id="scene-tab-bar"></div>

  <!-- IMMERSIVE SPATIAL AUDIO DECK (TO-GAZE-SPATIAL-AUDIO-V1) -->
  <div class="immersive-strip" id="immersive-strip">
    <div class="spat-left-controls">
      <button class="btn-immersive-toggle" id="btn-immersive-toggle" title="Church Spatial Audio Engine is Active">
        🎧 IMMERSIVE SPATIAL AUDIO <span class="badge-prof" id="badge-current-profile">PROFILE A (2.0 STEREO 3D)</span>
      </button>
      <label class="lbl-fallback" title="Force discrete stereo fallback without spatial matrix"><input type="checkbox" id="chk-stereo-fallback"> Stereo Fallback</label>
      <span class="spat-fader-grp">
        <span class="spat-fader-lbl">Surround:</span>
        <input type="range" class="spat-fader" id="fader-surround" min="0" max="1.5" step="0.05" value="1.0">
        <span class="spat-val" id="val-surround">100%</span>
      </span>
      <span class="spat-fader-grp">
        <span class="spat-fader-lbl">Sub/LFE:</span>
        <input type="range" class="spat-fader" id="fader-lfe" min="0" max="1.5" step="0.05" value="1.0">
        <span class="spat-val" id="val-lfe">100%</span>
      </span>
    </div>
    <div class="spat-right-actions">
      <button class="btn-spat-aux" id="btn-test-speakers">🔊 Test Speakers</button>
      <button class="btn-spat-aux btn-spat-panel-toggle" id="btn-toggle-spat-panel">📐 Spatial Radar &amp; Siege States ▼</button>
    </div>
  </div>

  <div class="immersive-panel" id="immersive-panel" style="display:none;">
    <!-- Column 1: Speaker Layout & Hardware Routing -->
    <div class="spat-col">
      <h3 class="spat-col-title">Speaker Layout &amp; Routing</h3>
      <select class="spat-select" id="select-speaker-profile">
        <option value="A">Profile A — Stereo / Binaural 3D (2 Ch)</option>
        <option value="B">Profile B — Quad Surround (4 Ch: Church 4-Corner)</option>
        <option value="C">Profile C — 5.1 Theatrical (6 Ch: L/C/R, LFE, Surrounds)</option>
        <option value="D">Profile D — 7.1 Immersive (8 Ch: Full Perimeter)</option>
        <option value="E">Profile E — Church Height (8+ Ch: Sanctuary Dome)</option>
      </select>
      <div class="spat-speaker-list" id="spat-speaker-list">
        <div class="spat-speaker-item"><span>Ch 1: Front Left (FL)</span><span>45° L</span></div>
        <div class="spat-speaker-item"><span>Ch 2: Front Right (FR)</span><span>45° R</span></div>
      </div>
      <button class="btn-spat-aux" id="btn-test-speakers-modal" style="width:100%;margin-top:auto;">🔊 Cycle Speaker Chimes</button>
    </div>

    <!-- Column 2: 2D Church Acoustic Radar Visualizer -->
    <div class="spat-col radar-wrap">
      <h3 class="spat-col-title" style="width:100%;text-align:center;">Church Sanctuary Acoustic Radar</h3>
      <canvas class="radar-canvas" id="church-radar-canvas" width="380" height="240"></canvas>
      <div class="radar-legend">
        <span><span class="dot-legend dot-front"></span> Front/Center</span>
        <span><span class="dot-legend dot-surr"></span> Surrounds</span>
        <span><span class="dot-legend dot-height"></span> Dome Heights</span>
        <span><span class="dot-legend dot-sub"></span> Sub/LFE</span>
        <span><span class="dot-legend dot-source"></span> Live SFX</span>
      </div>
    </div>

    <!-- Column 3: Act III Siege 5-State Sequencer & Safety -->
    <div class="spat-col">
      <h3 class="spat-col-title">Siege 5-State Spatial Sequencer</h3>
      <div class="siege-states-grid">
        <button class="btn-siege-state" id="btn-siege-s1" onclick="SpatialEngine.triggerSiegeState(1)">
          <span>1. Approaching Army</span><span style="font-family:monospace;font-size:0.85em;">75m Rear</span>
        </button>
        <button class="btn-siege-state" id="btn-siege-s2" onclick="SpatialEngine.triggerSiegeState(2)">
          <span>2. Convent Under Attack</span><span style="font-family:monospace;font-size:0.85em;">Walls/Gates</span>
        </button>
        <button class="btn-siege-state" id="btn-siege-s3" onclick="SpatialEngine.triggerSiegeState(3)">
          <span>3. Clare\'s Fear (Auditory Tunnel)</span><span style="font-family:monospace;font-size:0.85em;">Heart Sub</span>
        </button>
        <button class="btn-siege-state" id="btn-siege-s4" onclick="SpatialEngine.triggerSiegeState(4)">
          <span>4. Divine Intervention</span><span style="font-family:monospace;font-size:0.85em;">Child Ctr</span>
        </button>
        <button class="btn-siege-state" id="btn-siege-s5" onclick="SpatialEngine.triggerSiegeState(5)">
          <span>5. Soldiers Retreat</span><span style="font-family:monospace;font-size:0.85em;">95m Peace</span>
        </button>
      </div>

      <div style="margin-top:auto;">
        <h4 style="font-size:0.75em;color:#ff8787;margin:6px 0 3px 0;text-transform:uppercase;">Emergency Safety Deck</h4>
        <div class="safety-deck">
          <button class="btn-safety-blackout" id="btn-spat-blackout-fade">🛑 Fade to Silence (2s)</button>
          <button class="btn-safety-blackout" id="btn-spat-hard-stop" style="background:#4a1212;border-color:#e74c3c;">⚡ All Stop</button>
        </div>
      </div>
    </div>
  </div>
</header>'''

assert old_top_markup in content, "old_top_markup not found!"
content = content.replace(old_top_markup, new_top_markup)

# 3. Bump STORAGE_KEY to v18 and include fallback to v17
content = content.replace("var STORAGE_KEY = 'to_gaze_soundboard_sequencer_v17';", "var STORAGE_KEY = 'to_gaze_soundboard_sequencer_v18';")
content = content.replace("var raw = localStorage.getItem(STORAGE_KEY) || localStorage.getItem('to_gaze_soundboard_sequencer_v16')", "var raw = localStorage.getItem(STORAGE_KEY) || localStorage.getItem('to_gaze_soundboard_sequencer_v17') || localStorage.getItem('to_gaze_soundboard_sequencer_v16')")

# 4. Inject spatial_audio_engine code right before SCENES_DATA
with open('spatial_audio_engine.js', 'r', encoding='utf-8') as sf:
    engine_code = sf.read()

content = content.replace('(function(){\n  var SCENES_DATA = [', engine_code + '\n\n(function(){\n  var SCENES_DATA = [')

# 5. Add CUE_SPATIAL_REGISTRY
cue_reg_code = '''
  var CUE_SPATIAL_REGISTRY = {
    "SFX-01A": { az: 0, el: 0, dist: 1.5, occl: 1.0 },
    "SFX-01": { az: 0, el: 0, dist: 3.0, occl: 1.0 },
    "SFX-02": { az: 0, el: 0, dist: 4.0, occl: 1.0 },
    "SFX-02B": { az: 290, el: 10, dist: 3.0, occl: 1.0 },
    "SFX-02C": { az: 70, el: 10, dist: 3.0, occl: 1.0 },
    "SFX-03": { az: 180, el: 0, dist: 25.0, occl: 0.7, isSurround: true },
    "SFX-04A": { az: 0, el: 0, dist: 3.0, occl: 1.0 },
    "SFX-04B": { az: 270, el: 0, dist: 12.0, occl: 0.9 },
    "SFX-04C": { az: 90, el: 0, dist: 12.0, occl: 0.9 },
    "SFX-05": { az: 80, el: 0, dist: 25.0, occl: 0.8 },
    "SFX-06": { az: 0, el: 0, dist: 2.5, occl: 1.0 },
    "SFX-07": { az: 0, el: 0, dist: 1.0, occl: 1.0 },
    "SFX-06B": { az: 180, el: 0, dist: 35.0, occl: 0.5 },
    "SFX-08": { az: 0, el: 0, dist: 8.0, occl: 1.0 },
    "SFX-09": { az: 130, el: 0, dist: 15.0, occl: 0.9 },
    "SFX-33A": { az: 0, el: 0, dist: 1.0, occl: 1.0, isLFE: true },
    "SFX-10A": { az: 180, el: 25, dist: 20.0, occl: 0.85, isSurround: true },
    "SFX-35": { az: 0, el: 75, dist: 12.0, occl: 1.0, isHeight: true },
    "SFX-36": { az: 0, el: 15, dist: 2.5, occl: 1.0, isLFE: true },
    "SFX-15": { az: 0, el: 20, dist: 8.0, occl: 1.0, isSurround: true },
    "SFX-34": { az: 315, el: 0, dist: 3.0, occl: 1.0 },
    "SFX-16_WATER": { az: 290, el: 0, dist: 3.0, occl: 1.0 },
    "SFX-17_CANTICLE": { az: 0, el: 0, dist: 4.0, occl: 1.0 },
    "SFX-23": { az: 75, el: 0, dist: 2.0, occl: 1.0 },
    "SFX-37": { az: 290, el: 0, dist: 2.5, occl: 1.0 },
    "SFX-D2_WAR": { az: 180, el: 0, dist: 75.0, occl: 0.15 },
    "SFX-D2_DRUMS": { az: 165, el: 0, dist: 60.0, occl: 0.25, isLFE: true },
    "SFX-D2_VO": { az: 270, el: 0, dist: 5.0, occl: 1.0 },
    "SFX-D2_GATE": { az: 285, el: 0, dist: 4.0, occl: 1.0, isLFE: true },
    "SFX-33A_D2": { az: 0, el: 0, dist: 1.0, occl: 1.0, isLFE: true },
    "SFX-CHILD_GOD": { az: 0, el: 10, dist: 1.8, occl: 1.0, isLFE: true },
    "SFX-26": { az: 0, el: 30, dist: 5.0, occl: 1.0, isLFE: true },
    "SFX-38_CHRISTMAS_MASS": { az: 0, el: 20, dist: 35.0, occl: 0.6, isSurround: true },
    "SFX-23_PAPAL": { az: 70, el: 0, dist: 2.5, occl: 1.0 },
    "SFX-30_CAUSTIC": { az: 0, el: 0, dist: 3.0, occl: 1.0 }
  };
'''

content = content.replace('var ST = {};', 'var ST = {};\n' + cue_reg_code)

# 6. Add spat-tag right after pan-row line
old_pan_line = "'<div class=\"pan-row\"><span class=\"slbl\" style=\"color:#2ecc71;\">PAN</span><input type=\"range\" class=\"pan-slider\" id=\"pn-' + sid + '\" min=\"-1\" max=\"1\" step=\"0.05\" value=\"' + ST[sid].savedPan + '\"><span class=\"pan-val\" id=\"pv-' + sid + '\" title=\"Double-click to Center\">' + (ST[sid].savedPan === 0 ? 'CTR' : (ST[sid].savedPan < 0 ? 'L ' + Math.round(Math.abs(ST[sid].savedPan)*100) + '%' : 'R ' + Math.round(ST[sid].savedPan*100) + '%')) + '</span></div>' +"

new_pan_line = old_pan_line + "\n            '<div class=\"spat-tag\" id=\"spat-tag-' + sid + '\">📍 Center Front (0°) • 2.0m</div>' +"

assert old_pan_line in content, "old_pan_line not found!"
content = content.replace(old_pan_line, new_pan_line)

# 7. Wire SpatialEngine registration in box loop
old_attach_spot = '''          ST[sid] = {
            audio: audioObj,
            iv: null,'''

new_attach_spot = '''          var spatCoords = CUE_SPATIAL_REGISTRY[sid] || { az: 0, el: 0, dist: 2.0, occl: 1.0 };
          SpatialEngine.attachTrack(sid, audioObj, spatCoords);

          ST[sid] = {
            audio: audioObj,
            iv: null,'''

assert old_attach_spot in content, "old_attach_spot not found!"
content = content.replace(old_attach_spot, new_attach_spot)

# 8. Update setTrackPan to adjust SpatialEngine azimuth
old_set_pan = '''    if (pv) {
      var txt = "CTR";
      if (panVal < -0.05) txt = "L " + Math.round(Math.abs(panVal) * 100) + "%";
      else if (panVal > 0.05) txt = "R " + Math.round(panVal * 100) + "%";
      pv.textContent = txt;
    }
  }'''

new_set_pan = '''    if (pv) {
      var txt = "CTR";
      if (panVal < -0.05) txt = "L " + Math.round(Math.abs(panVal) * 100) + "%";
      else if (panVal > 0.05) txt = "R " + Math.round(panVal * 100) + "%";
      pv.textContent = txt;
    }
    // Update spatial engine azimuth in real time
    if (typeof SpatialEngine !== 'undefined') {
      var mappedAz = panVal * 90.0; // -1 -> -90 (Left 270), +1 -> +90 (Right 90)
      if (mappedAz < 0) mappedAz += 360.0;
      SpatialEngine.setTrackSpatial(id, { az: mappedAz });
    }
  }'''

assert old_set_pan in content, "old_set_pan not found!"
content = content.replace(old_set_pan, new_set_pan)

# 9. In playSound, link web audio
old_play_sound = '''  function playSound(id) {
    var s = ST[id];
    if (!s || !s.audio) return;
    cancelFades(id);'''

new_play_sound = '''  function playSound(id) {
    var s = ST[id];
    if (!s || !s.audio) return;
    cancelFades(id);
    if (typeof SpatialEngine !== 'undefined') {
      SpatialEngine.ensureContext();
      SpatialEngine.linkWebAudio(id);
      SpatialEngine.updateTrackPosition(id);
    }'''

assert old_play_sound in content, "old_play_sound not found!"
content = content.replace(old_play_sound, new_play_sound)

# 10. Wire Immersive Control Deck UI events at the end of renderSoundboard
spat_ui_wiring = '''
    // --- Wire Immersive Spatial Audio Deck Controls ---
    var btnSpatToggle = document.getElementById('btn-immersive-toggle');
    var btnTogglePanel = document.getElementById('btn-toggle-spat-panel');
    var spatPanel = document.getElementById('immersive-panel');

    function toggleSpatPanel() {
      if (!spatPanel) return;
      var isOpen = (spatPanel.style.display !== 'none');
      spatPanel.style.display = isOpen ? 'none' : 'grid';
      if (btnTogglePanel) {
        btnTogglePanel.innerHTML = isOpen ? '📐 Spatial Radar &amp; Siege States ▼' : '📐 Close Spatial Radar ▲';
      }
      if (!isOpen && typeof SpatialEngine !== 'undefined') {
        SpatialEngine.ensureContext();
        SpatialEngine.bindRadarCanvas(document.getElementById('church-radar-canvas'));
      }
    }

    if (btnTogglePanel) btnTogglePanel.addEventListener('click', toggleSpatPanel);
    if (btnSpatToggle) btnSpatToggle.addEventListener('click', toggleSpatPanel);

    var selProfile = document.getElementById('select-speaker-profile');
    var badgeProfile = document.getElementById('badge-current-profile');
    var spkList = document.getElementById('spat-speaker-list');

    function renderSpeakerList(profId) {
      if (!spkList || !SPEAKER_PROFILES[profId]) return;
      spkList.innerHTML = '';
      SPEAKER_PROFILES[profId].speakers.forEach(function(spk){
        var row = document.createElement('div');
        row.className = 'spat-speaker-item';
        row.id = 'spk-row-' + spk.id;
        row.innerHTML = '<span>Ch ' + (spk.ch + 1) + ': ' + spk.name + '</span><span>' + (spk.isLFE ? 'LFE SUB' : (spk.isHeight ? 'DOME HEIGHT' : (spk.az + '°'))) + '</span>';
        spkList.appendChild(row);
      });
      if (badgeProfile) {
        badgeProfile.textContent = SPEAKER_PROFILES[profId].name.split('—')[0].trim().toUpperCase() + ' (' + SPEAKER_PROFILES[profId].channels + ' CH)';
      }
    }

    if (selProfile) {
      selProfile.addEventListener('change', function(){
        SpatialEngine.setProfile(this.value);
        renderSpeakerList(this.value);
      });
      renderSpeakerList('A');
    }

    var chkFallback = document.getElementById('chk-stereo-fallback');
    if (chkFallback) {
      chkFallback.addEventListener('change', function(){
        SpatialEngine.setStereoFallback(this.checked);
      });
    }

    var faderSurr = document.getElementById('fader-surround');
    var valSurr = document.getElementById('val-surround');
    if (faderSurr) {
      faderSurr.addEventListener('input', function(){
        SpatialEngine.setSurroundLevel(this.value);
        if (valSurr) valSurr.textContent = Math.round(this.value * 100) + '%';
      });
    }

    var faderLFE = document.getElementById('fader-lfe');
    var valLFE = document.getElementById('val-lfe');
    if (faderLFE) {
      faderLFE.addEventListener('input', function(){
        SpatialEngine.setLFELevel(this.value);
        if (valLFE) valLFE.textContent = Math.round(this.value * 100) + '%';
      });
    }

    var btnTestSpk = document.getElementById('btn-test-speakers');
    var btnTestSpkModal = document.getElementById('btn-test-speakers-modal');
    if (btnTestSpk) btnTestSpk.addEventListener('click', function(){ SpatialEngine.runSpeakerTestSequence(); });
    if (btnTestSpkModal) btnTestSpkModal.addEventListener('click', function(){ SpatialEngine.runSpeakerTestSequence(); });

    var btnBlackout = document.getElementById('btn-spat-blackout-fade');
    if (btnBlackout) btnBlackout.addEventListener('click', fadeOutAll);

    var btnHardStop = document.getElementById('btn-spat-hard-stop');
    if (btnHardStop) btnHardStop.addEventListener('click', stopAll);

    // Initial update of all source position labels
    SpatialEngine.updateAllSourcePositions();
    SpatialEngine.bindRadarCanvas(document.getElementById('church-radar-canvas'));
'''

content = content.replace('switchTab(initialTab);\n  }', 'switchTab(initialTab);\n' + spat_ui_wiring + '\n  }')

with open('Rehearsal_Soundboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Rehearsal_Soundboard.html successfully upgraded with TO-GAZE-SPATIAL-AUDIO-V1!")
