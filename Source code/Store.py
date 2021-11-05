from laptop import Laptop
import pandas as pd
class Store:
    list_brand=set()
    list_product=[]
    def add_brand(self,new_brand):
        if (new_brand in self.list_brand):
            print("Da ton tai")
        else:
            self.list_brand.add(new_brand)
    def print_brand(self):
        print("Danh sach cac hang")
        for brand in self.list_brand:
            print(brand)
    def delete_brand(self):
        self.print_brand()
        brand=input("Nhap ten hang muon xoa: ")
        self.list_brand.remove(brand)
        print("Xoa thanh cong!!!")
    def add_product(self):
        name=input("Nhap ten Laptop: ")
        brand=input("Nhap hang Laptop: ")
        price=input("Nhap gia ban san pham: ")
        quantum=input("Nhap so luong san pham: ")
        product = Laptop(name,brand,price,quantum)
        self.list_product.append(product)
    def save_product(self):
        f=open("product.csv",'a')
        for i in self.list_product:
            f.write(i.name+','+i.brand +','+i.price+','+i.quantum+'\n')

    def print_product(self):
        df_product = pd.read_csv("product.csv", sep=',', names=["Ten san pham", "Hang", "Gia", "So luong"])
        print(df_product)
    def update_product(self):
        df_product = pd.read_csv("product.csv", sep=',', names=["Ten san pham", "Hang", "Gia", "So luong"])
        print("\n\t\tDANH SACH SAN PHAM")
        print(df_product)
        index = int(input("\nNhap so thu tu san pham muon cap nhat: "))
        print("Tien hanh cap nhat: ")
        df_product.at[index, 'Ten san pham'] = input("Nhap ten Laptop: ")
        df_product.at[index, 'Hang'] = input("Nhap hang Laptop: ")
        df_product.at[index, 'Gia'] = input("Nhap gia san pham: ")
        df_product.at[index, 'So luong'] = input("Nhap so luong san pham: ")
        df_product.to_csv('product.csv', header=False, index=False)
        print("\n\t\tDANH SACH SAN PHAM")
        print(df_product)
    def remove_product(self):
        df_product = pd.read_csv("product.csv", sep=',', names=["Ten san pham", "Hang", "Gia", "So luong"])
        print("\n\t\tDANH SACH SAN PHAM")
        print(df_product)
        index = int(input("Nhap so thu tu san pham muon xoa: "))
        df_product.drop(index, inplace=True)
        print("Xoa thanh cong!!!")
        print("\n\t\tDANH SACH SAN PHAM")
        print(df_product.reset_index(drop=True))
        df_product.to_csv('product.csv', header=False, index=False)

    def create_bill(self):
        name = input("Nhap ten Laptop: ")
        brand = input("Nhap hang Laptop: ")
        price = input("Nhap gia san pham: ")
        quantum = input("Nhap so luong san pham: ")
        customer=input("Nhap ten khach hang: ")
        date=input("Nhap ngay mua: ")
        month=input("Nhap thang mua: ")
        product = Laptop(name, brand, price, quantum)
        df_product = pd.read_csv("product.csv", sep=',', names=["Ten san pham", "Hang", "Gia", "So luong"])
        if(name in df_product['Ten san pham'].values):
            index=df_product[df_product['Ten san pham']==name]['So luong'].index
            value=df_product[df_product['Ten san pham']==name]['So luong']-int(quantum)
            df_product.at[index,'So luong']=value
        df_product.to_csv('product.csv',header=False,index=False)
        f = open("bill.csv", 'a')
        f.write(name + ',' + brand + ',' + price + ',' + quantum +',' +str(int(price)*int(quantum))+','+ customer +','+date+','+month+'\n')
    def update_bill(self):
        df_bill=df_product = pd.read_csv("bill.csv", sep=',', names=["Ten san pham", "Hang", "Gia", "So luong","Tong tien","Ten khach hang","Ngay","Thang"])
        print("\n\t\tDANH SACH DON HANG")
        print(df_bill)
        index=int(input("\nNhap so thu tu don muon sua: "))
        print("Tien hanh cap nhat: ")
        df_bill.at[index, 'Ten san pham'] = input("Nhap ten Laptop: ")
        df_bill.at[index, 'Hang'] = input("Nhap hang Laptop: ")
        df_bill.at[index, 'Gia'] = input("Nhap gia san pham: ")
        df_bill.at[index, 'So luong'] = input("Nhap so luong san pham: ")
        df_bill.at[index, 'Tong tien: ']=int(df_bill.at[index, 'Gia'])*int(df_bill.at[index, 'So luong'])
        df_bill.at[index, 'Ten khach hang'] = input("Nhap ten khach hang: ")
        df_bill.at[index, 'Ngay'] = input("Nhap ngay mua: ")
        df_bill.at[index, 'Thang'] = input("Nhap thang mua: ")
        df_bill.to_csv('bill.csv', header=False, index=False)
        print("Cap nhat thanh cong")
        print("\n\t\tDANH SACH DON HANG")
        print(df_bill)
    def delete_bill(self):
        df_bill  = pd.read_csv("bill.csv", sep=',',
                                           names=["Ten san pham", "Hang", "Gia", "So luong","Tong tien" ,"Ten khach hang",
                                                  "Ngay","Thang"])
        print(df_bill)
        index = int(input("Nhap so thu tu don muon xoa: "))
        df_bill.drop(index,inplace=True)
        print(df_bill)
        df_bill.to_csv('bill.csv', header=False, index=False)
        print("\nXoa don thanh cong!!!")
    def print_bill(self):
        print("\n\t\tDON HANG")
        df_bill = pd.read_csv("bill.csv", sep=',',
                              names=["Ten san pham", "Hang", "Gia", "So luong", "Tong tien", "Ten khach hang",
                                     "Ngay", "Thang"])
        print(df_bill)
    def show_product_over(self):
        df_product = pd.read_csv("product.csv", sep=',', names=["Ten san pham", "Hang", "Gia", "So luong"])
        df_over=df_product[df_product['So luong']<10]
        if df_over.empty:
            print('Khong co mat hang nao sap het')
        else:
            print("\n\t\tSAN PHAM")
            print(df_over.reset_index(drop=True))
    def show_best_seller(self):
        df_bill = pd.read_csv("bill.csv", sep=',',
                              names=["Ten san pham", "Hang", "Gia", "So luong", "Tong tien","Ten khach hang",
                                     "Ngay","Thang"])
        month=int(input("Nhap thang: "))
        df_sell=df_bill[df_bill["Thang"]==month ]
        df_sell=df_sell[df_sell["So luong"] > 20]
        print(f"\n\t\tDON HANG BAN CHAY TRONG THANG {month}")
        print(df_sell.reset_index(drop=True))
        return df_sell, month
    def show_sell(self):
        df_bill = pd.read_csv("bill.csv", sep=',',
                              names=["Ten san pham", "Hang", "Gia", "So luong", "Tong tien","Ten khach hang",
                                     "Ngay","Thang"])
        month=int(input("Nhap thang: "))
        df_sell=df_bill[df_bill["Thang"]==month ]
        print(f"\n\t\tDON HANG TRONG THANG {month}")
        print(df_sell.reset_index(drop=True))
    def profit(self):
        df_bill = pd.read_csv("bill.csv", sep=',',
                              names=["Ten san pham", "Hang", "Gia", "So luong", "Tong tien", "Ten khach hang",
                                     "Ngay", "Thang"])
        month = int(input("Nhap thang: "))
        df_sell = df_bill[df_bill["Thang"] == month]
        print(f"\n\t\tDON HANG BAN TRONG THANG {month}")
        print(df_sell)
        print(f"\nDoanh thu thang {month}:",int(df_sell["Tong tien"].sum()),"USD")
        print(f"\nLoi nhuan thang {month}:", int(df_sell["Tong tien"].sum()*0.15), "USD")
        print("\n")
    def show_product_brand(self):
        df_product = pd.read_csv("product.csv", sep=',', names=["Ten san pham", "Hang", "Gia", "So luong"])
        brand=input("Nhap ten hang muon xem san pham: ")
        df_product_brand=df_product[df_product['Hang']==brand]
        print(df_product_brand)
        return df_product_brand

        
a=Store()
# a.add_brand("Dell")
# a.add_brand("HP")
# a.add_brand("Aplle")
# a.add_brand("HP")
# a.add_brand("Lenovo")
# a.add_brand("Lenovo")
# a.add_product()
# a.save_product()
# a.print_product()
# df_product=pd.read_csv("product.csv",sep=',',names=["Ten san pham","Hang","Gia","So luong"])
# print(df_product.head())
# a.create_bill()
# df_product=pd.read_csv("product.csv",sep=',',names=["Ten san pham","Hang","Gia","So luong"])
# print(df_product.head())
#a.delete_bill()
#a.show_best_seller()
#a.profit()
#a.print_product()
#a.update_product()


