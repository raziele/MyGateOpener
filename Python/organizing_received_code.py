#!/usr/bin/python

import os
import numpy as np

fpath = "/Users/raziele/Downloads/ParkingRCanalysis/parkRC_bytes" #"/home/maayan4/ParkingRC/parkRC_bytes"

MAX_NUM_OF_SIGNALS = 15  #maximum number of signals in a file
SZ_SIGNAL          = 161 #size in bits

with open(fpath,'rb') as f:
    data = f.read()

data_array = np.fromstring(data, dtype='b')

count = 0
num_of_signals = 0

preamble_code = np.array([1,1,1,1,1])

Signals = np.zeros()

for bit in data_array:
    if bit == 1:
        count += 1
    else:
        count = 0
    if count > 4:
        num_of_signals += 1
        count = 0

print(num_of_signals)
