import librosa
import os
from monophonic import wave_to_midi 

print("Starting...")
file_in = "Test/Tum Hi Ho.mp3"
file_out = os.path.splitext("Data/"+file_in.replace('Test/',''))[0] + '_cov.mid'
y, sr = librosa.load(file_in, sr=None)
print("Audio file loaded!")
midi = wave_to_midi(y)
print("Conversion finished!")
with open (file_out, 'wb') as f:
    midi.writeFile(f)
print("Done. Exiting!")