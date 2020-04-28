from sklearn.externals import joblib
salary_model=joblib.load("salary_model.pk1")
print("\t\t\tWelcome to future tools")
print("\t\t\t-----------------------")
print()
while True:
    print("Press 0: to exit")
    print("Press 1: Salary predict")
    print("Press 2: predict new requirements")
    print("Press 3: cal score for curr employee")
    print("Enter your choice : ",end='')
    ch=input()
    if int(ch)==1:
        print("Enter yeras of exp : ",end='')
        exp=input()
        exp=float(exp)
        print("predicted salary : " ,salary_model.predict([[exp]])[0])
    elif int (ch)==0:
        exit()

    else:
        print("option not supported")
        
    
    print("press enter key to continue")
    input()