import mido
import time

# You may need to change this between 'USB2.0-MIDI Port 1' and 'USB2.0-MIDI Port 2'
PORT_NAME = 'USB2.0-MIDI Port 1'

def run_sequence_test():
    print(f"Opening MIDI output: {PORT_NAME}")
    try:
        with mido.open_output(PORT_NAME) as port:
            print("Starting sequence test in 3 seconds...")
            time.sleep(3)
            
            print("--- Testing Note On messages (often used to trigger scenes) ---")
            for note in [0, 1, 2, 3]:  # Testing first few notes
                print(f"Sending Note On: {note}")
                port.send(mido.Message('note_on', note=note, velocity=127))
                time.sleep(1)
                port.send(mido.Message('note_off', note=note, velocity=0))
                time.sleep(0.5)

            print("--- Testing Control Change messages (often used for faders/channels) ---")
            for cc in [1, 2, 3, 4, 5, 6]:  # Testing first few CC channels
                print(f"Sweeping CC {cc} (Values 0 -> 127 -> 0)")
                
                # Sweep up
                for val in range(0, 128, 16):
                    port.send(mido.Message('control_change', control=cc, value=val))
                    time.sleep(0.1)
                
                # Sweep down
                for val in range(127, -1, -16):
                    port.send(mido.Message('control_change', control=cc, value=val))
                    time.sleep(0.1)
                    
                # Ensure it's off
                port.send(mido.Message('control_change', control=cc, value=0))
                time.sleep(0.5)
                
            print("Sequence test complete. Did the profile lights respond?")
    except Exception as e:
        print(f"Error opening MIDI port: {e}")

if __name__ == "__main__":
    run_sequence_test()
