from scipy.io.wavfile import write
import sys
import matplotlib.pyplot as plt

import functions


if not functions.check_arguments(sys.argv):
    exit(1)


waveform = sys.argv[1]
frequency = float(sys.argv[2])
duration = float(sys.argv[3])
x, y = functions.generate_signal("SINE", 100, 0.1)
plt.plot(x, functions.DAC(y, resolution=4))
plt.show()

