# scope-analysis
For studying results of oscilloscope data 

Starting with data from the scope, in files 0xFF00_"+lengthOfWire[k]+"AllWaveforms.csv"

1. `python createFileStartingPoints.py`
This file creates a list of all of the 1's registered by the scope. (Channel 1 > 0.2V). It outputs files  0xFF00_"+lengthOfWire[k]+"_hightolowC1.csv"

2. `python check_chunk_spacing.py`
This file checks the spacing, and picks all of the indices with spacing greater than 10000 (arbitrary decision). It outputs files 0xFF00_"+lengthOfWire[k]+"startChunks.csv". This file is also useful for making histograms of the spacing between spikes. 

3. `python analysisFromStartingPoints.py`
This file saves smaller files from the large scope output, and saves them according to the spacing from the checked chunk spacing in /splitData/"+lengthOfWire[k]+"/". Ideally, each of these files should contain 16 data bits for analysis. It also writes an output file containing decoded values for each saved packet into 0xFF00_"+lengthOfWire[k]+"_decoded_values.csv". This value is decoded into however many # of bits are in the saved files.

Next, it's ok to run several different scripts in any order.

`python check_0xFF00_bits.py` checks to see if the saved data chunks are 0xFF00

`python compare_0xFF00_bits.py ` plots different saved data chunks using dimensionless x-axis (causing overlap)

`python original_time_side_by_side_plots.py ` plots saved data chunks on their original time scale for x-axis.
