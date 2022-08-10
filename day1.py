import os
directory = os.getcwd()
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

#checking for file and also id the file is empty

    if os.path.isfile(f) and os.stat(f).st_size == 0:
        print("deleting the empty file: ", f)

#removing the files if found.

        os.remove(f)
        break
    else:
        print("no empty files are there.")
