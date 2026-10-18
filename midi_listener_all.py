import mido
import time

def listen_all_ports(duration=60):
    inputs = mido.get_input_names()
    print(f"Available inputs: {inputs}")
    ports = []
    
    for name in inputs:
        try:
            p = mido.open_input(name)
            ports.append((name, p))
            print(f"Listening on {name}...")
        except Exception as e:
            print(f"Could not open {name}: {e}")

    print(f"\n>>> PLEASE MOVE YOUR FADERS AND PRESS BUTTONS NOW (Listening for {duration} seconds) <<<\n")
    
    start_time = time.time()
    while time.time() - start_time < duration:
        for name, p in ports:
            for msg in p.iter_pending():
                print(f"[{name}] Received: {msg}")
        time.sleep(0.1)
        
    print("\nFinished listening.")
    for name, p in ports:
        p.close()

if __name__ == "__main__":
    listen_all_ports()
