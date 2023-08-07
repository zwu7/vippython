scr_file = open('logo.png', 'rb')

target_file = open('copylogo.png', 'wb')

target_file.write(scr_file.read())

target_file.close()
scr_file.close()
