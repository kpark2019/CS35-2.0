# Connect to Mindwave, then run to get data
import numpy as np
import matplotlib.pyplot as plt
import mindwave, time


then = time.time()
now = time.time()


plt.axis([-2000, 2000, 0, 50])
plt.ion()

#connects the path(usb) and the specific serial number of your mindwave
headset = mindwave.Headset('COM5', 'CC0E')
time.sleep(2)

#connecting the mindwave
headset.connect()
print ("Pairing...")

while mindwave.status != "Paired!":
    time.sleep(2)
    if mindwave.status == "Standing by...":
        mindwave.connect()
        print ("Retrying...")
print ("Paired!")

#the graph of mindwave
while True:
    #time.sleep(.5)
    print "Attention: %s" % (headset.attention)
    now = time.time()
    duration = now - then
    duration_sec = duration % 60
    x = str(headset.attention)
    y = str(duration_sec)
    plt.plot(x, y)
    plt.pause(1)



while True:
    plt.pause(1)
