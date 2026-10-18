import mido
import time

PORTS = ['USB2.0-MIDI Port 1', 'USB2.0-MIDI Port 2']

def full_scan():
    for port_name in PORTS:
        print(f"\n======================================")
        print(f" TESTING PORT: {port_name}")
        print(f"======================================")
        try:
            with mido.open_output(port_name) as port:
                # Test CCs across all 16 MIDI channels
                print("--- Sending Control Change (Fader) signals across ALL MIDI channels ---")
                print("Watch the lights...")
                for midi_ch in range(16):
                    # Set Fade, Initiate, and Red to max
                    port.send(mido.Message('control_change', channel=midi_ch, control=8, value=127))
                    port.send(mido.Message('control_change', channel=midi_ch, control=11, value=127))
                    port.send(mido.Message('control_change', channel=midi_ch, control=1, value=127))
                
                time.sleep(2)
                
                # Turn them off
                for midi_ch in range(16):
                    port.send(mido.Message('control_change', channel=midi_ch, control=8, value=0))
                    port.send(mido.Message('control_change', channel=midi_ch, control=11, value=0))
                    port.send(mido.Message('control_change', channel=midi_ch, control=1, value=0))

                # Test Notes across all 16 MIDI channels
                print("\n--- Sending Note signals (Scene Triggers) across ALL MIDI channels ---")
                print("Please watch the '101' on your DMX controller screen. Does it change numbers?")
                for midi_ch in range(16):
                    for note in range(0, 5):  # Just test first 5 notes to see if screen changes
                        port.send(mido.Message('note_on', channel=midi_ch, note=note, velocity=127))
                        time.sleep(0.1)
                        port.send(mido.Message('note_off', channel=midi_ch, note=note, velocity=0))
                time.sleep(1)
                
        except Exception as e:
            print(f"Could not open port {port_name}: {e}")

if __name__ == "__main__":
    full_scan()
