student = int(input("Please enter student : "))
print("-"*30)
total = [0 , 0 , 0 , 0 , 0 , 0]
score = ['90-100  :','80-89  :','70-79  :','60-69  :','50-59  :','0-49  :']
a = 1
while a <= student :
	point = int(input("Please enter score : "))
	if point <= 100 and point >= 90 :
		total[0] += 1
	elif point < 90 and point >= 80 :
		total[1] += 1
	elif point < 80 and point >= 70 :
		total[2] += 1
	elif point < 70 and point >= 60 :
		total[3] += 1
	elif point < 60 and point >= 50 :
		total[4] += 1
	elif point < 50 and point >= 0 :
		total[5] += 1
	a = a+1
for a in range(0,6) :
	print(score[a],"*"*total[a])