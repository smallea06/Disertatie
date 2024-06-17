import numpy as np
import pandas as pd
import os
from collections import UserDict

def load_data(data_dir):
    """Load the GEFCom 2014 energy load data"""

    energy = pd.read_csv(os.path.join(data_dir, 'MAC000002.csv'), parse_dates=['tstp'])
    energy = energy.rename(columns={'energy(kWh/hh)': 'load'})


    energy.index = energy['tstp'] # type: ignore
    energy = energy.reindex(pd.date_range(min(energy['tstp']),
                                          max(energy['tstp']),
                                          freq='30min'))
    energy = energy.drop('tstp', axis=1)

    return energy
