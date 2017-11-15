import re
import json
# fileref = open("qbdata.txt",'r')
#
# for line in fileref:
#     print(line)
#
# fileref.close()


with open('key.txt') as file:
    str = file.readline()
    keys = [x.strip() for x in str.split(',')]

# print(keys)


with open('qbdata.txt') as f:
    data = []
    for line in f:

        # line = line.replace('\s+',  ' ')
        # remove duplicate whitespace
        line = " ".join(line.split())
        # values = [x.strip() for x in line.split(' ')]
        values = [x for x in line.split(' ')]
        # values = [x.strip() for x in re.split('\s', line)]
        # print(values)
        item = {}
        for key, value in zip( keys, values):
            print('{}: {}'.format(key, value))

            item[key] = value
        print('\n')
        data.append(item)

print(data[0])
print(data[1])

json_file = json.dumps(data)
print(json.loads(json_file)[0])
