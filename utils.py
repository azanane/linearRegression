import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def checkFloat(inputStr):

    try: 
        float(inputStr)
    except ValueError:
        return False
    else:
        return True

def checkLine(line):

    splitLine = np.array(line.strip().split(','))

    if splitLine.shape[0] != 2:
        return False
    elif splitLine[0].isdigit() == False or splitLine[1].isdigit() == False:
        return False

    return True


def parseData():
    
   with open("datasets/data.csv", "r") as filin:
        
    line = filin.readline()
    indexLine = 0

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
            
            tmpTrainX.append(int(splitLine[0]) / 10000)
            tmpTrainY.append(int(splitLine[1]) / 10000)

        line = filin.readline()

    trainX = np.array(tmpTrainX)
    trainY = np.array(tmpTrainY)

    if trainX.shape[0] == 0 or trainY.shape[0] == 0:
        print("If you did modify the data.csv file, please do it to the correct format (km,mileage)")
        exit(1)

    return trainX, trainY


def parseThetas():

    with open("datasets/thetaValues.csv", "r") as filin:
        theta0 = filin.readline()
        theta1 = filin.readline()

    if (checkFloat(theta0) == False or checkFloat(theta1) == False) and theta0 != "" and theta1 != "":
        
        print("Don't modify the theta.csv content, if you did, please reset it to empty and launch the gradient descent programm.")
        exit(1)
    
    return theta0, theta1
