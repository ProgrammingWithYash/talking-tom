from time import sleep
import sounddevice as sd
from scipy.io.wavfile import write

from pydub import AudioSegment
from pydub.playback import play

from playsound import playsound


fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
print('Recording')
sd.wait()  # Wait until recording is finished
print('Done')
write('output.wav', fs, myrecording)  # Save as WAV file

sleep(1)

sound = AudioSegment.from_file('output.wav', format="wav")

# shift the pitch up by half an octave (speed will increase proportionally)
octaves = 0.3

new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

# keep the same samples but tell the computer they ought to be played at the 
# new, higher sample rate. This file sounds like a chipmunk but has a weird sample rate.
hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

# now we just convert it to a common sample rate (44.1k - standard audio CD) to 
# make sure it works in regular audio players. Other than potentially losing audio quality (if
# you set it too low - 44.1k is plenty) this should now noticeable change how the audio sounds.
hipitch_sound = hipitch_sound.set_frame_rate(44100)

#Play pitch changed sound

#export / save pitch changed sound
hipitch_sound.export("output_pitch.wav", format="wav")

playsound('output_pitch.wav')
