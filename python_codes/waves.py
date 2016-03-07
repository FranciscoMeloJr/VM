import wave, random, struct

import numpy as np
from scipy.io.wavfile import write

data = np.random.uniform(-10,10,44100) # 44100 random samples between -1 and 1

print data
scaled = np.int16(data/np.max(np.abs(data)) * 32767)

print scaled

write('test.wav', 44100, scaled)

print 'fim'
