aips_python/
│
├── __init__.py              # Initialize the main package
│
├── utils/                   # Utility scripts and helper functions
│   ├── __init__.py          # Initialize utils package
│   ├── file_utils.py        # File I/O handling, like reading UV data, FITS files
│   ├── math_utils.py        # Math functions for FFT, convolution, etc.
│
├── core/                    # Core functionality (equivalent of AIPS tasks)
│   ├── __init__.py          # Initialize core package
│   ├── calibration.py       # Calibration tasks (FRING, etc.)
│   ├── imaging.py           # Imaging tasks (CLEAN, MTMFS, etc.)
│   ├── visualization.py      # Display tasks (TVINI, TVLOD, etc.)
│
└── main.py                  # Entry point to run AIPS-like commands