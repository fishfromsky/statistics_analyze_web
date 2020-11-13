import os

for (root, dirs, files) in os.walk('media/static/result/admin/relation'):
    print(root)
    for file in files:
        print(file)