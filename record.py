import sounddevice as sd
import soundfile as sf

# Set the desired sample rate and duration of the recording
sample_rate = 44100  # Standard sample rate for most audio devices
duration = 90  # Recording duration in seconds

# Start the recording from the virtual audio cable device
print("Recording audio from the browser...")
recording = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=2, dtype='float32')

# Wait for the recording to complete
sd.wait()

# Get the desired filename for the recording
filename = input("Enter the filename to save the recording (without extension): ")

# Save the recording as a WAV file
sf.write(filename + ".wav", recording, sample_rate)

print("Audio recording saved as", filename + ".wav")
