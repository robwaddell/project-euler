#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.

if __name__ == "__main__":
	#O(n) runtime
	multipleSum = 0
	for i in range(1000):
		if i % 3 == 0 or i % 5 == 0:
			multipleSum += i
	print(multipleSum)

	#O(n) runtime
	#add all multiples of 3 under 1000
	#add all multiples of 5 under 1000
	#subtract numbers that are multiples of both 5 and 3, because
	# we want to count them only once, and they will be counted in
	# both of the above loops. So subtract to "undo" one of the countings
	multipleSum = 0
	for i in range(3, 1000, 3):
		multipleSum += i
	for i in range(5, 1000, 5):
		multipleSum += i
	for i in range(15, 1000, 15):
		multipleSum -= i
	print(multipleSum)

	#O(n) runtime
	#list comprehension solution
	multipleSum = sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
	print(multipleSum)

	#O(1) runtime
	#the sum of the first n positive integers is (n(n+1))/2  (Carl Gauss)
	#the sum of the first n multiples of x is then x(n(n+1)/2)
	#the number of multiples of x under (and not including) m = 1000 is
	# floor((m-1)/x)
	multipleSum = 0
	numMultiples = (1000 - 1) // 3
	multipleSum += 3 * ((numMultiples * (numMultiples + 1)) // 2)
	numMultiples = (1000 - 1) // 5
	multipleSum += 5 * ((numMultiples * (numMultiples + 1)) // 2)
	numMultiples = (1000 - 1) // 15
	multipleSum -= 15 * ((numMultiples * (numMultiples + 1)) // 2)
	print(multipleSum)
