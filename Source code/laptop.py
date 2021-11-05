class Laptop:
    def __init__(self,ten,hang,gia,soluong):
        self.name = ten
        self.brand = hang
        self.price = gia
        self.quantum = soluong
    def xuatgia(self):
        return self.price
new= Laptop("G3","Dell",25000,3)




