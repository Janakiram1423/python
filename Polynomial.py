class node:
    def __init__(self,coeff,power):
        self.coeff=coeff
        self.pow=power
        self.next=None

class polynomial:
    def __init__(self):
        self.head=None
        
    def insert(self,coeff,power):
        new=node(coeff,power)
        if self.head is None:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        
    def display(self):
        temp=self.head
        while temp:
            print(f"{temp.coeff}*^{temp.power}",end="")
            if temp.next:
                print("+",end="")
            temp=temp.next
        print()
        
    def add(poly1,poly2):
        p=p1.head
        q=p2.hed
        result=polynomial()
        while p and q:
            if p.power ==  q.power:
                result.insert(p.coeff+q.coeff,p.power)
                p=p.next
                q=q.next
            elif p.power > q.power:
                result.insert(p.coeff,p.power)
                p=p.next
            else:
                result.insert(p.coeff,p.power)
            while p:
                result.insert(p.coeff,p.power)
                p=p.next
            while q:
                result.insert(q.coeff,q.power)
                q=q.next
                return result
    
p1=polynomial()
p2=polynomial()
n1=int(input("Enter number of terms in polynomianl 1:"))
print("Enter co-efficient and power:")

for i in range(n1):
    c,p=map(int,input().split())
    p1.insert(c,p)
n2=int(input("Enter number of terms in polynomianl 2:"))
print("Enter co-efficient and power:")

for i in range(n2):
    c,p=map(int,input().split())
    p2.insert(c,p)
print("\nPolynomail1:")
p1.display()
print("\nPolynomial2:")
p2.display()
result=add(p1,p2)
print("\nResult :")
result.display()
