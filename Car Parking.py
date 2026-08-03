queue=[]
max = 5
def enqueue():
    if len(queue)==max:
        print("Parking is full.")
    else:
        car=input("Enter call number:")
        queue.append(car)
        print(car,"has entered the parking.")
def dequeue():
    if len(queue)==0:
        print("Parking is empty.")
    else:
        car=queue.pop(0)
        print(car,"has exited the parking.")
def display():
    if len(queue)==0:
        print("No cars int he parking.")
    else:
        print("Car is parking.")
        for car in queue:
            print(car)
while True:
    print("\n----CAR PARKING SYSTEM----")
    print("1.Park car(enqueue)")
    print("2.Remove car(dequeue)")
    print("3.Display")
    print("4.Exit")
    ch=int(input("Enter your choice:"))
    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        print("Exiting the program.")
        break
    else:
        print("Invaild choice.")
