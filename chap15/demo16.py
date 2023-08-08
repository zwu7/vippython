import os

print(os.getcwd())
list = os.listdir('../chap15')
print(list)

os.mkdir('newdir')
os.makedirs('A/B/C')

os.rmdir('newdir')
os.removedirs('A/B/C')

os.chdir('../chap15')
print(os.getcwd())
