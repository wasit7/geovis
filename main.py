import numpy as np
import nrrd

# Some sample numpy data
data = np.zeros((5,4,3,2))
filename = 'testdata.nrrd'

# Write to a NRRD file
nrrd.write(filename, data)

# Read the data back from file
readdata, header = nrrd.read(filename)
print(readdata.shape)
print(header)