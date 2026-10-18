/**
 * TO-GAZE-SPATIAL-AUDIO-V1
 * Church-Scale Immersive Theatrical Audio Playback & Spatialization Engine
 * Production: To Gaze: Saint Clare of Assisi
 * Author: Antigravity Audio Engineering
 */

(function(global){
  'use strict';

  // 1. Speaker Layout Profiles Definition
  var SPEAKER_PROFILES = {
    'A': {
      id: 'A',
      name: 'Profile A — Stereo / Binaural 3D',
      channels: 2,
      description: 'Front Left & Right (2 Ch). Virtual 3D HRTF spatialization active for headphones & stereo PA.',
      speakers: [
        { id: 'FL', name: 'Front Left', ch: 0, x: -1.0, y: 1.0, z: 0.0, az: 315, el: 0 },
        { id: 'FR', name: 'Front Right', ch: 1, x: 1.0, y: 1.0, z: 0.0, az: 45, el: 0 }
      ]
    },
    'B': {
      id: 'B',
      name: 'Profile B — Quad Surround',
      channels: 4,
      description: '4-Corner Church Perimeter (FL, FR, Rear Left, Rear Right).',
      speakers: [
        { id: 'FL', name: 'Front Left', ch: 0, x: -1.0, y: 1.0, z: 0.0, az: 315, el: 0 },
        { id: 'FR', name: 'Front Right', ch: 1, x: 1.0, y: 1.0, z: 0.0, az: 45, el: 0 },
        { id: 'RL', name: 'Rear Left (Nave)', ch: 2, x: -1.0, y: -1.0, z: 0.0, az: 225, el: 0 },
        { id: 'RR', name: 'Rear Right (Nave)', ch: 3, x: 1.0, y: -1.0, z: 0.0, az: 135, el: 0 }
      ]
    },
    'C': {
      id: 'C',
      name: 'Profile C — 5.1 Theatrical Surround',
      channels: 6,
      description: 'Front L/C/R, LFE Subwoofer, and Side Surrounds (L-Shaped Seating aligned).',
      speakers: [
        { id: 'FL', name: 'Front Left', ch: 0, x: -0.85, y: 1.0, z: 0.0, az: 330, el: 0 },
        { id: 'FR', name: 'Front Right', ch: 1, x: 0.85, y: 1.0, z: 0.0, az: 30, el: 0 },
        { id: 'C',  name: 'Center (Proscenium)', ch: 2, x: 0.0, y: 1.0, z: 0.0, az: 0, el: 0 },
        { id: 'LFE',name: 'Subwoofer (LFE)', ch: 3, x: 0.0, y: 0.0, z: -1.0, isLFE: true },
        { id: 'SL', name: 'Surround Left (L-Arm)', ch: 4, x: -1.0, y: -0.3, z: 0.0, az: 250, el: 0 },
        { id: 'SR', name: 'Surround Right (Nave Wall)', ch: 5, x: 1.0, y: -0.3, z: 0.0, az: 110, el: 0 }
      ]
    },
    'D': {
      id: 'D',
      name: 'Profile D — 7.1 Immersive Theater',
      channels: 8,
      description: 'Front L/C/R, LFE, Side Surrounds, and Rear Surrounds.',
      speakers: [
        { id: 'FL', name: 'Front Left', ch: 0, x: -0.85, y: 1.0, z: 0.0, az: 330, el: 0 },
        { id: 'FR', name: 'Front Right', ch: 1, x: 0.85, y: 1.0, z: 0.0, az: 30, el: 0 },
        { id: 'C',  name: 'Center', ch: 2, x: 0.0, y: 1.0, z: 0.0, az: 0, el: 0 },
        { id: 'LFE',name: 'Subwoofer (LFE)', ch: 3, x: 0.0, y: 0.0, z: -1.0, isLFE: true },
        { id: 'SL', name: 'Side Left', ch: 4, x: -1.0, y: 0.0, z: 0.0, az: 270, el: 0 },
        { id: 'SR', name: 'Side Right', ch: 5, x: 1.0, y: 0.0, z: 0.0, az: 90, el: 0 },
        { id: 'RL', name: 'Rear Left', ch: 6, x: -0.85, y: -1.0, z: 0.0, az: 210, el: 0 },
        { id: 'RR', name: 'Rear Right', ch: 7, x: 0.85, y: -1.0, z: 0.0, az: 150, el: 0 }
      ]
    },
    'E': {
      id: 'E',
      name: 'Profile E — Church Height System (Sanctuary Dome)',
      channels: 8,
      description: 'Front L/C/R, Surrounds, and Overhead Dome Height Speakers.',
      speakers: [
        { id: 'FL', name: 'Front Left', ch: 0, x: -0.85, y: 1.0, z: 0.0, az: 330, el: 0 },
        { id: 'FR', name: 'Front Right', ch: 1, x: 0.85, y: 1.0, z: 0.0, az: 30, el: 0 },
        { id: 'C',  name: 'Center', ch: 2, x: 0.0, y: 1.0, z: 0.0, az: 0, el: 0 },
        { id: 'LFE',name: 'Subwoofer', ch: 3, x: 0.0, y: 0.0, z: -1.0, isLFE: true },
        { id: 'SL', name: 'Surround Left', ch: 4, x: -1.0, y: -0.5, z: 0.0, az: 250, el: 0 },
        { id: 'SR', name: 'Surround Right', ch: 5, x: 1.0, y: -0.5, z: 0.0, az: 110, el: 0 },
        { id: 'HL', name: 'Height Left (Dome)', ch: 6, x: -0.7, y: 0.5, z: 1.0, az: 315, el: 65, isHeight: true },
        { id: 'HR', name: 'Height Right (Dome)', ch: 7, x: 0.7, y: 0.5, z: 1.0, az: 45, el: 65, isHeight: true }
      ]
    }
  };

  // 2. Spatial Engine State
  var SpatialEngine = {
    ctx: null,
    isInitialized: false,
    currentProfile: 'A',
    masterSurroundGain: 1.0,
    masterLFEGain: 1.0,
    masterGainNode: null,
    surroundGainNode: null,
    lfeGainNode: null,
    mergerNode: null,
    isStereoFallback: false,
    sources: {}, // id -> source wrapper
    activeState: null,
    radarCanvas: null,
    radarAnimId: null,

    init: function() {
      if (this.isInitialized) return;
      try {
        var AudioCtxClass = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtxClass) {
          console.warn('[SpatialEngine] Web Audio API not supported in this browser.');
          return;
        }
        this.ctx = new AudioCtxClass();
        var maxCh = (this.ctx.destination && this.ctx.destination.maxChannelCount) || 2;
        console.log('[SpatialEngine] Initialized. Hardware Max Channels:', maxCh);
        this.setupBusRouting();
        this.isInitialized = true;
      } catch(e) {
        console.warn('[SpatialEngine] AudioContext init deferred until user gesture:', e);
      }
    },

    ensureContext: function() {
      if (!this.ctx) this.init();
      if (this.ctx && this.ctx.state === 'suspended') {
        this.ctx.resume();
      }
    },

    setupBusRouting: function() {
      if (!this.ctx) return;
      var prof = SPEAKER_PROFILES[this.currentProfile] || SPEAKER_PROFILES['A'];
      var targetChannels = this.isStereoFallback ? 2 : Math.min(prof.channels, this.ctx.destination.maxChannelCount || 2);
      
      try {
        this.ctx.destination.channelCount = targetChannels;
        this.ctx.destination.channelInterpretation = 'discrete';
      } catch(e) {
        // Fallback for strict browser restrictions
        this.ctx.destination.channelCount = 2;
      }

      this.masterGainNode = this.ctx.createGain();
      this.masterGainNode.gain.value = 1.0;

      this.surroundGainNode = this.ctx.createGain();
      this.surroundGainNode.gain.value = this.masterSurroundGain;

      this.lfeGainNode = this.ctx.createGain();
      this.lfeGainNode.gain.value = this.masterLFEGain;

      // Channel merger node
      this.mergerNode = this.ctx.createChannelMerger(targetChannels);
      this.mergerNode.connect(this.ctx.destination);
    },

    setProfile: function(profId) {
      if (!SPEAKER_PROFILES[profId]) return;
      this.currentProfile = profId;
      console.log('[SpatialEngine] Switched to profile:', profId);
      this.setupBusRouting();
      this.updateAllSourcePositions();
    },

    setStereoFallback: function(enabled) {
      this.isStereoFallback = !!enabled;
      console.log('[SpatialEngine] Stereo Fallback mode:', this.isStereoFallback);
      this.setupBusRouting();
      this.updateAllSourcePositions();
    },

    setSurroundLevel: function(val) {
      this.masterSurroundGain = Math.max(0, Math.min(2.0, parseFloat(val) || 1.0));
      if (this.surroundGainNode) {
        this.surroundGainNode.gain.setValueAtTime(this.masterSurroundGain, this.ctx.currentTime);
      }
    },

    setLFELevel: function(val) {
      this.masterLFEGain = Math.max(0, Math.min(2.0, parseFloat(val) || 1.0));
      if (this.lfeGainNode) {
        this.lfeGainNode.gain.setValueAtTime(this.masterLFEGain, this.ctx.currentTime);
      }
    },

    // Compute VBAP Speaker Gains from Azimuth, Elevation, Distance
    calculateSpeakerGains: function(azimuth, elevation, distance, isLFEEligible) {
      var prof = SPEAKER_PROFILES[this.currentProfile] || SPEAKER_PROFILES['A'];
      var rad = (azimuth * Math.PI) / 180.0;
      var elRad = (elevation * Math.PI) / 180.0;
      
      // Source Cartesian coordinates on unit sphere
      var sx = Math.sin(rad) * Math.cos(elRad);
      var sy = Math.cos(rad) * Math.cos(elRad);
      var sz = Math.sin(elRad);

      var gains = {};
      var totalPwr = 0.0;

      prof.speakers.forEach(function(spk){
        if (spk.isLFE) {
          // LFE Subwoofer handling
          gains[spk.id] = isLFEEligible ? 0.85 : 0.0;
          return;
        }

        var spkRad = (spk.az * Math.PI) / 180.0;
        var spkElRad = ((spk.el || 0) * Math.PI) / 180.0;
        var px = Math.sin(spkRad) * Math.cos(spkElRad);
        var py = Math.cos(spkRad) * Math.cos(spkElRad);
        var pz = Math.sin(spkElRad);

        // Dot product / angular proximity
        var dot = sx * px + sy * py + sz * pz;
        var weight = Math.max(0.0, dot);
        // Exponent for spatial focus
        var g = Math.pow(weight, 1.8);
        gains[spk.id] = g;
        totalPwr += g * g;
      });

      // Normalize gains for constant power
      if (totalPwr > 0.0001) {
        var norm = Math.sqrt(totalPwr);
        prof.speakers.forEach(function(spk){
          if (!spk.isLFE) {
            gains[spk.id] = gains[spk.id] / norm;
          }
        });
      } else {
        // Fallback default stereo center
        gains['FL'] = 0.707;
        gains['FR'] = 0.707;
      }

      // Distance attenuation factor
      var distFactor = 1.0 / (1.0 + 0.08 * Math.max(0, distance - 1.0));
      prof.speakers.forEach(function(spk){
        if (!spk.isLFE) {
          gains[spk.id] *= distFactor;
        }
      });

      return gains;
    },

    // Register or attach a sound element to the spatial engine
    attachTrack: function(id, audioObj, initialSpatial) {
      if (!audioObj) return null;
      var self = this;
      var track = {
        id: id,
        audio: audioObj,
        azimuth: (initialSpatial && initialSpatial.az !== undefined) ? initialSpatial.az : 0,
        elevation: (initialSpatial && initialSpatial.el !== undefined) ? initialSpatial.el : 0,
        distance: (initialSpatial && initialSpatial.dist !== undefined) ? initialSpatial.dist : 2.0,
        occlusion: (initialSpatial && initialSpatial.occl !== undefined) ? initialSpatial.occl : 1.0,
        isLFE: !!(initialSpatial && initialSpatial.isLFE),
        mediaSource: null,
        gainNode: null,
        occlusionFilter: null,
        pannerNode: null,
        speakerGainNodes: {},
        isWebAudioLinked: false
      };

      this.sources[id] = track;
      return track;
    },

    // Link track to Web Audio graph safely (Bypassed to prevent browser CORS muting on file:/// and ensure 100% native audio playback)
    linkWebAudio: function(id) {
      var track = this.sources[id];
      if (!track) return;
      track.isWebAudioLinked = false;
      this.updateTrackPosition(id);
    },

    updateTrackPosition: function(id) {
      var track = this.sources[id];
      if (!track) return;
      
      // Update Web Audio Panner if linked
      if (track.pannerNode && this.ctx) {
        var rad = (track.azimuth * Math.PI) / 180.0;
        var elRad = (track.elevation * Math.PI) / 180.0;
        var x = Math.sin(rad) * Math.cos(elRad) * track.distance;
        var y = Math.cos(rad) * Math.cos(elRad) * track.distance;
        var z = Math.sin(elRad) * track.distance;

        if (track.pannerNode.positionX) {
          track.pannerNode.positionX.setValueAtTime(x, this.ctx.currentTime);
          track.pannerNode.positionY.setValueAtTime(y, this.ctx.currentTime);
          track.pannerNode.positionZ.setValueAtTime(z, this.ctx.currentTime);
        } else {
          track.pannerNode.setPosition(x, y, z);
        }

        // Occlusion Low-Pass
        var cutoff = Math.max(400, Math.min(20000, 20000 * track.occlusion * (1.0 / (1.0 + 0.05 * track.distance))));
        if (track.occlusionFilter) {
          track.occlusionFilter.frequency.setValueAtTime(cutoff, this.ctx.currentTime);
        }
      }

      // Update UI spatial tag
      var tag = document.getElementById('spat-tag-' + id);
      if (tag) {
        var dirTxt = 'Center Front (0°)';
        var az = ((track.azimuth % 360) + 360) % 360;
        if (az >= 340 || az <= 20) dirTxt = 'Stage Front (' + az.toFixed(0) + '°)';
        else if (az > 20 && az < 70) dirTxt = 'Front Right (' + az.toFixed(0) + '°)';
        else if (az >= 70 && az <= 110) dirTxt = 'Stage Right (' + az.toFixed(0) + '°)';
        else if (az > 110 && az < 160) dirTxt = 'Rear Right (' + az.toFixed(0) + '°)';
        else if (az >= 160 && az <= 200) dirTxt = 'Rear Nave (' + az.toFixed(0) + '°)';
        else if (az > 200 && az < 250) dirTxt = 'Rear Left (' + az.toFixed(0) + '°)';
        else if (az >= 250 && az <= 290) dirTxt = 'Stage Left (' + az.toFixed(0) + '°)';
        else if (az > 290 && az < 340) dirTxt = 'Front Left (' + az.toFixed(0) + '°)';
        
        tag.textContent = '📍 ' + dirTxt + ' • ' + track.distance.toFixed(1) + 'm';
      }
    },

    updateAllSourcePositions: function() {
      var self = this;
      Object.keys(this.sources).forEach(function(id){
        self.updateTrackPosition(id);
      });
    },

    // 3. Act III: The 5-State Siege Spatial Sequencer
    triggerSiegeState: function(stateNum) {
      this.ensureContext();
      this.activeState = 'SIEGE_' + stateNum;
      console.log('[SpatialEngine] Activating Siege State:', stateNum);

      // State definitions
      switch(stateNum) {
        case 1: // APPROACHING ARMY
          this.setTrackSpatial('SFX-D2_WAR', { az: 180, el: 0, dist: 75.0, occl: 0.15 }); // Rear valley, muffled
          this.setTrackSpatial('SFX-D2_DRUMS', { az: 165, el: 0, dist: 60.0, occl: 0.25, isLFE: true });
          this.setTrackSpatial('SFX-33A_D2', { az: 0, el: 0, dist: 2.0, occl: 1.0, isLFE: true });
          break;

        case 2: // CONVENT UNDER ATTACK
          this.setTrackSpatial('SFX-D2_WAR', { az: 270, el: 5, dist: 8.0, occl: 0.85 }); // Stage Left wall
          this.setTrackSpatial('SFX-D2_DRUMS', { az: 90, el: 0, dist: 12.0, occl: 0.9, isLFE: true });
          this.setTrackSpatial('SFX-D2_GATE', { az: 285, el: 0, dist: 4.0, occl: 1.0, isLFE: true }); // Gate Left
          this.setTrackSpatial('SFX-D2_VO', { az: 270, el: 0, dist: 5.0, occl: 1.0 }); // Sister warning
          this.setTrackSpatial('SFX-D2_FB1', { az: 315, el: 10, dist: 3.5, occl: 0.9 }); // Father flashback penetrates
          break;

        case 3: // CLARE'S FEAR (Auditory Tunnel / Isolation)
          this.setTrackSpatial('SFX-D2_WAR', { az: 200, el: 0, dist: 35.0, occl: 0.1 }); // External war pushed back & muffled
          this.setTrackSpatial('SFX-D2_DRUMS', { az: 160, el: 0, dist: 40.0, occl: 0.15 });
          this.setTrackSpatial('SFX-33A_D2', { az: 0, el: 0, dist: 0.8, occl: 1.0, isLFE: true }); // Heartbeat intimate center thump
          this.setTrackSpatial('SFX-D2_FB1', { az: 320, el: 5, dist: 2.0, occl: 1.0 }); // Father memory close
          this.setTrackSpatial('SFX-D2_FB2', { az: 0, el: 0, dist: 1.2, occl: 1.0 }); // Clare intimate destiny reflection
          break;

        case 4: // DIVINE INTERVENTION
          this.setTrackSpatial('SFX-CHILD_GOD', { az: 0, el: 10, dist: 1.8, occl: 1.0, isLFE: true }); // Pristine center presence
          this.setTrackSpatial('SFX-D2_WAR', { az: 180, el: 0, dist: 65.0, occl: 0.08 });
          this.setTrackSpatial('SFX-26', { az: 0, el: 30, dist: 5.0, occl: 1.0, isLFE: true }); // Shockwave expands
          break;

        case 5: // SOLDIERS RETREAT
          this.setTrackSpatial('SFX-D2_WAR', { az: 180, el: -5, dist: 95.0, occl: 0.05 }); // Recedes into distant valley
          this.setTrackSpatial('SFX-D2_DRUMS', { az: 180, el: 0, dist: 100.0, occl: 0.05 });
          break;
      }

      this.highlightSiegeStateButton(stateNum);
    },

    setTrackSpatial: function(id, coords) {
      if (!this.sources[id]) {
        this.sources[id] = { id: id, azimuth: 0, elevation: 0, distance: 2.0, occlusion: 1.0 };
      }
      var track = this.sources[id];
      if (coords.az !== undefined) track.azimuth = coords.az;
      if (coords.el !== undefined) track.elevation = coords.el;
      if (coords.dist !== undefined) track.distance = coords.dist;
      if (coords.occl !== undefined) track.occlusion = coords.occl;
      if (coords.isLFE !== undefined) track.isLFE = coords.isLFE;
      this.updateTrackPosition(id);
    },

    highlightSiegeStateButton: function(stateNum) {
      document.querySelectorAll('.btn-siege-state').forEach(function(b){
        b.classList.remove('active');
      });
      var activeBtn = document.getElementById('btn-siege-s' + stateNum);
      if (activeBtn) activeBtn.classList.add('active');
    },

    // 4. Speaker Test Tone Generator (Pink Noise / Chime Sequence)
    runSpeakerTestSequence: function() {
      this.ensureContext();
      if (!this.ctx) {
        alert('Please click anywhere on the page first to initialize audio context.');
        return;
      }

      var prof = SPEAKER_PROFILES[this.currentProfile] || SPEAKER_PROFILES['A'];
      var spks = prof.speakers;
      var self = this;
      console.log('[SpatialEngine] Running speaker test for ' + prof.name);

      var idx = 0;
      function playNextChime() {
        if (idx >= spks.length) {
          console.log('[SpatialEngine] Speaker test complete.');
          return;
        }
        var spk = spks[idx];
        self.playTestChimeOnSpeaker(spk, function(){
          idx++;
          setTimeout(playNextChime, 450);
        });
      }
      playNextChime();
    },

    playTestChimeOnSpeaker: function(spk, onDone) {
      if (!this.ctx) return;
      var self = this;
      var osc = this.ctx.createOscillator();
      var gain = this.ctx.createGain();
      
      // Chime frequency: 440 Hz for mains, 80 Hz for Subwoofer
      osc.type = spk.isLFE ? 'sine' : 'triangle';
      osc.frequency.value = spk.isLFE ? 65 : (spk.isHeight ? 880 : 440);

      var now = this.ctx.currentTime;
      gain.gain.setValueAtTime(0.001, now);
      gain.gain.exponentialRampToValueAtTime(0.35, now + 0.05);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);

      osc.connect(gain);

      // Flash speaker indicator on radar
      self.highlightTestingSpeaker(spk.id);

      if (this.mergerNode && spk.ch < (this.ctx.destination.channelCount || 2)) {
        gain.connect(this.ctx.destination);
      } else {
        // Stereo preview balance
        var pan = this.ctx.createStereoPanner ? this.ctx.createStereoPanner() : null;
        if (pan) {
          pan.pan.value = (spk.x < 0) ? -0.8 : ((spk.x > 0) ? 0.8 : 0.0);
          gain.connect(pan);
          pan.connect(this.ctx.destination);
        } else {
          gain.connect(this.ctx.destination);
        }
      }

      osc.start(now);
      osc.stop(now + 0.5);
      setTimeout(onDone, 500);
    },

    highlightTestingSpeaker: function(spkId) {
      this.testingSpeakerId = spkId;
      var self = this;
      setTimeout(function(){
        self.testingSpeakerId = null;
      }, 500);
    },

    // 5. 2D Church Spatial Radar Visualizer
    bindRadarCanvas: function(canvasEl) {
      this.radarCanvas = canvasEl;
      if (!canvasEl) return;
      var self = this;
      
      function renderLoop() {
        self.drawRadar();
        self.radarAnimId = requestAnimationFrame(renderLoop);
      }
      if (this.radarAnimId) cancelAnimationFrame(this.radarAnimId);
      this.radarAnimId = requestAnimationFrame(renderLoop);
    },

    drawRadar: function() {
      var cv = this.radarCanvas;
      if (!cv) return;
      var ctx = cv.getContext('2d');
      var w = cv.width;
      var h = cv.height;
      var cx = w / 2;
      var cy = h / 2;
      var r = Math.min(cx, cy) - 22;

      // Clear dark background
      ctx.fillStyle = '#0f1115';
      ctx.fillRect(0, 0, w, h);

      // Draw Church Architecture Outline
      ctx.strokeStyle = '#222933';
      ctx.lineWidth = 1.5;
      
      // Sanctuary / Altar Apse (Top semicircle)
      ctx.beginPath();
      ctx.arc(cx, cy - r * 0.45, r * 0.45, Math.PI, 2 * Math.PI);
      ctx.stroke();

      // Nave Walls (Central rectangle)
      ctx.strokeRect(cx - r * 0.7, cy - r * 0.45, r * 1.4, r * 1.3);

      // L-Shaped Seating Area Highlight
      ctx.fillStyle = 'rgba(212, 175, 55, 0.06)';
      ctx.strokeStyle = 'rgba(212, 175, 55, 0.22)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      // Shorter leg (East/West) & Longer leg (North/South)
      ctx.rect(cx - r * 0.65, cy + r * 0.35, r * 1.3, r * 0.45);
      ctx.rect(cx + r * 0.35, cy - r * 0.35, r * 0.3, r * 0.7);
      ctx.fill();
      ctx.stroke();

      // Concentric distance rings
      ctx.strokeStyle = 'rgba(255,255,255,0.06)';
      [0.33, 0.66, 1.0].forEach(function(pct){
        ctx.beginPath();
        ctx.arc(cx, cy, r * pct, 0, 2 * Math.PI);
        ctx.stroke();
      });

      // Axis crosshairs
      ctx.strokeStyle = 'rgba(255,255,255,0.08)';
      ctx.beginPath();
      ctx.moveTo(cx, cy - r); ctx.lineTo(cx, cy + r);
      ctx.moveTo(cx - r, cy); ctx.lineTo(cx + r, cy);
      ctx.stroke();

      // Stage & Actor Center Point
      ctx.fillStyle = '#d4af37';
      ctx.beginPath();
      ctx.arc(cx, cy - r * 0.25, 4, 0, 2 * Math.PI);
      ctx.fill();
      ctx.font = '10px sans-serif';
      ctx.fillStyle = '#d4af37';
      ctx.textAlign = 'center';
      ctx.fillText('Sanctuary Altar', cx, cy - r * 0.55);
      ctx.fillStyle = '#888';
      ctx.fillText('Clare / Station', cx, cy - r * 0.15);
      ctx.fillText('Rear Nave (Exit)', cx, cy + r * 0.95);

      // Render Speakers for current profile
      var prof = SPEAKER_PROFILES[this.currentProfile] || SPEAKER_PROFILES['A'];
      var self = this;
      prof.speakers.forEach(function(spk){
        var sx = cx + spk.x * (r * 0.88);
        var sy = cy - spk.y * (r * 0.88);
        var isTesting = (self.testingSpeakerId === spk.id);

        ctx.fillStyle = isTesting ? '#2ecc71' : (spk.isHeight ? '#9b59b6' : (spk.isLFE ? '#e67e22' : '#3498db'));
        ctx.beginPath();
        ctx.arc(sx, sy, isTesting ? 8 : 5, 0, 2 * Math.PI);
        ctx.fill();

        ctx.font = '9px monospace';
        ctx.fillStyle = isTesting ? '#2ecc71' : '#aaa';
        ctx.textAlign = 'center';
        ctx.fillText(spk.id, sx, sy + (spk.y > 0 ? -9 : 14));
      });

      // Render Active Sound Sources (Live Animated Blips)
      if (global.ST) {
        Object.keys(global.ST).forEach(function(sid){
          var s = global.ST[sid];
          if (!s || !s.playing) return;
          var sp = self.sources[sid] || { azimuth: 0, distance: 2.0 };
          var rad = (sp.azimuth * Math.PI) / 180.0;
          var normDist = Math.min(1.0, sp.distance / 50.0);
          var bx = cx + Math.sin(rad) * (r * (0.15 + normDist * 0.8));
          var by = cy - Math.cos(rad) * (r * (0.15 + normDist * 0.8));

          // Blip pulse
          var pulse = (performance.now() % 1000) / 1000;
          ctx.strokeStyle = 'rgba(231, 76, 60, ' + (1.0 - pulse) + ')';
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.arc(bx, by, 5 + pulse * 12, 0, 2 * Math.PI);
          ctx.stroke();

          ctx.fillStyle = '#e74c3c';
          ctx.beginPath();
          ctx.arc(bx, by, 4.5, 0, 2 * Math.PI);
          ctx.fill();

          ctx.font = 'bold 9px sans-serif';
          ctx.fillStyle = '#fff';
          ctx.textAlign = 'center';
          ctx.fillText(sid.replace('SFX-', ''), bx, by - 8);
        });
      }
    }
  };

  global.SpatialEngine = SpatialEngine;
  global.SPEAKER_PROFILES = SPEAKER_PROFILES;

})(typeof window !== 'undefined' ? window : this);
