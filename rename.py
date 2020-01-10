
# this script below walks through all subdirectories and will look for only tifs
# still need something to confirm or be a little more careful
# need to test that the script runs in a given dir as opposed to where the script lives
# need to figure out best way to tell it to run in a given dir, shebang or keyword arg?
import os

def main():
    path = os.getcwd()
    count = 1

    for root, dirs, files in os.walk(path):
        for file in files:
            if '.tif' in file:
                if 'Pos' in file:
                    name_split = file.split('_')
                    xpos = name_split[-2][-3:]
                    ypos = name_split[-1][:3]

                    new_name = 'x' + xpos + '_y' + ypos + '.tif'

                    src = os.path.join(root, file)
                    dst = os.path.join(root, new_name)

                    os.rename(src, dst)

if __name__ == '__main__':
    main()
