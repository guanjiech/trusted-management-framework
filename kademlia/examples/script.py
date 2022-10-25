import os

def script():
    for i in range(1,6):
        for j in range(1,6):
            os.system("python3 set.py 127.0.0.1 800%s hello test%s" % (j,i))
            os.system("python3 get.py 127.0.0.1 800%s hello" % j)

script()
