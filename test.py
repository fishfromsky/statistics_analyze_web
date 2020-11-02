import os

list = []

for root, dirs, files in os.walk('media\\static\\file'):
    if len(files) != 0:
        for file in files:
            list.extend([os.path.join(root, file)])

for item in list:
    print(os.path.split(item))

