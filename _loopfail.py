import os
import sys
import time

if __name__ == '__main__':
    try:
        cmd = ' '.join(sys.argv[1:])
        while 0 != os.system(cmd):
            print("Error, retrying...")
            time.sleep(2)
        print("Done")
    except KeyboardInterrupt:
        exit(-1)
