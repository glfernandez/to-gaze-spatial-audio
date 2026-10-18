import re

with open('Rehearsal_Soundboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Top Master Bar HTML
old_mbar = '''<div class="mbar">
  <h1>To Gaze &mdash; Visual Soundboard &amp; Scene Sequencer <span style="font-size:0.6em;color:#aaa;font-weight:normal;">[Dramaturgy Edition]</span></h1>
  <div class="mbar-actions">
    <button class="stpall" id="stopbtn">STOP ALL AUDIO</button>
    <button class="btn-fade-all" id="fadeallbtn">FADE OUT ALL</button>
    <button class="btn-aux" id="btn-export-preset">💾 Save Preset</button>
    <button class="btn-aux" id="btn-import-preset">📂 Load Preset</button>
    <button class="btn-aux" id="btn-reset-defaults" style="color:#e74c3c;">🔄 Reset</button>
    <input type="file" id="preset-file-input" accept=".json">
  </div>
</div>

<div id="app"></div>'''

new_mbar = '''<header class="sticky-top-header">
  <div class="mbar">
    <h1>To Gaze &mdash; Visual Soundboard &amp; Scene Sequencer <span style="font-size:0.6em;color:#aaa;font-weight:normal;">[Dramaturgy Edition]</span></h1>
    <div class="mbar-actions">
      <button class="stpall" id="stopbtn">STOP ALL AUDIO</button>
      <button class="btn-fade-all" id="fadeallbtn">FADE OUT ALL</button>
      <button class="btn-aux" id="btn-export-preset">💾 Save Preset</button>
      <button class="btn-aux" id="btn-import-preset">📂 Load Preset</button>
      <button class="btn-aux" id="btn-reset-defaults" style="color:#e74c3c;">🔄 Reset</button>
      <input type="file" id="preset-file-input" accept=".json">
    </div>
  </div>
  <div class="scene-tab-bar" id="scene-tab-bar"></div>
</header>

<div id="app"></div>'''

assert old_mbar in content, "old_mbar not found!"
content = content.replace(old_mbar, new_mbar)

# 2. Add Tab CSS Styles
tab_css = '''
  /* Sticky Header Wrapper & 9 Script-Aligned Tabs */
  .sticky-top-header {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(18, 18, 18, 0.98);
    backdrop-filter: blur(8px);
    border-bottom: 2px solid #282828;
    margin: -20px -20px 25px -20px;
    padding: 16px 20px 10px 20px;
  }
  .scene-tab-bar {
    display: flex;
    gap: 6px;
    overflow-x: auto;
    padding: 10px 0 2px 0;
    scrollbar-width: thin;
    align-items: center;
  }
  .scene-tab-btn {
    background: #1e1e1e;
    color: #aaa;
    border: 1px solid #383838;
    border-radius: 5px;
    padding: 7px 12px;
    font-size: 0.78em;
    font-weight: 600;
    letter-spacing: 0.3px;
    cursor: pointer;
    white-space: nowrap;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.15s ease;
    user-select: none;
  }
  .scene-tab-btn:hover {
    background: #282828;
    color: #fff;
    border-color: #555;
  }
  .scene-tab-btn.active {
    background: #2a2512;
    color: #d4af37;
    border-color: #d4af37;
    box-shadow: 0 0 10px rgba(212, 175, 55, 0.3);
  }
  .scene-tab-btn .tab-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #444;
    display: inline-block;
    transition: all 0.2s ease;
    flex-shrink: 0;
  }
  .scene-tab-btn.active .tab-dot {
    background: #d4af37;
  }
  .scene-tab-btn.playing .tab-dot {
    background: #2ecc71 !important;
    box-shadow: 0 0 7px #2ecc71;
    animation: tabPulseGreen 0.7s infinite alternate;
  }
  @keyframes tabPulseGreen {
    from { transform: scale(0.9); opacity: 0.7; }
    to { transform: scale(1.3); opacity: 1; }
  }
  .scene-tab-btn-all {
    background: #162018;
    color: #81c784;
    border-color: #2e5935;
    margin-left: auto;
  }
  .scene-tab-btn-all:hover {
    background: #1e2c20;
    color: #a5d6a7;
    border-color: #388e3c;
  }
  .scene-tab-btn-all.active {
    background: #1b3820;
    color: #4ade80;
    border-color: #22c55e;
    box-shadow: 0 0 10px rgba(34, 197, 94, 0.35);
  }
'''

# Place tab_css right before </style>
content = content.replace('</style>', tab_css + '\n</style>')

# 3. Update SCENES_DATA
old_scenes_data_match = re.search(r'var SCENES_DATA = \[.*?\];\n  var ST = \{\};', content, re.DOTALL)
assert old_scenes_data_match, "SCENES_DATA block not matched!"

new_scenes_data = '''var SCENES_DATA = [
  {
    "scene": "[Act 0, Sc 1] Christ on the Cross",
    "sounds": [
      {
        "id": "SFX-01A",
        "label": "[SFX-01A] Clare's Initial Breath (Woman's Calming Breath)",
        "defCue": 0.0,
        "optLabels": ["Opt 1: Calming Breath (Direct 22s)", "Opt 2: Cathedral Reverb Halo (22s)", "Opt 3: Intimate Warm Tone (22s)"],
        "o1": "SFX/P1_PROLOGUE/SFX-01A_CALM_BREATH_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-01A_CALM_BREATH_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-01A_CALM_BREATH_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-01",
        "label": "[SFX-01] TV Turn On",
        "defCue": 4.0,
        "o1": "SFX/P1_PROLOGUE/SFX-01_TV_TURN_ON_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-01_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-01_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-02",
        "label": "[SFX-02] Mouse Clicks & Interface",
        "defCue": 7.0,
        "o1": "SFX/P1_PROLOGUE/SFX-02_MOUSE_CLICKS_INTERFACE_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-02_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-02_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-02B",
        "label": "[SFX-02B] Instagram & Social Media Alerts",
        "defCue": 10.0,
        "o1": "SFX/P1_PROLOGUE/SFX-02B_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-02B_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-02B_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-02C",
        "label": "[SFX-02C] Tinder Notification Alert",
        "defCue": 11.5,
        "optLabels": ["Opt 1: Clean Tinder Chime (Direct)", "Opt 2: Cathedral Reverb Chime", "Opt 3: Slapback Echo Chime"],
        "o1": "SFX/P1_PROLOGUE/SFX-02C_TINDER_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-02C_TINDER_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-02C_TINDER_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-03",
        "label": "[SFX-03] Traffic & City Bed",
        "defCue": 13.0,
        "o1": "SFX/P1_PROLOGUE/SFX-03_TRAFFIC_CITYBED_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-03_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-03_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-04A",
        "label": "[SFX-04A] Breaking Headline News",
        "defCue": 16.0,
        "optLabels": ["Opt 1: TV Breaking News (Anchor Duo)", "Opt 2: Live Newsroom Floor (Acoustic Room)", "Opt 3: AM Radio Broadcast EQ"],
        "o1": "SFX/P1_PROLOGUE/SFX-04A_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-04A_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-04A_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-04B",
        "label": "[SFX-04B] News of War & Conflict Sirens",
        "defCue": 20.0,
        "defPan": -0.55,
        "optLabels": ["Opt 1: Live War Correspondent (Balanced)", "Opt 2: Stage Left War Anchor (Panned)", "Opt 3: Shortwave Military Radio Filter"],
        "o1": "SFX/P1_PROLOGUE/SFX-04B_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-04B_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-04B_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-04C",
        "label": "[SFX-04C] Floods & Climate Disaster News",
        "defCue": 24.0,
        "defPan": 0.55,
        "optLabels": ["Opt 1: Flash Flood EAS Alert (Balanced)", "Opt 2: Stage Right Climate Anchor (Panned)", "Opt 3: Emergency Transistor Radio EQ"],
        "o1": "SFX/P1_PROLOGUE/SFX-04C_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-04C_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-04C_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-05",
        "label": "[SFX-05] Ambulance Siren",
        "defCue": 28.0,
        "optLabels": ["Opt 1: Passing Siren (Balanced)", "Opt 2: Doppler Pan Sweep (Stage Right ➜ Stage Left)", "Opt 3: Distant City Emergency"],
        "o1": "SFX/P1_PROLOGUE/SFX-05_AMBULANCE_EMERGENCY_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-05_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-05_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-06",
        "label": "[SFX-06] Commercials & Shopping Ads",
        "defCue": 32.0,
        "optLabels": ["Opt 1: Rapid-Fire TV Commercials & Beeps", "Opt 2: Shopping Mall P.A. Acoustic", "Opt 3: Hyper-Compressed Radio Promo Punch"],
        "o1": "SFX/P1_PROLOGUE/SFX-06_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-06_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-06_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-07",
        "label": "[SFX-07] Digital Glitch & System Breakdown",
        "defCue": 35.0,
        "optLabels": ["Opt 1: Full Glitch Attack (12s)", "Opt 2: Cathedral Reverb Glitch", "Opt 3: Lo-Fi Radio Glitch"],
        "o1": "SFX/P1_PROLOGUE/SFX-07_GLITCH_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-07_GLITCH_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-07_GLITCH_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-06B",
        "label": "[SFX-06B] 13th Century Historical Bleed",
        "defCue": 38.0,
        "o1": "SFX/P1_PROLOGUE/SFX-06B_REC_v01_RAW.wav",
        "o2": "SFX/P1_PROLOGUE/SFX-06B_REC_v02_RAW.wav",
        "o3": "SFX/P1_PROLOGUE/SFX-06B_REC_v03_RAW.wav"
      }
    ]
  },
  {
    "scene": "[Act I, Sc 2] The Meeting of Francis",
    "sounds": [
      {
        "id": "SFX-08",
        "label": "[SFX-08] Medieval Atmosphere",
        "defCue": 0.0,
        "o1": "SFX/A1_MARKET/SFX-08_REC_v01_RAW.wav",
        "o2": "SFX/A1_MARKET/SFX-08_REC_v02_RAW.wav",
        "o3": "SFX/A1_MARKET/SFX-08_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-09",
        "label": "[SFX-09] 13th C. Assisi Market (Carts & Calls)",
        "defCue": 6.0,
        "optLabels": ["Opt 1: Market Square (Full Panoramic)", "Opt 2: Left Alley Merchants (Panned Left)", "Opt 3: Right Carts & Street Bells (Panned Right)"],
        "o1": "SFX/A1_MARKET/SFX-09_REC_v01_RAW.wav",
        "o2": "SFX/A1_MARKET/SFX-09_REC_v02_RAW.wav",
        "o3": "SFX/A1_MARKET/SFX-09_REC_v03_RAW.wav"
      }
    ]
  },
  {
    "scene": "[Act I, Sc 3] The Escape",
    "sounds": [
      {
        "id": "SFX-33A",
        "label": "[SFX-33A] Canonical Heartbeat (Circling)",
        "defCue": 0.0,
        "o1": "SFX/00_GLOBAL/SFX-33A_HB_CANONICAL_REC_v01_RAW.wav",
        "o2": "SFX/00_GLOBAL/SFX-33A_REC_v02_RAW.wav",
        "o3": "SFX/00_GLOBAL/SFX-33A_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-10A",
        "label": "[SFX-10A] Palm Sunday Street Gathering (Bells & Chants)",
        "defCue": 18.0,
        "o1": "SFX/A2_THE_PASSION/SFX-10A_REC_v01_RAW.wav",
        "o2": "SFX/A2_THE_PASSION/SFX-10A_REC_v02_RAW.wav",
        "o3": "SFX/A2_THE_PASSION/SFX-10A_REC_v03_RAW.wav"
      }
    ]
  },
  {
    "scene": "[Act II, Sc 4] San Damiano",
    "sounds": [
      {
        "id": "SFX-35",
        "label": "[SFX-35] Lightning Strike",
        "defCue": 0.0,
        "optLabels": ["Opt 1: Sharp Crack", "Opt 2: Thunder Reverb Boom", "Opt 3: Distant Echo Rumble"],
        "o1": "SFX/B1_SAN_DAMIANO/SFX-35_LIGHTNING_REC_v01_RAW.wav",
        "o2": "SFX/B1_SAN_DAMIANO/SFX-35_REC_v02_RAW.wav",
        "o3": "SFX/B1_SAN_DAMIANO/SFX-35_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-36",
        "label": "[SFX-36] Voice of God (\\"Repair my house\\")",
        "defCue": 2.5,
        "optLabels": ["Opt 1: Direct Sacred Command (Take 2)", "Opt 2: Cathedral Reverb Halo & Sub-Bass (Take 1)", "Opt 3: Mystical Crucifix Vision"],
        "o1": "SFX/B1_SAN_DAMIANO/SFX-36_VOICEOFGOD_v01_RAW.wav",
        "o2": "SFX/B1_SAN_DAMIANO/SFX-36_VOICEOFGOD_v02_RAW.wav",
        "o3": "SFX/B1_SAN_DAMIANO/SFX-36_VOICEOFGOD_v03_RAW.wav"
      },
      {
        "id": "SFX-15",
        "label": "[SFX-15] Cicadas (Deus, Deus)",
        "defCue": 17.0,
        "optLabels": ["Opt 1: Close Summer Cicadas", "Opt 2: Ambient Field", "Opt 3: Distant Drone"],
        "o1": "SFX/B1_SAN_DAMIANO/SFX-15_REC_v01_RAW.wav",
        "o2": "SFX/B1_SAN_DAMIANO/SFX-15_REC_v02_RAW.wav",
        "o3": "SFX/B1_SAN_DAMIANO/SFX-15_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-34",
        "label": "[SFX-34] Cross Glitch (Father's intrusion)",
        "defCue": 25.0,
        "optLabels": ["Opt 1: Full Glitch Attack (12s)", "Opt 2: Cathedral Reverb Glitch", "Opt 3: Lo-Fi Radio Glitch"],
        "o1": "SFX/B1_SAN_DAMIANO/SFX-34_GLITCH_REC_v01_RAW.wav",
        "o2": "SFX/B1_SAN_DAMIANO/SFX-34_GLITCH_REC_v02_RAW.wav",
        "o3": "SFX/B1_SAN_DAMIANO/SFX-34_GLITCH_REC_v03_RAW.wav"
      }
    ]
  },
  {
    "scene": "[Act II, Sc 5] Sisterhood & Passing",
    "sounds": [
      {
        "id": "SFX-16_WATER",
        "label": "[SFX-16] Trickling Water (Stream Source)",
        "defCue": 0.0,
        "defPan": -0.35,
        "optLabels": ["Opt 1: Balanced Stream (Full Bed)", "Opt 2: Stage Left Courtyard Spring (Panned Left)", "Opt 3: Cavern Echo Stream"],
        "o1": "SFX/C2_SISTERHOOD/SFX-16_WATER_REC_v01_RAW.wav",
        "o2": "SFX/C2_SISTERHOOD/SFX-16_WATER_REC_v02_RAW.wav",
        "o3": "SFX/C2_SISTERHOOD/SFX-16_WATER_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-17_CANTICLE",
        "label": "[SFX-17] Canticle of the Creatures (Simon De Voil)",
        "defCue": 12.0,
        "optLabels": ["Opt 1: Simon De Voil (Acoustic)", "Opt 2: Reverb Sanctuary", "Opt 3: Ambient Echo"],
        "o1": "SFX/C2_SISTERHOOD/SFX-17_CANTICLE_REC_v01_RAW.wav",
        "o2": "SFX/C2_SISTERHOOD/SFX-17_CANTICLE_REC_v02_RAW.wav",
        "o3": "SFX/C2_SISTERHOOD/SFX-17_CANTICLE_REC_v03_RAW.wav"
      }
    ]
  },
  {
    "scene": "[Act III, Sc 6] Letters to Prague",
    "sounds": [
      {
        "id": "SFX-23",
        "label": "[SFX-23] Quill Pen Writing on Parchment",
        "defCue": 0.0,
        "defPan": 0.40,
        "optLabels": ["Opt 1: Crisp Quill Scratch (Direct 68s)", "Opt 2: Stage Right Writing Desk (Panned Right)", "Opt 3: Gentle Soft Writing"],
        "o1": "SFX/B1_SAN_DAMIANO/SFX-23_QUILL_REC_v01_RAW.wav",
        "o2": "SFX/B1_SAN_DAMIANO/SFX-23_QUILL_REC_v02_RAW.wav",
        "o3": "SFX/B1_SAN_DAMIANO/SFX-23_QUILL_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-37",
        "label": "[SFX-37] Agnes Letter VO (\\"Dear Agnes of Prague...\\")",
        "defCue": 0.0,
        "defPan": -0.20,
        "optLabels": ["Opt 1: Direct Sacred Intimacy (Clare's Cell)", "Opt 2: Letter Writing Bed (+ Quill Scratch Overlay)", "Opt 3: Cloister Reverb Halo (Stone Room Decay)"],
        "o1": "SFX/D1_LETTER/SFX-37_AGNES_VO_v01_RAW.wav",
        "o2": "SFX/D1_LETTER/SFX-37_AGNES_VO_v02_RAW.wav",
        "o3": "SFX/D1_LETTER/SFX-37_AGNES_VO_v03_RAW.wav"
      }
    ]
  },
  {
    "scene": "[Act III, Sc 7] The Siege",
    "sounds": [
      {
        "id": "SFX-D2_WAR",
        "label": "[SFX-D2] Medieval War Soundscape (SoundofTime)",
        "defCue": 0.0,
        "defPan": -0.2,
        "optLabels": ["Opt 1: Canonical War Soundscape (17.6s)", "Opt 2: Convent Interior Muffled (Stone Wall)", "Opt 3: Wide Valley Reverb"],
        "o1": "SFX/D2_SIEGE/SFX-D2_WAR_v01_RAW.wav",
        "o2": "SFX/D2_SIEGE/SFX-D2_WAR_v02_RAW.wav",
        "o3": "SFX/D2_SIEGE/SFX-D2_WAR_v03_RAW.wav"
      },
      {
        "id": "SFX-D2_DRUMS",
        "label": "[SFX-D2] Medieval War Drums (Der Wikinger)",
        "defCue": 0.0,
        "defPan": 0.2,
        "optLabels": ["Opt 1: Full War Drums (142.5s)", "Opt 2: Heavy Sub-Bass Pulsing Drums", "Opt 3: Distant Valley Siege Drums"],
        "o1": "SFX/D2_SIEGE/SFX-D2_DRUMS_v01_RAW.wav",
        "o2": "SFX/D2_SIEGE/SFX-D2_DRUMS_v02_RAW.wav",
        "o3": "SFX/D2_SIEGE/SFX-D2_DRUMS_v03_RAW.wav"
      },
      {
        "id": "SFX-D2_VO",
        "label": "[SFX-D2_VO] Sister's Warning VO (\\"The soldiers are coming!\\")",
        "defCue": 0.0,
        "defPan": -0.25,
        "optLabels": ["Opt 1: Stone Cloister Reverb (Vocal Focus)", "Opt 2: Sanctuary Defense (Alarm Bells & Early Gate Slam)", "Opt 3: Spatial Panic Pan (Continuous Bells & 50% Gate Slam)"],
        "o1": "SFX/D2_SIEGE/SFX-D2_VO_v01_RAW.wav",
        "o2": "SFX/D2_SIEGE/SFX-D2_VO_v02_RAW.wav",
        "o3": "SFX/D2_SIEGE/SFX-D2_VO_v03_RAW.wav"
      },
      {
        "id": "SFX-D2_GATE",
        "label": "[SFX-D2_GATE] Convent Defense (Oak Gate Slam & Alarm Bells)",
        "defCue": 13.0,
        "defPan": -0.4,
        "optLabels": ["Opt 1: Massive Oak Gate Slam & Iron Bolt Barring", "Opt 2: Sanctuary Alarm Bells + Heavy Gate Slam", "Opt 3: Rushing Footsteps into Heavy Gate Slam"],
        "o1": "SFX/D2_SIEGE/SFX-D2_GATE_v01_RAW.wav",
        "o2": "SFX/D2_SIEGE/SFX-D2_GATE_v02_RAW.wav",
        "o3": "SFX/D2_SIEGE/SFX-D2_GATE_v03_RAW.wav"
      },
      {
        "id": "SFX-33A_D2",
        "label": "[SFX-33A] Canonical Heartbeat (Siege Prayer & Letter 2)",
        "defCue": 16.0,
        "optLabels": ["Opt 1: Intimate Pulse", "Opt 2: Sub-Bass Reverb", "Opt 3: Muffled Throbbing"],
        "o1": "SFX/00_GLOBAL/SFX-33A_HB_CANONICAL_REC_v01_RAW.wav",
        "o2": "SFX/00_GLOBAL/SFX-33A_REC_v02_RAW.wav",
        "o3": "SFX/00_GLOBAL/SFX-33A_REC_v03_RAW.wav"
      },
      {
        "id": "SFX-CHILD_GOD",
        "label": "[SFX-CG] Voice of Christ as a Child (\\"I will always protect you\\")",
        "defCue": 29.5,
        "optLabels": ["Opt 1: Clean Vocal (Direct)", "Opt 2: Cathedral Reverb Halo", "Opt 3: Warm Intimate Tone"],
        "o1": "SFX/D2_SIEGE/SFX-CHILD_GOD_REC_v01_RAW.wav",
        "o2": "SFX/D2_SIEGE/SFX-CHILD_GOD_REC_v02_RAW.wav",
        "o3": "SFX/D2_SIEGE/SFX-CHILD_GOD_REC_v03_RAW.wav",
        "subOctLabels": ["Opt 1: Clean Vocal + Sub-Bass Overlay (10%➜50%)", "Opt 2: Cathedral Halo + Sub-Bass Overlay (10%➜50%)", "Opt 3: Warm Intimate + Sub-Bass Overlay (10%➜50%)"],
        "subOct1": "SFX/D2_SIEGE/SFX-CHILD_GOD_SUBOCT_v01_RAW.wav",
        "subOct2": "SFX/D2_SIEGE/SFX-CHILD_GOD_SUBOCT_v02_RAW.wav",
        "subOct3": "SFX/D2_SIEGE/SFX-CHILD_GOD_SUBOCT_v03_RAW.wav",
        "slowLabels": ["Opt 1: Clean Vocal (Slow-Down 7.8s)", "Opt 2: Cathedral Reverb Halo (Slow-Down 8.1s)", "Opt 3: Warm Intimate Tone (Slow-Down 7.8s)"],
        "slow1": "SFX/D2_SIEGE/SFX-CHILD_GOD_REC_SLOW_v01_RAW.wav",
        "slow2": "SFX/D2_SIEGE/SFX-CHILD_GOD_REC_SLOW_v02_RAW.wav",
        "slow3": "SFX/D2_SIEGE/SFX-CHILD_GOD_REC_SLOW_v03_RAW.wav",
        "subOctSlowLabels": ["Opt 1: Clean Vocal + Sub-Bass Overlay (Slow 7.8s)", "Opt 2: Cathedral Halo + Sub-Bass Overlay (Slow 8.1s)", "Opt 3: Warm Intimate + Sub-Bass Overlay (Slow 7.8s)"],
        "subOctSlow1": "SFX/D2_SIEGE/SFX-CHILD_GOD_SUBOCT_SLOW_v01_RAW.wav",
        "subOctSlow2": "SFX/D2_SIEGE/SFX-CHILD_GOD_SUBOCT_SLOW_v02_RAW.wav",
        "subOctSlow3": "SFX/D2_SIEGE/SFX-CHILD_GOD_SUBOCT_SLOW_v03_RAW.wav"
      },
      {
        "id": "SFX-26",
        "label": "[SFX-26] Divine Warp / Time Travel Shockwave",
        "defCue": 33.0,
        "optLabels": ["Opt 1: Direct Time Travel Warp (5.6s)", "Opt 2: Cathedral Reverb Warp", "Opt 3: Sub-Bass Heavy Warp"],
        "o1": "SFX/D2_SIEGE/SFX-26_TIMETRAVEL_REC_v01_RAW.wav",
        "o2": "SFX/D2_SIEGE/SFX-26_TIMETRAVEL_REC_v02_RAW.wav",
        "o3": "SFX/D2_SIEGE/SFX-26_TIMETRAVEL_REC_v03_RAW.wav"
      }
    ]
  },
  {
    "scene": "[Act IV, Sc 8] The Christmas Vision",
    "sounds": [
      {
        "id": "SFX-38_CHRISTMAS_MASS",
        "label": "[SFX-38] Christmas Mass Liturgy & Chants (15m Bed)",
        "defCue": 0.0,
        "defPan": 0.0,
        "optLabels": ["Opt 1: Full Sacred Liturgy Bed (15:00 min)", "Opt 2: Cathedral Reverb Overlay (15:00 min)", "Opt 3: Mystical Vision Swell (15:00 min)"],
        "o1": "SFX/D6_CHRISTMAS_MASS/SFX-38_CHRISTMAS_MASS_v01_RAW.wav",
        "o2": "SFX/D6_CHRISTMAS_MASS/SFX-38_CHRISTMAS_MASS_v02_RAW.wav",
        "o3": "SFX/D6_CHRISTMAS_MASS/SFX-38_CHRISTMAS_MASS_v03_RAW.wav"
      },
      {
        "id": "SFX-23_PAPAL",
        "label": "[SFX-23] Papal Seal & Document Tactile Cue",
        "defCue": 15.0,
        "defPan": 0.35,
        "optLabels": ["Opt 1: Crisp Parchment & Seal Presentation", "Opt 2: Stage Right Desk Acoustics", "Opt 3: Soft Sacred Reverence"],
        "o1": "SFX/B1_SAN_DAMIANO/SFX-23_QUILL_REC_v01_RAW.wav",
        "o2": "SFX/B1_SAN_DAMIANO/SFX-23_QUILL_REC_v02_RAW.wav",
        "o3": "SFX/B1_SAN_DAMIANO/SFX-23_QUILL_REC_v03_RAW.wav"
      }
    ]
  },
  {
    "scene": "[Act IV, Sc 9] Final Gaze & Blackout",
    "sounds": [
      {
        "id": "SFX-30_CAUSTIC",
        "label": "[SFX-30] Water Font Caustic Drone (Blackout Meditation)",
        "defCue": 0.0,
        "defPan": 0.0,
        "optLabels": ["Opt 1: Sacred Caustic Light Hum", "Opt 2: Sub-Bass Caustic Drone", "Opt 3: Expanded Meditation Drone"],
        "o1": "SFX/D6_CHRISTMAS_MASS/SFX-30_CAUSTIC_REC_v01_RAW.wav",
        "o2": "SFX/D6_CHRISTMAS_MASS/SFX-30_CAUSTIC_REC_v02_RAW.wav",
        "o3": "SFX/D6_CHRISTMAS_MASS/SFX-30_CAUSTIC_REC_v03_RAW.wav"
      }
    ]
  }
];
  var ST = {};'''

content = content.replace(old_scenes_data_match.group(0), new_scenes_data)

# 4. Bump STORAGE_KEY to v16
content = content.replace("var STORAGE_KEY = 'to_gaze_soundboard_sequencer_v15';", "var STORAGE_KEY = 'to_gaze_soundboard_sequencer_v16';")

# 5. Update loadStateFromStorage to migrate legacy keys and check v15 fallback
old_load = "var raw = localStorage.getItem(STORAGE_KEY) || localStorage.getItem('to_gaze_soundboard_sequencer_v14')"
new_load = "var raw = localStorage.getItem(STORAGE_KEY) || localStorage.getItem('to_gaze_soundboard_sequencer_v15') || localStorage.getItem('to_gaze_soundboard_sequencer_v14')"
content = content.replace(old_load, new_load)

# Add legacy mapping inside loadStateFromStorage:
legacy_map_code = '''      if (parsed && parsed.scenes) {
        var LEGACY_ID_MAP = {
          'P1_PROLOGUE': '_Act_0__Sc_1__Christ_on_the_Cross',
          'A1_MARKET': '_Act_I__Sc_2__The_Meeting_of_Francis',
          'A2_THE_PASSION': '_Act_I__Sc_3__The_Escape',
          'B1_SAN_DAMIANO': '_Act_II__Sc_4__San_Damiano',
          'C2_SISTERHOOD': '_Act_II__Sc_5__Sisterhood___Passing',
          'D1_LETTERS_TO_PRAGUE': '_Act_III__Sc_6__Letters_to_Prague',
          'D2_SIEGE': '_Act_III__Sc_7__The_Siege',
          'D6_CHRISTMAS_MASS': '_Act_IV__Sc_8__The_Christmas_Vision'
        };
        Object.keys(LEGACY_ID_MAP).forEach(function(oldId){
          if (parsed.scenes[oldId] && !parsed.scenes[LEGACY_ID_MAP[oldId]]) {
            parsed.scenes[LEGACY_ID_MAP[oldId]] = parsed.scenes[oldId];
          }
        });
      }'''

old_parsed_sounds = "if (parsed && parsed.sounds) {"
content = content.replace(old_parsed_sounds, legacy_map_code + "\n      if (parsed && parsed.sounds) {")

# 6. Default duration for Christmas Vision to 900s, max duration input to 1800s
old_sc_dur = "duration: savedSc ? savedSc.duration : 60.0,"
new_sc_dur = "duration: savedSc ? savedSc.duration : (scId.indexOf('Christmas_Vision') !== -1 ? 900.0 : 60.0),"
content = content.replace(old_sc_dur, new_sc_dur)

content = content.replace('min="10" max="600" step="5"', 'min="10" max="1800" step="5"')
content = content.replace('val = Math.max(10, Math.min(600, val));', 'val = Math.max(10, Math.min(1800, val));')

# 7. Add Tab Switching Functions and Wiring in renderSoundboard
tab_js_funcs = '''
  var currentTab = localStorage.getItem('to_gaze_active_tab') || 'ALL';

  function updateTabPlayingState(scId, isPlaying) {
    var btn = document.querySelector('.scene-tab-btn[data-tab-id="' + scId + '"]');
    if (btn) {
      if (isPlaying) btn.classList.add('playing');
      else btn.classList.remove('playing');
    }
  }

  function updateAllTabsPlayingState(isPlaying) {
    document.querySelectorAll('.scene-tab-btn').forEach(function(b){
      if (isPlaying) b.classList.add('playing');
      else b.classList.remove('playing');
    });
  }

  function switchTab(tabId) {
    currentTab = tabId;
    localStorage.setItem('to_gaze_active_tab', tabId);

    document.querySelectorAll('.scene-tab-btn').forEach(function(b){
      if (b.getAttribute('data-tab-id') === tabId) {
        b.classList.add('active');
      } else {
        b.classList.remove('active');
      }
    });

    SCENES_DATA.forEach(function(scData){
      var scId = safeId(scData.scene);
      var sec = document.getElementById('sc-sec-' + scId);
      if (!sec) return;
      if (tabId === 'ALL' || tabId === scId) {
        sec.style.display = 'block';
      } else {
        sec.style.display = 'none';
      }
    });
  }
'''

content = content.replace('function safeId(str) {', tab_js_funcs + '\n  function safeId(str) {')

# Hook updateTabPlayingState into playScene, pauseScene, resetScene, stopAll, fadeOutAll
content = content.replace("btn.classList.add('playing');\n    }", "btn.classList.add('playing');\n      updateTabPlayingState(scId, true);\n    }")
content = content.replace("btn.classList.remove('playing');\n    }", "btn.classList.remove('playing');\n      updateTabPlayingState(scId, false);\n    }")
content = content.replace("function stopAll() {", "function stopAll() {\n    updateAllTabsPlayingState(false);")
content = content.replace("function fadeOutAll() {", "function fadeOutAll() {\n    updateAllTabsPlayingState(false);")

# Build the tab buttons inside renderSoundboard
old_app_build = '''    var saved = loadStateFromStorage();

    SCENES_DATA.forEach(function(scData){'''

new_app_build = '''    var saved = loadStateFromStorage();

    // Render 9 Script-Aligned Tabs Bar
    var tabBar = document.getElementById('scene-tab-bar');
    if (tabBar) {
      tabBar.innerHTML = '';
      SCENES_DATA.forEach(function(scData){
        var scId = safeId(scData.scene);
        var btn = document.createElement('button');
        btn.className = 'scene-tab-btn';
        btn.setAttribute('data-tab-id', scId);
        btn.innerHTML = '<span class="tab-dot"></span> ' + scData.scene;
        btn.addEventListener('click', function(){
          switchTab(scId);
        });
        tabBar.appendChild(btn);
      });

      var btnAll = document.createElement('button');
      btnAll.className = 'scene-tab-btn scene-tab-btn-all';
      btnAll.setAttribute('data-tab-id', 'ALL');
      btnAll.innerHTML = '<span class="tab-dot"></span> 🌐 Show All Scenes';
      btnAll.addEventListener('click', function(){
        switchTab('ALL');
      });
      tabBar.appendChild(btnAll);
    }

    SCENES_DATA.forEach(function(scData){'''

assert old_app_build in content, "old_app_build not found!"
content = content.replace(old_app_build, new_app_build)

# At the end of renderSoundboard, apply currentTab
old_render_end = '''    var rstBtn = document.getElementById('btn-reset-defaults');
    if (rstBtn) rstBtn.addEventListener('click', resetToDefaults);
  }'''

new_render_end = '''    var rstBtn = document.getElementById('btn-reset-defaults');
    if (rstBtn) rstBtn.addEventListener('click', resetToDefaults);

    // Initialize Tab view (restore saved tab or show first scene)
    var initialTab = localStorage.getItem('to_gaze_active_tab') || safeId(SCENES_DATA[0].scene);
    switchTab(initialTab);
  }'''

assert old_render_end in content, "old_render_end not found!"
content = content.replace(old_render_end, new_render_end)

with open('Rehearsal_Soundboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Rehearsal_Soundboard.html updated successfully with 9 tabs!")
