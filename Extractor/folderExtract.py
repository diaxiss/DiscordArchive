from os import listdir
from os.path import join, isfile
from discordExtractParser import extractor

mypath = './migrated'

files = []
for dir in listdir(mypath):

    directory_path = join(mypath, dir)
    if not isfile(directory_path):

        for file in listdir(directory_path):
            file_path = join(directory_path, file)
            if isfile(file_path):
                print(file_path)
                extractor(path = file_path)
    else:
        extractor(path = directory_path)