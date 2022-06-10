#question 39
class AutoMobile:
    def __init__(self,make,modelYear,mileage,price,color,airbags):
        self.make=make
        self.modelYear=modelYear
        self.mileage=mileage
        self.price=price
        self.color=color
        self.airbags=airbags

class Car(AutoMobile):
    carCount=0
    def __init__(self,make,modelYear,mileage,price,color,airbags,no_doors,sunRoof,electric):
        super().__init__(make,modelYear,mileage,price,color,airbags)# calling constructor of base class using super
        self.no_doors=no_doors
        self.sunRoof=sunRoof
        self.electric=electric
        Car.carCount+=1

    def __str__(self):
        #using F string to make a nice output
        return f"Make : {self.make}\nModel-Year : {self.modelYear}\nMileage (Km/L) : {self.mileage}\nPrice(Rs) : {self.price}\nColor : {self.color}\nAirbags : {self.airbags}\nNumber of doors : {self.no_doors}"

class PUtrucks(AutoMobile):
    puTcount=0
    def __init__(self, make, modelYear, mileage, price,color,airbags,driveType):
        super().__init__(make, modelYear, mileage, price,color,airbags)
        self.driveType=driveType
        PUtrucks.puTcount+=1
    def __str__(self):
        return f"Make : {self.make}\nModel-Year : {self.modelYear}\nMileage (Km/L) : {self.mileage}\nPrice(Rs) : {self.price}\nColor : {self.color}\nAirbags : {self.airbags}\nDrive-type : {self.driveType}"

class SUV(AutoMobile):
    suvCount=0
    def __init__(self,make,modelYear,mileage,price,color,airbags,capacity):
        super().__init__(make,modelYear,mileage,price,color,airbags)
        self.capacity=capacity
        SUV.suvCount+=1
    def __str__(self):
        return f"Make : {self.make}\nModel-Year : {self.modelYear}\nMileage (Km/L) : {self.mileage}\nPrice(Rs) : {self.price}\nColor : {self.color}\nAirbags : {self.airbags}\nCapacity : {self.capacity}"

def main():
    carList=[]
    puTruckList=[]
    suvList=[]
    while True:
        print("Enter which type of AutoMobile you want to enter data into : ")
        n=int(input("(1) Car : \n(2) PickupTruck : \n(3) Suv : \n(4) Exit & Display : "))
        if n==4:
            print()
            break
        while True:
            try:
                makein=input("Enter the make of the AutoMobile : ")
                break
            except:
                print("invalid make! enter again...")
        while True:
            try:
                model_year=int(input("Enter the Model Year of the AutoMobile : "))
                if model_year>1800:
                    break
                else:
                    print("AutoMobiles weren't made before 1800.... ")
                    print("Enter Again....")

            except:
                print("invalid Model Year! enter again...")
        while True:
            try:
                mil=float(input("Enter the Mileage of the AutoMobile (Km/L): "))
                if mil>0:
                    break
                else:
                    print("Mileage can't be negative.... ")
                    print("Enter Again....")

            except:
                print("invalid Mileage ! enter again...")
        while True:
            try:
                cost=float(input("Enter the price of the AutoMobile (Rs): "))
                if cost>0:
                    break
                else:
                    print("Price can't be negative.... ")
                    print("Enter Again....")

            except:
                print("invalid Price ! enter again...")
        while True:
            try:
                colorin=input("Enter the color of the AutoMobile : ")
                break
            except:
                print("invalid color! enter again...")
        while True:
            try:
                airbag=int(input("Enter the No of Airbags of the AutoMobile : "))
                if airbag>0 :
                    break
                else:
                    print("Airbags can't be negative! \nEnter again.... ")

            except:
                print("Invalid Airbags! Enter Again....")
        if n==1:
            while True:
                try:
                    ndoor = int(input("Enter the No of doors of the Car: "))
                    if ndoor== 4 or ndoor==2:
                        break
                    else:
                        print("Doors can be only 2 or 4.... ")
                        print("Enter Again....")

                except:
                    print("invalid Doorno ! enter again...")
            while True:
                try:
                    sun_roof = input("Enter yes/no for sunroof of Car : ")
                    break
                except:
                    print("invalid make! enter again...")
            while True:
                try:
                    elec = input("Enter yes/no for electric Car : ")
                    break
                except:
                    print("invalid make! enter again...")
            carList.append(Car(makein,model_year,mil,cost,colorin,airbag,ndoor,sun_roof,elec))
        if n==2:
            while True:
                try:
                    d_type = int(input("Enter the drive type of the pickup Truck: "))
                    if d_type == 4 or d_type == 2:
                        break
                    else:
                        print("Drive type can be only 2 or 4.... ")
                        print("Enter Again....")

                except:
                    print("invalid Drive type ! enter again...")
            puTruckList.append(PUtrucks(makein,model_year,mil,cost,colorin,airbag,d_type))
        if n==3:
            while True:
                try:
                    capi = int(input("Enter the capacity of the SUV: "))
                    if 2<=capi<=20:
                        break

                    else:
                        print("Capacity can't be in this range.... ")
                        print("Enter Again....")
                except:
                    print("Invalid capicity! Enter Again...")
            suvList.append(SUV(makein,model_year,mil,cost,colorin,airbag,capi))
        print()


    while True:
        print("Enter which type of AutoMobile you want to display : ")
        n = int(input("(1) Car : \n(2) PickupTruck : \n(3) Suv : \n(4) Exit & Display : "))

        if n==1:
            print()
            for car in carList:
                print()
                print(car)
        if n==2:
            for puTruck in puTruckList:
                print(puTruck)
        if n==3:
            for suv in suvList:
                print(suv)
        if n==4:
            break
        print()
    print("\nPROGRAM ENDED SUCCESFULLY")






main()