def test(x):
	y = 0
	for i in range(len(x),-1,-1):
		if y == len(x):
			pass
		else:
			print(x[i-1],end="")
	
		
		
test("hello")
