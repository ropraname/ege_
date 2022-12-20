for n in range(1000):
	bn = bin(n)[2:]
	for c in range(3):
		sum_ = 0
		for i in str(int(bn, 2)):
			sum_ += int(i)
		if sum_ % 2 == 1:
			bn += '1'
		else:
			bn += '0'
	if int(bn, 2) > 2054:
		print(int(bn, 2))
		break
