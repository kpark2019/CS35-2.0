#
# hw3pr1.py
#
#  lab problem - matplotlib tutorial (and a bit of numpy besides...)
#
# this asks you to work through the first part of the tutorial at
#     www.labri.fr/perso/nrougier/teaching/matplotlib/
#   + then try the scatter plot, bar plot, and one other kind of "Other plot"
#     from that tutorial -- and create a distinctive variation of each
#
# include screenshots or saved graphics of your variations of those plots with the names
#   + plot_scatter.png, plot_bar.png, and plot_choice.png
#
# Remember to run  %matplotlib  at your ipython prompt!
#

#
# in-class examples...
#

def inclass1():
    """
    Simple demo of a scatter plot.
    """
    import numpy as np
    import matplotlib.pyplot as plt


    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()



#
# First example from the tutorial/walkthrough
#


#
# Feel free to replace this code as you go -- or to comment/uncomment portions of it...
#

def example1():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C,S = np.cos(X), np.sin(X)

    plt.plot(X,C)
    plt.plot(X,S)

    plt.show()






#
# Here is a larger example with many parameters made explicit
#

def example2():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm

    # Create a new figure of size 8x6 points, using 100 dots per inch
    plt.figure(figsize=(8,6), dpi=80)

    # Create a new subplot from a grid of 1x1
    plt.subplot(111)

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    # Plot cosine using blue color with a continuous line of width 1 (pixels)
    plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

    # Plot sine using green color with a continuous line of width 1 (pixels)
    plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

    # Set x limits
    plt.xlim(-4.0,4.0)

    # Set x ticks
    plt.xticks(np.linspace(-4,4,9,endpoint=True))

    # Set y limits
    plt.ylim(-1.0,1.0)

    # Set y ticks
    plt.yticks(np.linspace(-1,1,5,endpoint=True))

    # Save figure using 72 dots per inch
    # savefig("../figures/exercice_2.png",dpi=72)

    # Show result on screen
    plt.show()

def example3():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm

    # Create a new figure of size 8x6 points, using 100 dots per inch
    plt.figure(figsize=(8,6), dpi=80)

    # Create a new subplot from a grid of 1x1
    plt.subplot(111)

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    # Plot cosine using blue color with a continuous line of width 1 (pixels)
    plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

    # Plot sine using green color with a continuous line of width 1 (pixels)
    plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

    # Set x limits
    plt.xlim(-4.0,4.0)

    # Set x ticks
    plt.xticks(np.linspace(-4,4,9,endpoint=True))

    # Set y limits
    plt.ylim(-1.0,1.0)

    # Set y ticks
    plt.yticks(np.linspace(-1,1,5,endpoint=True))

    # Save figure using 72 dots per inch
    # savefig("../figures/exercice_2.png",dpi=72)

    # Alters the size
    plt.figure(figsize=(10,6), dpi=80)

    # Alters the cosine graph to blue and thicker
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")

    # Alters the sin graph to red and thicker
    plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-")

    # Sets the limits to make more space
    plt.xlim(X.min()*1.1, X.max()*1.1)

    # Sets the limits to make more space
    plt.ylim(C.min()*1.1, C.max()*1.1)

    # Shows the pi and pi/2 for sin and cos x
    plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])

    # Shows the pi and pi/2 for sin and cos y
    plt.yticks([-1, 0, +1])

    # Makes the numbers into pi and pi/2
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
    [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    # Makes the numbers into pi and pi/2
    plt.yticks([-1, 0, +1],
    [r'$-1$', r'$0$', r'$+1$'])

    # Makes the "spines" move so that it is centered on xy
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    # Makes a legend showing the cos and sin
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
    plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
    plt.legend(loc='upper left', frameon=False)

    # Annotates the points 2pi/3on both the sin and cos using a point and
    # dotted line
    t = 2*np.pi/3
    plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
    plt.scatter([t,],[np.cos(t),], 50, color ='blue')

    plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
    plt.scatter([t,],[np.sin(t),], 50, color ='red')

    plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    # Makes the tick labels more visible and puts it on the back of a
    # transparent background
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))

    # Shows graph
    plt.show()


def scatterplot():
    import numpy as np
    import matplotlib.pyplot as plt

    n = 1024
    X = np.random.normal(0,4,n)
    Y = np.random.normal(0,4,n)
    T = np.arctan2(X,Y)

    # Makes the side bars maroon
    fig = plt.figure()
    fig.patch.set_facecolor('maroon')

    # Axes
    plt.axes([0.03,0.03,1,1])

    # Changes the markers, size etc.
    plt.scatter(X,Y, s=25, c=T, alpha=1, marker = '*')

    # Connects the markers, legend
    plt.plot(X, Y, color="pink", label="Random Point Connect", linewidth = .1, linestyle = "-")
    plt.legend(loc='upper left')

    # Labels the axis
    plt.xlabel('X AXIIIIIIIIIIIS')
    plt.ylabel('Y AXIIIIIIIIIIIS')

    # Limits
    plt.xlim(-12,12), plt.xticks([])
    plt.ylim(-12,12), plt.yticks([])

    # Show plot
    plt.show()


def barplot():
    import numpy as np
    import matplotlib.pyplot as plt
    n = 12
    X = np.arange(n)
    Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
    Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

    plt.title('Random Bar Graph')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.axes([0.025,0.025,0.95,0.95])
    plt.bar(X, +Y1, facecolor='#FFDB58', edgecolor='#000000')
    plt.bar(X, -Y2, facecolor='#000000', edgecolor='#FFDB58')

    for x,y in zip(X,Y1):
        plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

        for x,y in zip(X,Y2):
            plt.text(x+0.4, -y-0.05, '%.2f' % y, ha='center', va= 'top')

    plt.xlim(-.5,n), plt.xticks([])
    plt.ylim(-1.25,+1.25), plt.yticks([])

    plt.show()

def pieplot():
    import matplotlib.pyplot as plt

    labels = ('Sleep', 'Homework', 'Eat', 'Play')
    sizes = (500,400,200,100)

    plt.pie(sizes, labels= labels)
    plt.title('Routine')
    plt.show()




#
# using style sheets:
#   # be sure to               import matplotlib
#   # list of all of them:     matplotlib.style.available
#   # example of using one:    matplotlib.style.use( 'seaborn-paper' )
#
