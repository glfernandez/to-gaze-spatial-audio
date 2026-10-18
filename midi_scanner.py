import mido
import time

PORT_NAME = 'USB2.0-MIDI Port 1'

def scan_midi_capabilities():
    print(f"Opening MIDI output: {PORT_NAME}")
    try:
        with mido.open_output(PORT_NAME) as port:
            print("\n--- PHASE 1: Testing Control Change (Fader) Overrides ---")
            print("If your controller allows digital fader control, the lights should turn red or white now.")
            # We will test MIDI Channel 1 (0 in code) and Channel 16 (15 in code)
            for midi_ch in [0, 15]: 
                # Turn up Fade (CC 8) and Initiate (CC 11)
                port.send(mido.Message('control_change', channel=midi_ch, control=8, value=127))
                port.send(mido.Message('control_change', channel=midi_ch, control=11, value=127))
                
                # Turn up Red (CC 1)
                port.send(mido.Message('control_change', channel=midi_ch, control=1, value=127))
                time.sleep(1)
                
                # Turn off
                port.send(mido.Message('control_change', channel=midi_ch, control=1, value=0))
                port.send(mido.Message('control_change', channel=midi_ch, control=8, value=0))
                port.send(mido.Message('control_change', channel=midi_ch, control=11, value=0))
            
            print("Phase 1 complete. Did the lights turn on without you touching the controller?")
            time.sleep(3)

            print("\n--- PHASE 2: Testing Note Messages (Scene Triggers) ---")
            print("Many controllers use Notes 0-120 to trigger saved scenes.")
            print("Firing Notes 0 through 10... watch the controller screen to see if the 'Scene' or 'Bank' changes.")
            for note in range(0, 10):
                port.send(mido.Message('note_on', channel=0, note=note, velocity=127))
                time.sleep(0.5)
                port.send(mido.Message('note_off', channel=0, note=note, velocity=0))
            
            print("Phase 2 complete.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scan_midi_capabilities()
