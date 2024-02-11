from LinearFunction import linearFunction
from PlotData import plotData

import numpy as np

def checkLine(line):

    splitLine = np.array(line.strip().split(','))

    if splitLine.shape[0] != 2:
        return False
    elif splitLine[0].isdigit() == False or splitLine[1].isdigit() == False:
        return False

    return True

def gradientDescent(trainX, trainY):

    learningRate = 1.0e-3
    m = trainX.shape[0]

    theta0 = 0
    theta1 = 0

    for _ in range(40000):

        total0 = 0
        total1 = 0
        i = 0

        for i in range(m):

            total0 += linearFunction(theta0, theta1, trainX[i]) - trainY[i]
            total1 += (linearFunction(theta0, theta1, trainX[i]) - trainY[i]) * trainX[i]
        

        total0 = total0 / m
        total1 = total1 / m

        theta0 -= learningRate * total0
        theta1 -= learningRate * total1
    
    return theta0, theta1

        


def main():

    with open("datasets/data.csv", "r") as filin:
        
        line = filin.readline()
        indexLine = 0

        saveTrainX = []
        tmpTrainX = []
        tmpTrainY = []
        
        while line != "":

            if indexLine == 0:
                
                indexLine += 1
                
            elif checkLine(line) == False:
                
                print("If you did modify the data.csv file, please do it to the correct format (km,mileage)")
                return 1
            
            else:				
                
                splitLine = np.array(line.strip().split(','))
                
                saveTrainX.append(int(splitLine[0]))
                tmpTrainX.append(int(splitLine[0]) / 10000)
                tmpTrainY.append(int(splitLine[1]) / 10000)

            line = filin.readline()

        trainX = np.array(tmpTrainX)
        trainY = np.array(tmpTrainY)

        if trainX.shape[0] == 0 or trainY.shape[0] == 0:
            print("If you did modify the data.csv file, please do it to the correct format (km,mileage)")
            return 1
    
    theta0, theta1 = gradientDescent(trainX, trainY)
    theta0 = theta0 * 10000


    with open("datasets/thetaValues.csv", "w") as filin:

        filin.write(str(theta0))
        filin.write('\n')
        filin.write(str(theta1))
        
    # Part of the bonus
    plotData(theta0, theta1, saveTrainX)

    return 0

if __name__ == "__main__":
    main()
