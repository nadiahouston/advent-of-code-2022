import re

# Part 1
print(
	sum(
		[
			not ((int(a) < int(x) and int(b) < int(y)) or
				 (int(a) > int(x) and int(b) > int(y)))
			for a, b, x, y in [
				re.split(',|-', line) for line in open('input.txt').read().splitlines()
			]
		]
	)
)

# Part 2
print(
	sum(
		[
			not ((int(a) < int(x) and int(b) < int(x)) or
				 (int(a) > int(y) and int(b) > int(y)))
			for a, b, x, y in [
				re.split(',|-', line) for line in open('input.txt').read().splitlines()
			]
		]
	)
)