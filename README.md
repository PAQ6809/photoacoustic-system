# Photoacoustic System

This repository contains a Python-based photoacoustic signal acquisition and analysis system. It provides basic code and examples for generating synthetic photoacoustic signals, performing simple analyses, and saving results. The goal is to provide a foundation for developing a complete photoacoustic data processing pipeline.

## Features

- Generate synthetic photoacoustic signals for testing.
- Compute peak amplitude and average energy.
- Save the processed data to CSV files.
- Modular functions to enable easy extension.

## Requirements

- Python 3.8+
- No external dependencies (uses only built-in `math` and `csv` modules).

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/PAQ6809/photoacoustic-system.git
   cd photoacoustic-system
   ```
2. Run the example script:
   ```bash
   python3 main.py
   ```
   This will generate a synthetic signal, compute basic metrics, and save the output to `output.csv`.

3. Modify `main.py` to read real photoacoustic sensor data and extend the analysis pipeline.

## Future Work

- Implement signal filtering and noise reduction.
- Integrate with hardware for real-time data acquisition.
- Add visualization of signals and metrics.
- Provide more advanced analyses (e.g., frequency domain analysis, envelope detection).
