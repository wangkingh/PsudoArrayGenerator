import numpy as np


# Generate random noise
def generate_random(points: int) -> np.ndarray:
    return np.random.uniform(-1, 1, size=points).astype(np.float32)


# Generate noise from spectrum
def generate_from_spectrum(amplitude_spectrum: np.ndarray, points: int,
                           phase_perturbation_factor: float = 0.1) -> np.ndarray:
    # Generating random phase perturbation
    random_phases = np.exp(
        1j * np.random.uniform(-phase_perturbation_factor, phase_perturbation_factor, len(amplitude_spectrum)))
    perturbed_spectrum = amplitude_spectrum * random_phases

    # Using the I FFT signal
    signal = np.fft.ifft(perturbed_spectrum).real

    # if signal is longer, truncated it
    if len(signal) > points:
        signal = signal[:points]

    # if signal is shorter, pad it with 5% level of noise
    elif len(signal) < points:
        padding = np.random.uniform(-0.5, 0.5, size=points - len(signal))
        signal = np.concatenate((signal, padding))

    return signal.astype(np.float32)
