import itertools

s = 'ВЕРОНИКА'
gl = 'ЕОИА'
sog = 'ВРНК'

cnt = 0

for i in itertools.product(s, repeat=6):
	ns = ''.join(i)
	cnt_s = 0
	cnt_g = 0
	for j in ns:
		if j in gl:
			cnt_g += 1
		elif j in sog:
			cnt_s += 1
	if cnt_g > cnt_s:
		print(ns)
		cnt += 1
print(cnt)