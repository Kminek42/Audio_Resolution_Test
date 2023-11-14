import numpy as np

def show_usage():
    print("""--------------------------------------------------------------------------------
Usage:
    main.py waveform frequency duration
          
Arguments:
    waveform:
        Waveform of generated signal [SINE, SAWTOOTH, TRIANGLE, SQUARE]
    
    frequency:
        Main frequency of generated signal [1.0Hz - 10.0kHz]
          
    duration:
        Duration of generated signal [0.1s - 10.0s]
          
Example:
    python3 main.py SAWTOOTH 100.5 4.2
--------------------------------------------------------------------------------""")
    
def normlize(x):
    x -= min(x)
    x /= max(x)
    x *= 1.8
    x -= 0.9

    return x


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def check_arguments(arguments):
    if len(arguments) != 4:
        show_usage()
        return False

    if not is_number(arguments[2]):
        show_usage()
        print(f"ERROR: {arguments[2]} (frequency) is not a number")
        return False
    
    if not is_number(arguments[3]):
        show_usage()
        print(f"ERROR: {arguments[3]} (duration) is not a number")
        return False
    
    if not arguments[1] in ["SINE", "SAWTOOTH", "TRIANGLE", "SQUARE"]:
        show_usage()
        print(f"ERROR: {arguments[1]} (duration) is not a waveform")
        return False

    return True


def generate_signal(waveform, frequency, duration, sample_rate = 48000):
    x = np.arange(0, duration, 1 / sample_rate)
    output = np.zeros(x.shape)

    if waveform == "SAWTOOTH":
        for k in range(1, int(sample_rate / frequency / 2)):
            output += np.sin(2 * np.pi * frequency * k * x) / k
    
    elif waveform == "SINE":
        output = np.sin(2 * np.pi * frequency * x)
    
    elif waveform == "SQUARE":
        for k in range(1, int(sample_rate / frequency / 2)):
            if k % 2:
                output += np.sin(2 * np.pi * frequency * k * x) / k

    return x, normlize(output)


def DAC(samples, dithering = False, resolution=16):
    resolution -= 1
    samples = np.floor(samples * 2 ** resolution) / 2 ** resolution

    return samples