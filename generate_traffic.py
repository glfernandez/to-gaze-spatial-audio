import torch
from diffusers import AudioLDMPipeline
import scipy.io.wavfile
import os

# Initialize pipeline
print("Loading AudioLDM model...")
# Using the small model to save download time and memory
repo_id = "cvssp/audioldm-s-full-v2"
pipe = AudioLDMPipeline.from_pretrained(repo_id, torch_dtype=torch.float32)

# Move to mps if available (Mac Silicon)
device = "mps" if torch.backends.mps.is_available() else "cpu"
pipe = pipe.to(device)

def generate_sfx(prompt, filename_prefix, num_variants=2):
    print(f"\nGenerating '{prompt}'...")
    for i in range(num_variants):
        # Generate with a different seed each time for variation
        generator = torch.Generator(device).manual_seed(42 + i)
        audio = pipe(
            prompt, 
            num_inference_steps=20, 
            audio_length_in_s=5.0, 
            generator=generator
        ).audios[0]
        
        # Save as 48kHz (AudioLDM generates at 16kHz typically, we resample/save)
        # Note: AudioLDM output is typically float32 numpy array.
        filename = f"{filename_prefix}_v{i+1:02d}_RAW.wav"
        scipy.io.wavfile.write(filename, 16000, audio)
        print(f"Saved {filename}")

# Generate Traffic (SFX-03)
prompt_traffic = "Dense contemporary urban traffic from street level, realistic field recording, distant engines, tyre movement, occasional horns, dry recording, no music, no voices"
generate_sfx(prompt_traffic, "SFX/P1_WORLD/traffic/SFX-03_TRAFFIC_CITYBED_GEN")

# Generate Emergency (SFX-05)
prompt_emergency = "Distant urban ambulance siren approaching and receding through city traffic, realistic field recording, no music"
generate_sfx(prompt_emergency, "SFX/P1_WORLD/emergency/SFX-05_AMBULANCE_EMERGENCY_GEN")

print("\nGeneration complete!")
