y = 0
def test(x):
y+=1
if y == len(x):
	pass
else:
	for i in range(len(x),-1,-1):
		print(x[i-1],end="")
	
		
		
test("hello")
