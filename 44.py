shop_list = []
amount = [0,0,0,0,0]
price = [2300,1400,2100,1990,2400]
def out_item():
    n = 0
    while(True):
        print("\t สินค้าในตะกร้า มีดังนี้")
        for i in shop_list:
            n+=1
            print("\t"+str(n)+"."+i)
            n=0
            c = int(input("เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก : "))
            try:
                if c <= len(shop_list) and c!=-1:
                    shop_list.pop(c-1)
                elif c==0 and c<=len(shop_list) and c!=-1:
                    shop_list.pop(c)
                elif c==-1:
                    break
            except:
                print("กรุณากรอกลำดับสินค้าให้ถูกต้อง")
def list_item():
    print("\t รายการสินค้า")
    print("-"*50)
    print("\t1.nike cortez ราคา 2300 บาท")
    print("\t2.adidas superstar ราคา 1400 บาท")
    print("\t3.converse all star ราคา 2100 บาท")
    print("\t4.vans slip on ราคา 1990 บาท")
    print("\t5.vans old skool ราคา 2400 บาท")
def pick_item():
    c=0
    while(True):
        print("\t1.nike cortez")
        print("\t2.adidas superstar")
        print("\t3.converse all star")
        print("\t4.vans slip on")
        print("\t5.vans old skool")
        print("\t6.ออกจากฟังก์ชัน")
        c = (input("เลือกหยิบสินค้าหมายเลข : "))
        try :
            if int(c)==1 or c=="1" :
                shop_list.append("nike cortez")
            elif int(c)==2 or c=="2" :
                shop_list.append("adidas superstar")
            elif int(c)==3 or c=="3" :
                shop_list.append("converse al star")
            elif int(c)==4 or c=="4" :
                shop_list.append("vans slip on")
            elif int(c)==5 or c=="5" :
                shop_list.append("vans old skool")
            elif int(c)==6 or c=="6" :
                break
            else:
                print("กรุณากรอกหมายเลขสินค้าให้ถูกต้อง")
        except:
                print("กรุณากรอกหมายเลขสินค้าให้ถูกต้อง")
                pass
            
    def show_item():
        for i in shop_list:
            if i == "nike cortez" :
                amount[0]+=1
            elif i == "adidas superstar" :
                amount[1]+=1
            elif i == "converse all star" :
                amount[2]+=1
            elif i == "vans slip on" :
                amount[3]+=1
            elif i == "vans old skool" :
                amount[4]+=1
        amounttt = amount[0]+amount[1]+amount[2]+amount[3]+amount[4]
        pricett = amount[0]*2300+amount[1]*1400+amount[2]*2100+amount[3]*1990+amount[4]*2400
        print("")
        print("{0:_<10}{1}{0:_<10}".format("","สินค้าที่คุณได้หยิบไป มีดังนี้"))
        print("{0:.<6}{1}{0:.<6}{2}{0:.<6}{3}{0:.<07}",format("","สินค้า","จำนวน","ราคา"))
        print("{0:.<38}".format(""))
        if amount[0]!=0:
            print("{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}",format("","nike cortez",str(amount[0]*2300)))
        if amount[1]!=0:
            print("{0:.<4}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}",format("","adidas superstar",str(amount[1]*1400)))
        if amount[2]!=0:
            print("{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}",format("","converse all star",str(amount[2]*2100)))
        if amount[3]!=0:
            print("{0:.<6}{1}{0:.<8}{2}{0:.<9}{3}{0:.<10}",format("","vans slip on",str(amount[3]*1990)))
        if amount[4]!=0:
             print("{0:.<6}{1}{0:.<3}{2}{0:.<9}{3}{0:.<10}",format("","vans old skool",str(amount[4]*2400)))
        print("{0:_<38}".format(""))
        print("{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}".format("","รวม",str(amounttt),str(pricett)))
        print("")
print("\t-------- Bombam Sneaker -------")
print("-"*50)       
while(True):
    print("1. แสดงรายการสินค้า")
    print("2. หยิบสินค้าเข้าตะกร้า")
    print("3. แสดงรายจำนวนและราคาของสินค้าที่หยิบ")
    print("4. หยิบสินค้าออกจากตะกร้า")
    print("5. ปิดโปรแกรม")
    print("")
    ch = input("กรุณาเลือกทำรายการ")
    if ch=="1" :
        list_item()
    elif ch=="2" :
        pick_item()
    elif ch=="3" :
        show_item()
    elif ch=="4":
        out_item()
    elif ch=="5":
        ch = input("ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : ")
        if ch == "y":
            break
        elif ch == "n":
            continue
            import os 
price = [50,100,200,350,1000,2000]
wallet =[60,105,225,375,1185,2370]
good = [0,0,0,0,0,0]
def product():
    print(" รายการสินค้า\n",20*"-")
    for i in range(6):
        print(i+1,"STEAM WALLET",wallet[i]," ราคา",price[i],"บาท")

def choose():
    for i in range(6):
        print(i+1,"STEAM WALLET",wallet[i],"Wallet")
    data1 = int(input("กรุณาเลือกหยิบสินค้าหมายเลข :"))
    for i in range(6):
        if data1 == i+1:
            good[i] +=1

def show():
    sumz = 0
    sumx = 0 
    print(" ___สินค้าของคุณที่หยิบมีดังนี้___\n---สินค้า",17*"-"+"จำนวน",10*"-"+"ราคา---")
    for i in range(6):
        sumz = sumz+good[i]
        sumx = sumx+(good[i]*price[i])
        if good[i] > 0:
            print("STEAM WALLET",wallet[i]," Wallet",6*"-",good[i],12*"-",good[i]*price[i])
    print("รวม",23*"-",sumz,12*"-",sumx)
while(True):
    print(" โปรแกรมเติมเงิน STEAM \n",25*"-")
    print("1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.จำนวนและราคาสินค้าที่หยิบ\n 4.ปิดโปรแกรม\n