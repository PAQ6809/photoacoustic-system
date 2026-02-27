"""
A simple demonstration script for estimating tissue oxygen saturation (sO₂) from
photoacoustic signal amplitudes measured at two wavelengths. The method
implemented here uses a basic ratio‐of‐ratios approach: the ratio of
photoacoustic amplitudes at two wavelengths is linearly mapped to an oxygen
saturation estimate between 0 and 1.

This script reads amplitude values from two CSV files (one for each
wavelength), computes the ratio for each sample, converts it into an sO₂
estimate, clamps the result between 0 and 1, and writes the estimated
saturation values to a new CSV file. You can adjust the calibration
parameters `r_min` and `r_max` to reflect the minimum and maximum expected
ratio values for deoxygenated and fully oxygenated tissue, respectively.

Note: This example serves as a teaching tool and starting point for
implementing more sophisticated algorithms. In real systems, calibration
should be performed using reference phantoms or blood samples to determine
appropriate mapping parameters.
"""

import csv
from typing import List


def read_pa_amplitudes(file_path: str) -> List[float]:
    """Read photoacoustic amplitudes from a CSV file.

    Each line of the file should contain a single numeric value. Non-numeric
    values or empty lines are ignored.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A list of floating‑point amplitude values.
    """
    amplitudes: List[float] = []
    with open(file_path, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            try:
                amplitudes.append(float(row[0]))
            except ValueError:
                # Skip lines that cannot be converted to float
                continue
    return amplitudes


def estimate_so2(
    pa1: List[float], pa2: List[float], r_min: float = 0.4, r_max: float = 1.2
) -> List[float]:
    """Estimate oxygen saturation (sO₂) using the ratio‑of‑ratios method.

    Args:
        pa1: Photoacoustic amplitudes at wavelength 1.
        pa2: Photoacoustic amplitudes at wavelength 2.
        r_min: Ratio corresponding to 0% oxygenation. Defaults to 0.4.
        r_max: Ratio corresponding to 100% oxygenation. Defaults to 1.2.

    Returns:
        A list of sO₂ estimates between 0 and 1 for each pair of amplitudes.
    """
    ratios: List[float] = []
    for a1, a2 in zip(pa1, pa2):
        # Avoid division by zero by skipping pairs with zero second amplitude
        if a2 != 0:
            ratios.append(a1 / a2)
    # Map ratios to saturation; clamp to [0, 1]
    so2: List[float] = []
    for r in ratios:
        s = (r - r_min) / (r_max - r_min)
        s = max(0.0, min(1.0, s))
        so2.append(s)
    return so2


def write_estimates(estimates: List[float], file_path: str) -> None:
    """Write a list of saturation estimates to a CSV file.

    Args:
        estimates: List of saturation values between 0 and 1.
        file_path: Output CSV file path.
    """
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        for s in estimates:
            writer.writerow([s])


def main() -> None:
    """Example usage of the estimation functions.

    Replace 'data_wavelength1.csv' and 'data_wavelength2.csv' with your own
    measurement files. Each file should contain one amplitude per line.
    """
    pa_wl1 = read_pa_amplitudes("data_wavelength1.csv")
    pa_wl2 = read_pa_amplitudes("data_wavelength2.csv")
    so2 = estimate_so2(pa_wl1, pa_wl2)
    write_estimates(so2, "estimated_so2.csv")
    print(f"Estimated sO₂ values for {len(so2)} points written to 'estimated_so2.csv'.")


if __name__ == "__main__":
    main()
