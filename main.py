"""
Photoacoustic signal acquisition and analysis.

This script simulates acquisition of photoacoustic signals, performs basic analysis (e.g. peak amplitude and average energy), and saves results to a CSV file.
"""

import math
import csv


def acquire_signal(num_points: int = 1000, frequency: float = 100000.0, decay: float = 0.005):
    """Simulate acquiring a decaying sine wave representing a photoacoustic pulse.

    Args:
        num_points: Number of sample points in the signal.
        frequency: Frequency of the sine wave in Hz.
        decay: Exponential decay factor controlling how quickly the signal dies out.

    Returns:
        Tuple of time samples and signal values.
    """
    t = [i / num_points for i in range(num_points)]
    signal = [math.sin(2 * math.pi * frequency * ti) * math.exp(-decay * ti * num_points) for ti in t]
    return t, signal


def analyze_signal(t, signal):
    """Compute basic metrics from the signal.

    Args:
        t: List of time samples.
        signal: List of signal values.

    Returns:
        A tuple containing the peak amplitude and average energy of the signal.
    """
    peak_amplitude = max(abs(s) for s in signal)
    energy = sum(s * s for s in signal) / len(signal)
    return peak_amplitude, energy


def save_to_csv(filename: str, t, signal):
    """Save the time and signal arrays to a CSV file.

    Args:
        filename: Name of the CSV file to write.
        t: List of time samples.
        signal: List of signal values.
    """
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["time", "signal"])
        for ti, si in zip(t, signal):
            writer.writerow([ti, si])


def main():
    # Acquire a simulated signal
    t, signal = acquire_signal()
    # Analyze the signal
    peak, energy = analyze_signal(t, signal)
    print(f"Peak amplitude: {peak}")
    print(f"Average energy: {energy}")
    # Save the signal to a CSV file
    save_to_csv("signal.csv", t, signal)


if __name__ == "__main__":
    main()
