def T():
    global name,grade,sex,province,department,faculty
    print("_"*20+"แนะนำตัว"+"_"*20)

    T = input("ชื่อ-สกุล :  ชั้น  :  เพศ  :  จังหวัด  :  สาขา  :  คณะ         ")  
    add = T.split(":")
    name = add[0]
    grade = add[1]
    sex = add[2]
    province = add[3]
    department = add[4]
    faculty = add[5]
class nisit :
    def __init__(self,name,grade,sex,province,department,faculty) :
        self.name = name
        self.grade = grade
        self.sex = sex
        self.province = province 
        self.department = department
        self.faculty = faculty

    def showname(self) :
        print('สวัสดีค่ะ ฉันชื่อ    '+self.name+  '     เรียนอยู่ชั้นปีที่    '  +self.grade+  '     เพศ     '   +self.sex+  '    มาจากจังหวัด    '   +self.province+  '     เรียนอยู่สาขา   '   +self.department+   '     เรียนอยู่คณะ       '   +self.faculty)
T()
X = nisit(name,grade,sex,province,department,faculty)
X.showname()