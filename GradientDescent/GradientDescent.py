# adding LinearFunction.py to the system path
import sys
sys.path.append('../LinearFunction')
from LinearFunction import linearFunction, checkInt

import numpy as np

def checkLine(line):

	splitLine = np.array(line.strip().split(','))

	if splitLine.shape[0] != 2:
		return False
	elif splitLine[0].isdigit() == False or splitLine[1].isdigit() == False:
		return False

	return True

def gradientDescent(trainX, trainY, theta0, theta1):

	learningRate = 1.0e-5
	m = trainX.shape[0]

	for n in range(10000):

		total0 = 0
		total1 = 0
		i = 0

		for i in range(m):
		
			total0 += (linearFunction(theta0, theta1, trainX[i]) - trainY[i])
			total1 += ((linearFunction(theta0, theta1, trainX[i]) - trainY[i]) * trainX[i])

		if total0 == 0 and total1 == 0:
			break

		total0 = total0 / m
		total1 = total1 / m 


		theta0 = theta0 - learningRate * total0
		theta1 = theta1 - learningRate * total1

		


def main():

	with open("../data.csv", "r") as filin:
		
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
		
				tmpTrainX.append(int(splitLine[0]) / 1000)
				tmpTrainY.append(int(splitLine[1]) / 1000)

			line = filin.readline()

	
		trainX = np.array(tmpTrainX)
		trainY = np.array(tmpTrainY)

		if trainX.shape[0] == 0 or trainY.shape[0] == 0:
			print("If you did modify the data.csv file, please do it to the correct format (km,mileage)")
			return 1
	
	gradientDescent(trainX, trainY, 0, 0)

	return 0

if __name__ == "__main__":
	main()
