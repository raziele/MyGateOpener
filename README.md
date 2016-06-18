# MyGateOpener
My version for a receiver and code extractor of a car garage remote control  

This project was presented to the Software-Defined Radio Israel meetup group on June 2016  

# Contents by directory  

Arduino - an arduino code for a remote control replica based on Arduino Nano and a 433MHz transmitter module.  
          code was compiled and uploaded with PlatformIO  
GRC - The GnuRadio flowgraph used to extract the code  
Python - Python script used to do some more process on the code, including some error correction  
Samples - Contains the sample file used for the process  

# TODO  
Improve error correction. Right now the code still has some errors (e.g too many zeros\ones due to inaccurate clock recovery)

