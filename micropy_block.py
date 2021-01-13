import time
import urandom


for x in range (0,10000000000):
    b = urandom.getrandbits(2) * x
    print (b, end="\r")
    time.sleep(1)