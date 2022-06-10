def q1():
    return (9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5)
def q2():
    return 10 * 11 / 2
def q3():
    s1, s2 = 0, 0
    for i in range(1, 9):
        if i < 7:
            s1 += (1 / (2 * i - 1)) * (-1) ** (i - 1)
        s2 += (1 / (2 * i - 1)) * (-1) ** (i - 1)

    print("Output for 3rd ques is \n\tSum of 1st expression is " + str(4 * s1))
    print("\tSum of 2nd expression is " + str(4 * s2))
def q4():
    print("Output of 4th ques is ")
    print("\t",(input("Enter employee name: ")), int(input("Enter your age: ")), float(input("Enter your salary: ")))
def q5():
    print("Output for 5th ques is: ")
    while True:
        name = input("Enter the product name: ")
        q = int(input("Enter how much of this did u buy: "))
        p = int(input("Enter price of 1 " + name + " : "))
        print(name + "\t" + str(q) + "\t" + str(q * p))
        x = int(input("press 1 to continue "))
        if x != 1:
            break
def q6():
    print("Output for Q6 is : ")
    x = int(input("press 1 for F->C and 2 for C->F : "))
    if x == 2:
        return (9 / 5) * float(input("Enter temp in celsius : ")) + 32
    elif x == 1:
        return (float(input("enter temprature in farenhiet: ")) - 32) * 5 / 9
def q7():
    print("Output for Q7 is : ")
    p = float(input("enter principal value: "))
    r = float(input("enter rate of interest: "))
    t = int(input("enter years : "))
    n = int(input("No of times compounded in a year : "))
    print("\tSimple interest is " + str(p * t * r))
    print("\tCompound interest is " + str(p * ((1 + r / n) ** (n * t))))
def q8():
    print("Output for Q8 is :")
    a = int(input("enter value of variable 1 : "))
    b = int(input("enter value of variable 1 :"))
    print("\tvalue of a now is " + str(a) + " value of b now is " + str(b))
    a, b = b, a
    print("\tvalue of a after swap is " + str(a) + " value of b after swap is " + str(b))
def q9():
    print("Output for Q9 is : ")
    b = float(input("enter basic salary: "))
    print("\tThe total salary is : " + str(b + float(input("Enter DA in percentage : ")) * b / 100 + float(input("Enter CCA in percentage : ")) * b / 100))
def q10():
    print("Output for Q10 is :")
    for i in range(1,6):
        t = i * 365 * 24 * 60 * 60
        print("Current population after "+ str(i)+ " years is:",312032486+t//7-t//13+t//45)
'''print("Output of 1st ques is \n",q1())
print("Output of 2nd ques is \n",q2())
q3()
q4()
q5()
print(q6())
q7()
q8()
q9()
q10()'''
