import os
import shutil

os.mkdir('metadata')
for dir in os.listdir('.'):
    if os.path.isdir(dir):
        os.mkdir(os.path.join('metadata', dir))
        for file in os.listdir(dir):
            if file.endswith('.json'):
                shutil.move(os.path.join(dir, file), os.path.join('metadata', dir, file))
