# Connect to Mindwave to computer first
# Call neuropy.start() to get data.
# Neuropy.stop() to stop
from NeuroPy import NeuroPy
import numpy as np
import matplotlib.pyplot as plt
import mindwave, time

neuropy = NeuroPy() 
neuropy.start()

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

# Raw data of the attention
while True:
    print "Attention: %s" % (headset.attention)
neuropy.stop()

#the graph of mindwave attention
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
