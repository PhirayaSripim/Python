listshop=[0,0,0,0,0]
cost=[7,8,6,10,9]
def menu():
	global choice
	print('PlaiifahWater\n 1. แสดงรายการสินค้า\n 2. หยิบสินค้าใส่ตะกร้า\n 3.แสดงรายการจำนวนและราคาสินค้าที่หยิบ\n 4.หยิบสิค้าออกจากตะกร้า\n 5.ปิดโปรแกรม ')
	choice = input('กรุณาเลือกทำรายการ : ')

def costmenu():
	print('\n1. น้ำดื่มทิพย์ ราคา 7 บาท\n 2. น้ำดื่มคริสตรัล ราคา 8 บาท\n 3. น้ำดื่มเพียวไลฟ์ ราคา 6 บาท\n 4. น้ำดื่มมิเนเล่ ราคา 10 บาท\n 5. น้ำดื่มสิงห์ ราคา 9 บาท\n ')

def pickmenu():
	global pick
	print('\nรายากรสินค้า\n 1.น้ำดื่มทิพย์ \n 2.น้ำดื่มคริสตรัล\n 3.น้ำดื่มเพียวไลฟ์\n 4. น้ำดื่มมิเนเล่\n 5. น้ำดื่มสิงห์')
	pick = int(input('เลือกหยิบสินค้าหมายเลข : '))
	if pick == 1:
		listshop[0] += 1
	elif pick == 2:
		listshop[1] += 1
	elif pick == 3:
		listshop[2] += 1
	elif pick == 4:
		listshop[3] += 1
	elif pick == 5:
		listshop[4] += 1

def allpick():
	list_water = ["น้ำดื่มทิพย์" ,"น้ำดื่มคริสตรัล" ,"น้ำดื่มเพียวไลฟ์" ,"น้ำดื่มมิเนเล่" ,"น้ำดื่มสิงห์"]
	list_cost = [7,8,6,10,9]
	for i in range(5):
		print("{0:-<20}{1:-<10}{2}".format(list_water[i],list_cost[i],listshop[i],listshop[i]*list_cost[i]))

def outpick():
	print('รายการสินค้า\n 1.น้ำดื่มทิพย์\n 2.น้ำดื่มคริสตรัล\n 3.น้ำดื่มเพียวไลฟ์\n 4.น้ำดื่มมิเนเล่\n 5.น้ำดื่มสิงห์')
	outpick = int(input("เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก"))
	if outpick == 1:
		listshop[0] -=1
	elif outpick == 2:
		listshop[1] -=1
	elif outpick == 3:
		listshop[2] -=1
	elif outpick == 4:
		listshop[3] -=1
	elif outpick == 5:
		listshop[4] -=1

while True:
	menu()
	if choice == '1':
		costmenu()
	elif choice == '2':
		pickmenu()
	elif choice == '3':
		allpick()
	elif choice == '4':
		outpick()
	elif choice == '5':
		ch = input("ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n: ")
		if ch == 'y':
		   break
		elif ch == 'n':
		   continue