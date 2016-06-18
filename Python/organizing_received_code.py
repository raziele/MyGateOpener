#!/usr/bin/python

import os
import numpy as np

fpath = "/home/maayan4/MyReps/MyGateOpener/LiveSession/output_code"

MAX_NUM_OF_SIGNALS = 15  #maximum number of signals in a file
SZ_SIGNAL          = 161 #size in bits

np.set_printoptions(threshold=np.nan)

with open(fpath,'rb') as f:
    data = f.read()

data_array = np.fromstring(data, dtype='b')

count = 0
num_of_signals = 0

preamble_code = np.array([1,1,1,1,1])

signals = np.zeros((MAX_NUM_OF_SIGNALS,SZ_SIGNAL),bytes)

for idx, bit in enumerate(data_array):
    if (data_array.size - idx) < SZ_SIGNAL:
        break
    if (data_array[idx:idx+5] == preamble_code).all():
        signals[num_of_signals,:] = data_array[idx:idx+SZ_SIGNAL]
        num_of_signals += 1

print(num_of_signals)
signals = signals[0:num_of_signals,:]

decrypted_signal = np.zeros((1,SZ_SIGNAL),bytes)

for x in range(0,signals.shape[1]):
    candidates = signals[:,x]
    zero_count = candidates[candidates == '0'].size
    one_count = candidates[candidates == '1'].size
    if zero_count > one_count: decrypted_signal[0,x] = '0'
    elif one_count > zero_count: decrypted_signal[0,x] = '1'
    else: decrypted_signal[0,x] = '0' #just because I can

print(decrypted_signal)

print(decrypted_signal[0,5:decrypted_signal.size].reshape((52,3)))
