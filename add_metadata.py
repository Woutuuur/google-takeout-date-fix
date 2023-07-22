import os
from datetime import datetime
import filedate
import json

def find_photo(dir, json):
    filename = '.'.join(json.split('.')[:-1])
    
    if filename.endswith('(1)'):
        filename = filename[:-3]

    if os.path.isfile(os.path.join(dir, filename)):
        return filename
    
    candidates = []

    for other_filename in (x for x in os.listdir(dir) if not x.endswith('.json')):
        extension = '.' + other_filename.split('.')[-1]
        other_filename = '.'.join(other_filename.split('.')[:-1])

        if filename in other_filename:
            candidates.append(other_filename + extension)
    
    if len(candidates) == 1:
        return candidates[0]
    
    if len(candidates) > 1:
        print(f'Multiple candidates for {filename}: {candidates}')
        return None

    return None

def get_creation_date(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
        return datetime.fromtimestamp(int(data['photoTakenTime']['timestamp']))

for dir in os.listdir('.'):
    if os.path.isdir(dir):
        json_filenames = [x for x in os.listdir(dir) if x.endswith('.json') and x != 'metadata.json']
        for json_filename in json_filenames:
            if not (photo_filename := find_photo(dir, json_filename)):
                print(f'Failed for {json_filename} in {dir}')
                exit(0)
            
            media_path = os.path.join(dir, photo_filename)
            
            assert os.path.isfile(media_path)

            print(media_path)
            creation_date = get_creation_date(os.path.join(dir, json_filename))
            media_file = filedate.File(media_path)
            media_file.set(
                created = creation_date.strftime('%Y.%m.%d %H:%M:%S'),
                modified = creation_date.strftime('%Y.%m.%d %H:%M:%S'),
                accessed = media_file.get()['accessed'],
            )
