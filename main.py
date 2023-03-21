# This is a sample Python script.

# libraries

import numpy as np
import pandas as pd

# settings
pd.set_option('display.max_columns', 10)

# Read in Transcripts
trans = pd.read_csv("/Users/gregduckworth/Documents/Budget_Calculator/Transaction-History.csv", sep = ";")

# Sort the date object out:
pd.to_datetime(trans['Transaction Date'])
