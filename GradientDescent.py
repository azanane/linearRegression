from LinearFunction import linearFunction
from utils import parseData
from PlotData import plotData

def fit(trainX, trainY, epochs, learningRate):

    theta0 = 0
    theta1 = 0

    for _ in range(epochs):
        theta0, theta1 = gradientDescent(trainX, trainY, theta0, theta1, learningRate)

    return theta0, theta1
    

def gradientDescent(trainX, trainY, theta0, theta1, learningRate):

    m = trainX.shape[0]
    total0 = 0
    total1 = 0

    for i in range(m):
        total0 += linearFunction(theta0, theta1, trainX[i]) - trainY[i]
        total1 += (linearFunction(theta0, theta1, trainX[i]) - trainY[i]) * trainX[i]

    total0 = total0 / m
    total1 = total1 / m

    theta0 -= learningRate * total0
    theta1 -= learningRate * total1
    
    return theta0, theta1   


def main():

    trainX, trainY = parseData()
    
    theta0, theta1 = fit(trainX, trainY, 200000, 1.0e-3)
    theta0 = theta0 * 10000

    with open("datasets/thetaValues.csv", "w") as filin:

        filin.write(str(theta0))
        filin.write('\n')
        filin.write(str(theta1))
        
    # Part of the bonus
    plotData(theta0, theta1)

    return 0

if __name__ == "__main__":
    main()
