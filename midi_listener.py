import mido
import time

PORT_NAME = 'USB2.0-MIDI Port 1'  # Update if it needs to be different

def listen_to_midi(duration=20):
    print(f"Opening MIDI input: {PORT_NAME}")
    try:
        with mido.open_input(PORT_NAME) as port:
            print(f"Listening for MIDI messages for {duration} seconds...")
            print("Please move the controls on your DMX controller now.")
            
            start_time = time.time()
            while time.time() - start_time < duration:
                for msg in port.iter_pending():
                    print(f"Received: {msg}")
                time.sleep(0.1)
                
            print("Finished listening.")
    except Exception as e:
        print(f"Error opening MIDI port: {e}")

if __name__ == "__main__":
    listen_to_midi()
