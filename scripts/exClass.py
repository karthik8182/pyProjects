class Employee:
    empCount = 0
    def __init__(self,val1, val2):
        self.bigno = val1
        self.smallno = val2
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.bigno, ", Salary: ", self.smallno
        