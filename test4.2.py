word={}
def menu():
	print('พจนานุกรม\n 1. เพิ่มคำศัพท์\n 2. แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n')
def add():
	a = input('เพิ่มคำศัพท์ : ' )
	b = input('ชนิดคำศัพท์(n,v,adj,adv) : ')
	c = input('ความหมาย : ')
	word.update({a:{b,c}})
def view():
	print('-'*30)
	print(' '*20 +"คำศัพท์ของคุณมีดังนี้"+' '*20)
	print('-'*50)
	print('{0:-<15}{1:-<15}{2:-<10}'.format('คำศัพท์' , 'ประเภท' , 'ความหมาย'))
	for k,v in word.items():
		print(k+'	',v)
def remove():
	r = input('พิมพ์คำศัพท์ที่ต้องการลบ :')
	q = input('คุณแน่ใจใช่ไหมว่าต้องการลบ (y/n) :')
	if q == 'y':
		word.pop(r)
	else:
		print(' ')

while True:
	menu()
	me = int(input('เลือกรายการที่ต้องการ : '))
	if me == 1:
		add()
	elif me == 2:
		view()
	elif me == 3:
		remove()
	else:
		q = input('คุณแน่ใจใช่มั้ยว่าต้องการออกจากโปรแกรม : ')
		if q == 'y':
			break
		else:
			print(' ')
