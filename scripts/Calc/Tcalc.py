#! usr/bin/python



def Tcalc(no1,no2,tType):

    a = int(no1)
    b = int(no2)

    if tType == "Sum":
        total = a + b
        print "adding the nos %s + %s = %s" %(a,b,total)
        return (total)

    elif tType=="Sub":
        total = a - b
        print "Subtracting the nos %s - %s = %s" %(a,b,total)
        return (total)

    elif tType == "Div":
        total = a/b
        print "dividing the nos %s / %s = %s" % (a, b,total)
        return (total)

    elif tType == "Mul":
        total = a * b
        print "Multiplication of the nos %s x %s = %s" % (a, b,total)
        return (total)
    else:
        print "Not an accepted calculation type "

