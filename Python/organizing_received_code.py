#!/usr/bin/python

import os
import numpy as np

fpath = "/home/maayan4/ParkingRC/parkRC_bytes"

with open(fpath,'rb') as f:
    data = f.read()

data_array = np.fromstring(data, dtype='b')

count = 0
num_of_signals = 0

for bit in data_array:
    if bit == 1:
        count += 1
    else:
        count = 0
    if count > 4:
        num_of_signals += 1
        count = 0

print(num_of_signals)
