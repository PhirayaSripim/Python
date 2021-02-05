print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
list=[]
i=1
j=0
z=1
while(True):
    j=input("อาหารสุดโปรดลำดับที่ "  +str(i)+   " คือ ")
    list.append(j)
    i+=1
    if j == "exit":
        print("\n อาหารสุดโปรดของคุณคือ" )
        list.pop()
        break # หยุดการทำงาน
for x in list :
    print(str(z)+x,end="  ")
    z+=1
