import re
import json

def getObjFromTxt(txtfile):
    with open(txtfile, 'r') as file:
        first_line = file.readline()
        keys = [x.strip() for x in first_line.split(',')]

        data = list()
        for next_line in file:
            # line = line.replace('\s+',  ' ')

            # remove duplicate whitespace
            next_line = " ".join(next_line.split())
            # values = [x.strip() for x in line.split(' ')]
            values = [x for x in next_line.split(' ')]
            # values = [x.strip() for x in re.split('\s', line)]
            # print(values)
            item = dict()
            for key, value in zip(keys, values):
                # print('{}: {}'.format(key, value))

                item[key] = value
            # print('\n')
            data.append(item)

    # print(data[0])
    # print(data[1])
    return data

data = getObjFromTxt('keyvalues.txt')
json_file = json.dumps(data)
print(json.loads(json_file)[0])
