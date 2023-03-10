# Два игрока, Петя и Ваня, играют в следующую игру. 
# Перед игроками лежит куча камней. Игроки ходят по очереди, 
# первый ход делает Петя. За один ход игрок может добавить в
# кучу один камень или увеличить количество камней в куче в два раза.
# Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
# Игра завершается в тот момент, когда количество камней в куче становится не менее 29.
# Победителем считается игрок, сделавший последний ход, т.е. первым получивший кучу, в 
# которой будет 29 или больше камней. В начальный момент в куче было S камней, 1 ≤ § ≤ 28.
# Будем говорить, что игрок имеет выигрышную стратегию, если он
# может выиграть при любых ходах противника. 19.Укажите такое значение S, при котором Петя не
# может выиграть за один ход, но при любом ходе Пети Ваня может
# выиграть своим первым ходом.
def f(a, n):
	if a >= 29 or n > 2:
		return n == 2
	if n % 2 == 0:
		return all([f(a + 1, n + 1), f(a * 2, n + 1)])
	return any([f(a + 1, n + 1), f(a * 2, n + 1)])

for s in range(1, 28):
	if f(s, 0):
		print(s)