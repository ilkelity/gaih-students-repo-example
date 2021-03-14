# THIS IS A  STUDENT PASSING GRADE CALCULATOR

list = ["John Smith" ,"Angela Wilkinson" ,"David Williams" ,"Susan Jones" ,"Frank Hall"]

info2 = print("This is a student grade calculator!\nTo use this calculator students' name must be in this school list\nHERE are our students names\nplease enter one of them")
john = {"John Smith": "student", "midterm": 45, "project grade": 88, "final grade": 78}
angela = {"Angela Wilkinson": "student", "midterm": 80, "project grade": 40, "final grade": 90}
susan = {"Susan Jones": "student", "midterm": 70, "project grade": 70, "final grade": 80}
david = {"David Williams": "student", "midterm": 70, "project grade": 85, "final grade": 40}
frank = {"Frank Hall": "student", "midterm": 81, "project grade": 50, "final grade": 64}

info0 = input(list)
print(info0)
if  info0 in john:
        print("here John's information, so you can calculate his passing grade")
        print(john)
        midj = int(input("enter midterm score"))
        projectj = int(input("enter project score"))
        finalj = int(input("final grade?"))
        passingdavid = float(midj*0.3+finalj*0.7+projectj*0.3)
        print("passing grade is:")
        print(passingdavid)
if  info0 in angela:
       print("that is Angela's information,  so you can calculate her passing grade")
       print(angela)
       mida = int(input("enter midterm score"))
       projecta = int(input("enter project score"))
       finala = int(input("final grade?"))
       passingangela = float(mida * 0.3 + finala * 0.7 + projecta * 0.3)
       print("passing grade is:")
       print(passingangela)
if  info0 in susan:
        print("that is Susan's information,  so you can calculate her passing grade")
        print(susan)
        mids = int(input("enter midterm score"))
        projects = int(input("enter project score"))
        finals = int(input("final grade?"))
        passingsusan = float(mids * 0.3 + finals * 0.7 + projects * 0.3)
        print("passing grade is:")
        print(passingsusan)
if  info0 in david:
        print("that is david's information,  so you can calculate his passing grade")
        print(david)
        midd = int(input("enter midterm score"))
        projectd = int(input("enter project score"))
        finald = int(input("final grade?"))
        passingdavid = float(midd * 0.3 + finald * 0.7 + projectd * 0.3)
        print("passing grade is:")
        print(passingdavid)
if  info0 in frank:
        print("that is frank's information,  so you can calculate his passing grade")
        print(frank)
        midf = int(input("enter midterm score"))
        projectf = int(input("enter project score"))
        finalf = int(input("final grade?"))
        passingfrank = float(midf * 0.3 + finalf * 0.7 + projectf * 0.3)
        print("passing grade is:")
        print(passingfrank)
if  info0 not in list:
        print("that person does not exists in our school")

grades =  ["Angela Wilkinson,99.0 ", "Susan Jones, 98.0", "John Smith,94.5", "Frank Hall,84.1","David Williams,74.5"]

soru = input("would you like to see the ranking between our students from best to last? yes or no:")
if soru == "yes":
        print(grades)
else:
        print("OKAY, that is it")
