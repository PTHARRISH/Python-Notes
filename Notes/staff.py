class staff:
    def __init__(self,name,age,qualification,role,mobile_no):
        self.name=name
        self.qualification=qualification
        self.age=age
        self.role=role
        self.mobile_no=mobile_no

class staff_personal_details:
    def __init__(self):
        self.staff_details=[]
    
    def add_details(self,name,age,qualification,role,mobile_no):
        return self.staff_details.append(staff(name,age,qualification,role,mobile_no))
        


staff1=staff_personal_details()
staff1.add_details('harrish',18,'MCA','developer',9087654321)


