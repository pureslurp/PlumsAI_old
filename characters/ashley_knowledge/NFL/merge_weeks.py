from os import listdir
from os.path import isfile, join

SEASON = 2024
path = f'characters/ashley_knowledge/NFL/{SEASON}/'

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

with open(f'{path}/combine_weeks.txt', 'w') as outfile:
    for filename in onlyfiles:
        with open(f'{path}{filename}', 'r') as infile:
            outfile.write(infile.read())