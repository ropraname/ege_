for x in range (338472, 338495):
	divs = set()
	for d in range(1, round (x ** 0.5) + 1):
		if x % d == 0:
			divs.add (d)
			divs.add (x // d)
			if len (divs) > 4:
				break
	if len (divs) == 4:
		print(sorted(divs)[2:])