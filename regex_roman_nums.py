import re

s1 = '100 NORTH MAIN ROAD'
s2 = '100 NORTH BROAD ROAD'
s3 = '100 NORTH BROAD'

# sometimes replace is enought
s = s1.replace('ROAD', 'RD')
print(s)

#sometimes NOT
s = s2.replace('ROAD', 'RD')
print(s)

s = re.sub('ROAD$', 'RD.', s2)
print(s)

#but sometimes it's not enought
s = re.sub('ROAD$', 'RD.', s3)
print(s)

# add \b -> start of the word mus be escaped? probably not
s = re.sub('\\bROAD$', 'RD.', s3)
print(s)

# but ad r'' -> raw string
s = re.sub(r'\bROAD$', 'RD.', s3)
print(s)

# but road not on the end of string
s4 = '100 BROAD ROAD APT. 3'
s = re.sub(r'\bROAD$', 'RD.', s4)
print(s)

# remove $ adn ad \b for another word boundary
s = re.sub(r'\bROAD\b', 'RD.', s4)
print(s)
