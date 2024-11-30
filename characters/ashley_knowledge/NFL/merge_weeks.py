from os import listdir
from os.path import isfile, join

SEASON = 2024
path = f'characters/ashley_knowledge/NFL/{SEASON}/'

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
count = len(onlyfiles)
week_files = [f"Week{f}.txt" for f in range(1,count)]

with open(f'{path}/combine_weeks.txt', 'w') as outfile:
    for filename in week_files:
        with open(f'{path}{filename}', 'r') as infile:
            outfile.write(infile.read())