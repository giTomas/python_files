from os import listdir, getcwd, walk
from os.path import isfile, join, dirname, abspath
import glob

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

dirpath, _, filenames = next(walk(directory))
onlyfiles.extend(filenames)
# onlyfiles = next(walk(directory))[2]

print(onlyfiles)

with open('filelist.txt', 'w') as f:
    f.write('List of files in dir: {}\n\n'.format(dirpath))

    for idx, item in enumerate(onlyfiles, start=1):
        f.write('{}. {}\n'.format(idx, item))

# glob module takes wildcard and returns the full path of files and directories matching the wildcard
onlytxt = glob.glob(directory + '\*.txt')
print(onlytxt)
