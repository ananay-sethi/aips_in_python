# main.py - Entry point for AIPS in Python

import os
from core.calibration import initialize_calibration
from core.imaging import initialize_imaging
from utils.file_utils import setup_directories

def main():
    # Setup environment (similar to DADEVS)
    base_data_dir = os.path.join(os.getcwd(), 'aips_data')
    setup_directories(base_data_dir)

    # Initialize core functionalities
    initialize_calibration()
    initialize_imaging()

    print("AIPS environment initialized successfully.")

if __name__ == "__main__":
    main()