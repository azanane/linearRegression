from utils import parseThetas, parseData
from LinearFunction import linearFunction

def calcCost():

    theta0, theta1 = parseThetas()
    trainX, trainY = parseData()
    
    if theta0 == '' or theta1 == '':
        print("Thetas values ar not defined yet, launch the Gradient Descent programm before.")
        return 1

    m = trainX.shape[0]
    total = 0

    for i in range(m):
        x = trainX[i]
        y = trainY[i]
        algoPrediction = linearFunction(float(theta0) / 10000, float(theta1), x)
        total += (algoPrediction - y) ** 2

    cost = (1 / (2 * m)) * total

    print("Cost of the algorithm : ", cost)
    return 0

if __name__ == "__main__":
	calcCost()
