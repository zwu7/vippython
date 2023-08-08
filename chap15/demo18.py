import os

path = os.getcwd()
lst = os.listdir()

for filename in lst:
    if filename.endswith('.py'):
        print(filename)