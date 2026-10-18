import mido
import time

PORT_NAME = 'USB2.0-MIDI Port 1'

# The mapped channels based on your findings
R_CH = 1
G_CH = 2
B_CH = 3
FADE_CH = 8
STROBE_CH = 9
INITIATE_CH = 11

def set_channel(port, cc, value):
    # Sends a Control Change message (assuming MIDI Channel 1 (0-indexed as 0))
    # If the lights are on different MIDI channels (e.g., Scan 1 = MIDI Ch 1, Scan 2 = MIDI Ch 2), 
    # we would change the 'channel' argument here.
    msg = mido.Message('control_change', channel=0, control=cc, value=value)
    port.send(msg)

def run_custom_sequence():
    print(f"Opening MIDI output: {PORT_NAME}")
    try:
        with mido.open_output(PORT_NAME) as port:
            print("Starting your custom RGB & Strobe sequence in 2 seconds...")
            time.sleep(2)
            
            # Step 1: Initialization
            print("Initializing (Initiate and Fade at 100%)...")
            set_channel(port, INITIATE_CH, 127)  # Initiate on
            set_channel(port, FADE_CH, 127)      # Fade to full brightness
            set_channel(port, STROBE_CH, 0)      # Ensure strobe is off
            time.sleep(1)

            # Step 2: Color Cycle
            colors = [
                ("Red", R_CH), 
                ("Green", G_CH), 
                ("Blue", B_CH)
            ]
            
            for color_name, ch in colors:
                print(f"Fading in {color_name}...")
                # Ensure other colors are off
                for _, other_ch in colors:
                    if other_ch != ch:
                        set_channel(port, other_ch, 0)
                
                # Fade up
                for val in range(0, 128, 8):
                    set_channel(port, ch, val)
                    time.sleep(0.05)
                time.sleep(0.5)

            # Step 3: All colors on (White-ish)
            print("All colors on (White)...")
            set_channel(port, R_CH, 127)
            set_channel(port, G_CH, 127)
            set_channel(port, B_CH, 127)
            time.sleep(1)

            # Step 4: Strobe Test
            print("Activating Strobe...")
            set_channel(port, STROBE_CH, 100)  # Set strobe speed to around 80%
            time.sleep(3)                      # Let it strobe for 3 seconds
            set_channel(port, STROBE_CH, 0)    # Strobe off
            print("Strobe off.")
            time.sleep(1)

            # Step 5: Fade Out
            print("Fading out...")
            for val in range(127, -1, -8):
                set_channel(port, FADE_CH, val)
                time.sleep(0.05)
            
            # Blackout / Reset
            set_channel(port, R_CH, 0)
            set_channel(port, G_CH, 0)
            set_channel(port, B_CH, 0)
            set_channel(port, INITIATE_CH, 0)
            print("Sequence test complete!")

    except Exception as e:
        print(f"Error opening MIDI port: {e}")

if __name__ == "__main__":
    run_custom_sequence()
