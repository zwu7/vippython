with open('logo.png', 'rb') as scr_file:
    with open('copy2logo.png', 'wb') as target_file:
        target_file.write(scr_file.read())