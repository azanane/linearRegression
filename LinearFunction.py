from utils import checkFloat, parseThetas

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

			theta0, theta1 = parseThetas()

			if theta0 == "":
				theta0 = 0
			if theta1 == "":
				theta1 = 0

			theta0 = float(theta0)
			theta1 = float(theta1)
			mileage = float(mileage)

			print("The estimated price for the car is", int(linearFunction(theta0, theta1, mileage)), "euros")
			return 0

	except EOFError:
		print("End of file.")
		return 1

if __name__ == "__main__":
	main()
