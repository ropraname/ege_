def f(a,b,n):
	if a + b >= 211 or n > 4:
		return n == 2 or n == 4
	if n % 2 == 0:
		return all([f(a + 1, b, n + 1), f(a * 2, b, n + 1), f(a, b + 1, n + 1), f(a, b * 2, n + 1)])
	return any([f(a + 1, b, n + 1), f(a * 2, b, n + 1), f(a, b + 1, n + 1), f(a, b * 2, n + 1)])
print([s for s in range (1, 193 + 1) if f(17, s, 0)])