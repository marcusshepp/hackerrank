def eat_this(dollars, flavors, prices):
	for i in range(len(prices)-1):
		for j in prices:
			if prices[i] + j == dollars:
				x = min(prices[i], j), max(prices[i], j)
	return "".join(str(x)).replace(",", "").replace(")", "").replace("(", "")

for i in range(int(raw_input())):
	dollars = int(raw_input())
	flavors = int(raw_input())
	prices = [int(x) for x in raw_input().split()]
	print eat_this(dollars, flavors, prices)
