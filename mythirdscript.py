name="Henry"
height=250
weight=100
bmi=(height*0.4)
print("масса тела равна"+str(bmi))
if bmi<=(height*0.4):
	print ("У "+name+" нет лишнего веса")
if bmi>(height*0.4):
	print ("У "+name+" имеется лишний вес")