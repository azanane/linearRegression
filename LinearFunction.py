def checkInt(inputStr):

    try: 
        float(inputStr)
    except ValueError:
        return False
    else:
        return True

def linearFunction(theta0, theta1, mileage):

	estimatedPrice = mileage * theta1 + theta0
	return estimatedPrice


def main():
	try:
		mileage = input("Enter a mileage : ")

		if mileage.isdigit() == False:
			print("Mileage must be a positive number")
			return 1
		else:

			with open("datasets/thetaValues.csv", "r") as filin:
				theta0 = filin.readline()
				theta1 = filin.readline()

			if (checkInt(theta0) == False or checkInt(theta1) == False) and theta0 != "" and theta1 != "":
				
				print("Don't modify the theta.csv content, if you did, please reset it to empty and launch the gradient descent programm.")
				return 1

			else:

				if theta0 == "":
					theta0 = 0
				if theta1 == "":
					theta1 = 0

				theta0 = float(theta0)
				theta1 = float(theta1)
				mileage = float(mileage)

				print(theta0, theta1, mileage)
				print("The estimated price for the car is", int(linearFunction(theta0, theta1, mileage)), "euros")
				return 0

	except EOFError:
		print("End of file.")
		return 1

if __name__ == "__main__":
	main()
