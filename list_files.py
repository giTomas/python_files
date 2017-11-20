from os import listdir, getcwd, walk
from os.path import isfile, join, dirname, abspath

# get directory where script is executed
directory = dirname(abspath(__file__))
print(directory)

# get current working directory
cwddir = getcwd()

print(cwddir == directory)

# get list of files in directory
onlyfiles =  [f for f in listdir(directory) if isfile(join(directory, f))]

print(onlyfiles)

# os.walk #1
onlyfiles = []
# dirpath, dirnames, filenames
for (_, _, filenames) in walk(directory):
    onlyfiles.extend(filenames)
    break

print(onlyfiles)

# os.walk #1
onlyfiles = []

_, _, filenames = next(walk(directory))
onlyfiles.extend(filenames)

print(onlyfiles)

with open('filelist.txt', 'w') as f:
    for item in onlyfiles:
        f.write('{}\n'.format(item))
