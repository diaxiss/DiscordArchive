import json
from os import listdir
from os.path import join, isfile

mypath = ''

total_file_size_bytes = 0

for dir in listdir(mypath):

    directory_path = join(mypath, dir)
    if isfile(directory_path):

        with open(directory_path, 'r') as input:
            data = json.load(input)
        
        for entry in data['messages']:
            if entry['attachments']:
                for attachment in entry['attachments']:
                    total_file_size_bytes += attachment['fileSizeBytes']

print(f'{round(total_file_size_bytes/(1024**3), 2)}GB')