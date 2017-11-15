with open('qbdata.txt', 'r') as infile, open('qbnames.txt', 'w') as outfile:
    aline = infile.readline()

    while aline:
        items = aline.split()
        dataline = '{} {}'.format(items[1], items[0])
        outfile.write(dataline + '\n')
        aline = infile.readline()
