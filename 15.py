def f(x, y, A):
	return ((108 % x == 0) <= (not(x % y == 0))) or ((x + y) > 80) or ((A - y) > x)

for a in range(1, 100):
	var = True
	for x in range(1, 100):
		for y in range(1, 100):
			if not(f(x, y, a)):
				var = False
	if var == True:
		print(a)
		break
