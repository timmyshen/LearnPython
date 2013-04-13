def mySol(input_i, increment):
	''' My solution to drill '''
	# i = 0
	numbers = []

	for i in range(0, input_i, increment):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	# while i < input_i:
		# print "At the top i is %d" % i
		# numbers.append(i)

		# i += increment
		# print "Numbers now: ", numbers
		# print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

mySol(6,2)