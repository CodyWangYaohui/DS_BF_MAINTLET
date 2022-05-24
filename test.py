import BeamformingBasics as bf
import scipy.io.wavfile as wavfile
import numpy as np 


# create uniform linear array - try to change these values and see what happens!

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# Array length [m]

L = 0.45
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# Number of sensors in array (must be odd!)

M = 3
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
MyULA = bf.SensorArray(L, M)

filename = '../../data/4K_45_16_48000_10s.wav'

sampleRate, data = wavfile.read(filename)
# remove first 20000
front_offset = 48000*5
# extract 0.5S
#get the 0.5s starting at 5s, while extracting the middle 3 channels
data = data[front_offset:front_offset+24000,1:4].T
data = np.flip(data, 0)

# use delay-and-sum beamforming to map direction of arrival

N_theta = 181
theta = np.linspace(0, np.pi, N_theta)

theta0_deg = 135.
N_DoA = int(theta0_deg)

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
## array shading schemes - uncomment one

weights = np.ones(M)
# weights = ss.windows.hann(M)
# weights = ss.windows.chebwin(M, 40)
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
p_array = data
fs = 48e3       # sampling freq [Hz]

y_beamformer = bf.delayandsum_beamformer(MyULA, p_array, theta, weights, fs, c0=1500)

