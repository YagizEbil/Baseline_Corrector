# Baseline Corrector

## Project Overview

Baseline Corrector is a lightweight command-line toolkit for inspecting and cleaning Raman spectra and similar one-dimensional signals. It streamlines loading raw intensity data, applying baseline removal with proven algorithms, and visualizing the normalized output to accelerate spectral analysis workflows.

## Features

- **Interactive Input System**: Detects data files automatically or accepts custom paths, now with support for `.csv`, `.txt`, `.xlsx`, and `.xy` formats.
- **Baseline Correction**: Combines pybaselines' Modified Polynomial method with the arPLS algorithm for resilient background removal.
- **Signal Conditioning**: Offers moving-average smoothing, min-max normalization, and configurable wavenumber thresholding.
- **Visualization**: Generates normalized spectra plots with Matplotlib for rapid inspection.
- **Configurable Settings**: Persists thresholds and toggles via a simple JSON-backed settings menu.

## Repository Structure

```
Baseline_Corrector/
├── arPLS.py               # Standalone arPLS baseline removal implementation
├── baseline-settings.json # Persisted CLI configuration values
├── doc/                   # Sample input files for quick testing
├── input_system.py        # Question/answer helpers for the interactive CLI
├── main.py                # Program entry point and plotting workflow
├── process_data.py        # Utility functions for smoothing and normalization
├── read_data.py           # Multi-format data loader (csv, txt, xlsx, xy)
├── README.md              # Explains how to use the repository
├── requirements.txt       # Python dependencies for the toolkit
└── settings.py            # Settings manager for threshold configuration
```

## How to Run

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/YagizEbil/Baseline_Corrector.git
   cd Baseline_Corrector
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the CLI**  
   ```bash
   python main.py
   ```
   Choose a detected dataset or provide a custom path to load your spectral data. Adjust threshold settings as needed and visualize the corrected spectrum.

4. **Review Output**  
   Plots open in a Matplotlib window for quick inspection. Use the settings menu to tweak threshold ranges and rerun baseline correction without restarting the application.

## Authors

- [Can Badem](https://github.com/canbadem)
- [Kadir Yağız Ebil](https://github.com/YagizEbil)

## License

This project is distributed under the MIT License.
