import os.path

print(os.path.abspath('demo13.py'))
print(os.path.exists('demo13.py'), os.path.exists('demo18.py'))

print(os.path.join('../chap15', 'demo13.py'))

print(os.path.split('../chap15/demo13.py'))
print(os.path.splitext('demo13.py'))

print(os.path.basename('../chap15/demo13.py'))
print(os.path.dirname('../chap15/demo13.py'))
print(os.path.isdir('../chap15/demo13.py'))