# Part 1
print(
	sum(
		[ 
			(lambda x: ord(x) - (38 if x.isupper() else 96))((x & y).pop())
			for x, y in [
				(
					set(contents[: len(contents)//2]),
					set(contents[len(contents)//2 :])
				)
				for contents in open("input.txt").read().splitlines()
			]
		]
	)
)

# Part 2
from more_itertools import batched

print(
	sum(
		[ 
			(lambda x: ord(x) - (38 if x.isupper() else 96))(
				(set(x) & set(y) & set(z)).pop()
			)		
			for x, y, z in batched(
				open("input.txt").read().splitlines(), 3
			)
		]
	)
)