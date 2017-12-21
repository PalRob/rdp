"""Creates table of contents for Reddit Daily Programmer repository.
Goes throught local files within this repo and finds all files named
"dp_number_difficulty.extension".
"""
import os

local_dir = os.path.dirname(os.path.abspath(__file__))
README_FILE = local_dir + r"\README.md"
#os.path.isfile(README_FILE)