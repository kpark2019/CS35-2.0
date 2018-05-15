# Authors: Kenneth Park and Jason Jiang

import matplotlib.pyplot as plt
import mindwave, time
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
import peakutils


# 1) Receive data from neuroSet
# 2) Put data into graph format using matplotlib
# 3) Find average and set to zero
# 4) Determine peaks in focus
# 5) Match peaks to segments in music
# 6) Identify characteristics of music - e.g.) volume, genre
# 7) Turn data into numerical values
# 8) Store list in a .csv file
# 9) Use kNN for every feature to figure out best group for study music
# 10) Use Apple iTunes API to pull a cohesive study music playlist.

# Receive data from neuroSet
def graphAnalysis():
    """This function is used to both receive and depict the data into a graph."""
    then = time.time()
    now = time.time()

    plt.axis([-2000, 2000, 0, 50])
    plt.ion()

    # Connect the path and the mindwave's serial number
    neuroSet = mindwave.Headset('COM5', 'CC0E')
    time.sleep(2)

    # Connect the mindwave
    neuroSet.connect()
    print("Currently Pairing Your Headset.")

    while mindwave.status != "Paired!":
        time.sleep(2)
        if mindwave.status == "Standing by.":
            mindwave.connect()
            print("Retrying.")

    print("Paired!")

    # Put data into graph format using matplotlib
    x = True
    while x == True:
        # time.sleep(.5)
        print("Attention: %s" % (neuroSet.attention))
        now = time.time()
        duration = now - then
        duration_sec = duration % 60
        x = str(neuroSet.attention)
        y = str(duration_sec)
        plt.plot(x, y)
        plt.pause(1)

    while True:
        plt.pause(1)

# Find average and set to zero
def getAverageOfGraph(x, y):
    # find the origin aka x-axis line by setting it equal to the average
    xaxis = sum(x) / len(x)

    # Set up temp array and change each value to accomodate
    y2 = y
    for i in range(len(y2)):
        y2[i] = y2[i] - xaxis
    return (x, y2)

# Determine peaks in focus
def findPeaks(xData, yData):
    """We will employ the plotly library and find only the highest peaks"""
    graphData = yData
    cb = np.array(graphData)
    indices = peakutils.indexes(cb, thres=0.678, min_dist=0.1)

    trace = go.Scatter(
        x = xData,
        y = graphData,
        mode = 'lines',
        name = 'Original Plot'
    )

    trace2 = go.Scatter(
        x = indices,
        y = yData,
        mode = 'markers',
        marker = dict(
            size = 8,
            color = 'rgb(255,0,0)',
            symbol = 'cross'
        ),
        name='Detected Peaks'
    )

    data = [trace, trace2]
    py.iplot(data, filename='Graph With Peaks Traced')
    return trace2

# Figure out how much focus.
def durationsOfFocus(graphAveDataX, graphAveDataY):
    topHalfY = graphAveDataY
    for i in range(len(graphAveDataY)):
        if graphAveDataY[i] < 0:
            np.delete(topHalfY, i)

    topQuarterGraph = getAverageOfGraph(graphAveDataX, topHalfY)

    topQuarterY = topQuarterGraph[1]
    topQuarterY2 = topQuarterY
    for i in range(len(topQuarterY)):
        if topQuarterY[i] < 0:
            np.delete(topQuarterY2, i)

    return len(topQuarterY2)

# Identify characteristics of music - e.g.) volume, genre

# Turn data into numerical values
# Store list in a .csv file
# Use kNN for every feature to figure out best group for study music
# Use Apple iTunes API to pull a cohesive study music playlist.