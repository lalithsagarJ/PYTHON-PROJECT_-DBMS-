import mysql.connector as connector
con=connector.connect(host="localhost",
                        user="root",
                        passwd="root",
                        database="dbcollege")
cur=con.cursor()


def student_login():

    print("\n\n\t*****WELCOME TO STUDEDNT LOGIN*****")
    usn=input('student usn : ')
    passwordd=input("passwordd : ")
    return (usn,passwordd)


def adviser_login():

    print("\n\n\t*****CLASS ADVISER LOGIN*****")
    print('faculty id : ')
    id=input()
    print("passwordd : ")
    passwordd=input()
    return (id,passwordd)


# STUDENT CLASS
class student :
    def __init__(self):
        usn, passwordd = student_login ()
        query = 'select * from student'
        cur.execute (query)
        r = cur.fetchall ()
        for i in r:
            if usn == i[0]:
                if passwordd == i[5]:
                    print ("name: {}\nUSN: {}\n".format (i[1], i[0]))
                    query = "select * from iamarks where usn=%s "
                    cur.execute (query, (usn,))
                    res = cur.fetchall ()
                    print ("\n\t\t****results****\n\n  subject \t\tfinal marks\t\teligibility\n")
                    for j in res:
                        eligible = 'yes'
                        if j[6] < 9:
                            eligible = 'no'
                        print ("  ",j[1], "\t\t", float(j[6]), "\t\t\t", eligible, "\n")
                    break
                else:
                    print ("\t\taccess denied\n\t\tcheck your passwordd ")
                    break
        else:
            print ("USN : {} not found".format (usn))



def classs2A(id,password):
    query='select * from class_adviser where ssid=1'
    cur.execute(query)
    res=cur.fetchall()
    for i in res:
        if id==i[0]:
            if password==i[2]:
                print ("\nname: {}\nFID: {}\n".format (i[1], i[0]))
                print("Class Adviser of Class 2A ")
                while(1):
                    print("---options---")
                    print("1-view class marks\n2-view class attendence\n3-view single student marks\n4-update marks\n-update attendence\n0-Exit\n")
                    ch=int(input())

                    # view class marks
                    if ch == 1:
                        query='select * from iamarks where ssid=1'
                        cur.execute(query)
                        store=cur.fetchall()
                        print ("\nuUSN\t\t\tSubject Code\t\tssid\t\tTest1\tTest2\tTest3\t\tfinal marks\t\teligibility\n")
                        for j in store:
                            eligible = 'yes'
                            if j[6] < 9:
                                eligible = 'no'
                            print (j[0],'\t\t',j[1], '\t\t\t', j[2],'\t\t\t',float(j[3]),'\t',float(j[4]), '\t', float(j[5]),'\t\t', float(j[6]),"\t\t\t",eligible,"\n")

                    # view class attendence
                    elif ch==2:
                        query='select * from attendance where ssid=1'
                        cur.execute(query)
                        store=cur.fetchall()
                        print("USN\t\t\tSubject code\t\tssid\t\tattendence\t\teligibility\n")
                        for j in store:
                            eligible='yes'
                            if j[3]<75:
                                eligible='no'
                            print(j[0],"\t\t",j[1],"\t\t",j[2],"\t\t\t",j[3],"\t\t\t",eligible,"\n")

                    # view marks by student usn
                    elif ch==3:
                        USN=input("Enter usn to View Marks : ")
                        query='select * from iamarks where usn=%s AND ssid=1'
                        cur.execute(query,(USN,))
                        store=cur.fetchall()
                        print ("\t\tSubject Code\t\tssid\t\tTest1\tTest2\tTest3\t\tfinal marks\t\teligibility\n")
                        for j in store:
                            eligible = 'yes'
                            if j[6] < 9:
                                eligible = 'no'
                            print ('\t\t',j[1],'\t\t\t', j[2], '\t\t\t', float (j[3]), '\t', float (j[4]), '\t',float (j[5]), '\t\t', float (j[6]), "\t\t\t", eligible, "\n")

                    #update marks of student
                    elif ch==4:
                        query1='select * from sub where sem=2'
                        cur.execute(query1)
                        r=cur.fetchall()
                        print ("subcode\t\tCourse Name\n")
                        for k in r:
                            print(k[0],"\t\t",k[1],"\n")
                        USN = input ("Enter usn to Update Marks : ")
                        sub=input("Enter subject code : ")
                        t1 = int (input ("Test 1 marks: "))
                        t2 = int (input ("Test 2 marks: "))
                        t3 = int (input ("Test 3 marks: "))

                        query="update iamarks set(subcode='%s',)"




                    # EXIT from class2A
                    elif ch == 0:
                        break
                break
            else:
                print("\t\taccess denied\n\t\tcheck your passwordd ")
                break
    else:
        print ("FID : {} not found in class 2A".format (id))


#def classs2B(id,password):
    
#def classs2C(id,password):
    
#def classs4A(id,password):
    
#def classs4B(id,password):
    
#def classs4C(id,password):
    
#def classs6A(id,password):
    
#def classs6B(id,password):
    
#def classs6C(id,password):
    
#def classs8A(id,password):
    
#def classs8B(id,password):
    
#def classs8C(id,password):
    
    
    
# CLASS ADVISER
class class_adviser:
    def __init__(self) : 
        id,password=adviser_login()
        print("\nCSE Department\n1) class 2A\n2) class 2B\n3) class 2C\n4) class 4A\n5) class 4B\n6) class 4C\n7) class 6A\n8) class 6B\n9) class 6C\n10) class 8A\n11) class 8B\n12) class 8C\n\nSelect Your Class : ",end='')
        ch=int(input())
        if ch==1:
            classs2A(id,password)
        elif ch==2:
            classs2B(id,password)
        elif ch==3:
            classs2C(id,password)
        elif ch==4:
            classs4A(id,password)
        elif ch==5:
            classs4B(id,password)
        elif ch==6:
            classs4C(id,password)
        elif ch==7:
            classs6A(id,password)
        elif ch==8:
            classs6B(id,password)
        elif ch==9:
            classs6C(id,password)
        elif ch==10:
            classs8A(id,password)
        elif ch==11:
            classs8B(id,password)
        elif ch==12:
            classs8C(id,password)
        else:
            print("wrong choice")



def main():
    while(1):
        print('\n\n\n----------------------------------------------------\n--------------SEMESTER EXAM ELEGIBILITY--------------\n----------------------------------------------------\nENTER 1 FOR : STUDENT ELIGIBILITY RESULT\nENTER 2 FOR : FACULTY LOGIN\nENTER 0 : EXIT\nCHOICE : ',end='' )
        ch=int(input())
        
        if ch==1:
            h = student()
        elif ch==2:
            f = class_adviser()
        elif ch==0:
            exit()
        else:
            print("wrong input")


if __name__ == '__main__':
    main()
