import matplotlib.pyplot as plt
import pandas as pd
from LinearFunction import linearFunction

def getValuesFromCsv(filename):

    dataFrame = pd.read_csv(filename)    
    
    return ( dataFrame )

def plotData(theta0, theta1, trainX):

    dataFrame = getValuesFromCsv('datasets/data.csv')

    plt.plot(list(range(250000)), [linearFunction(theta0, theta1, x) for x in range(250000)])
    plt.scatter(data=dataFrame, x='km', y='price')

    fig = plt.gcf()
    fig.canvas.manager.set_window_title('Estimated price') # Set the window title

    plt.show()
