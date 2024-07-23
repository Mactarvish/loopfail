import os
import sys

if __name__ == '__main__':
    try:
        cmd = ' '.join(sys.argv[1:])
        while 0 != os.system(cmd):
            print("Error, retrying...")
        print("Done")
    except KeyboardInterrupt:
        exit(-1)
