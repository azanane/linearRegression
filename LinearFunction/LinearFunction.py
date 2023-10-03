def checkInt(inputStr):

    try: 
        int(inputStr)
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

			with open("../thetaValues.csv", "r") as filin:
				theta0 = filin.readline()
				theta1 = filin.readline()

			if (checkInt(theta0) == False or checkInt(theta1) == False) and theta0 != "" and theta1 != "":
				print("Don't modify the theta.csv content, if you did, please reset it to empty")
				return 1
			else:

				if theta0 == "":
					theta0 = 0
				if theta1 == "":
					theta1 = 0

				theta0 = int(theta0)
				theta1 = int(theta1)
				mileage = int(mileage)

				print("The estimated price for the car is", linearFunction(theta0, theta1, mileage))
				return 0

	except EOFError:
		print("End of file.")
		return 1

if __name__ == "__main__":
	main()
