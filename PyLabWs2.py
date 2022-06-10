def q2():
    x=float(input("enter number between -180 to 180 :"))
    print( x%360 if x>0 else ("invalid statement" if x<-180 or x>180  else 360+x))
def q3():
    print("The cost per inch of the pizza is ",(3.14*(float(input("Enter the diameter in inches :")))**2)/(float(input("cost of pizza :"))*4))
def q4():
    t=int(input("enter time in seconds :"))
    print(t//60,"Min : ",t%60," Sec")
def q5():
    import math
    print(float(input("enter height in m :"))/math.sin(math.radians(math.degrees(float(input("enter angle in radians :"))))))
def q6():
    print(sum(list(range(1,int(input("enter the value of n :"))+1))))
def q7():
    names=["rohan","rajesh","kamlesh"]
    age=[18,13,19]
    print(names,age,"\nMin is ",names[age.index(min(age))],min(age),", Max is ",names[age.index(max(age))],max(age))
def q8():
    s=input("enter your string :")
    print("length of string is ",len(s)," ,",s*10)
def q9():
    d={1:['A','E','I','L','N','O','R','S','T','U'],2:['D','G'],3:['B','C','M','P'],4:['F','H','V','W','Y'],5:['K'],8:['J','X'],10:['Q','Z']}
    alpha=input("Enter alphabet :").upper()
    for i in d:
        if alpha in d[i]:
            print("The point of ",alpha," is ",i)
def q10():
    d={1:["Math","Physics","Chemistry","Philosiphy","Computer science"],2:["Biology","Physics","Chemistry","history","Computer science"]}
    print(d)
print("The output for 2nd Question is :")
q2()
print("The output for 3rd Question is :")
q3()
print("The output for 4th Question is :")
q4()
print("The output for 5th Question is :")
q5()
print("The output for 6th Question is :")
q6()
print("The output for 7th Question is :")
q7()
print("The output for 8th Question is :")
q8()
print("The output for 9th Question is :")
q9()
print("The output for 10th Question is :")
q10()

