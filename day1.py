# import required module
import os
# assign directory
directory = os.getcwd()

# iterate over files in
# that directory
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	# checking if it is a file and its empty
	if os.path.isfile(f) and os.stat(f).st_size == 0:
		os.remove(f)