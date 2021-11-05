from Store import Store
import os
a=Store()

while True:
    os.system('cls')
    print("\t\tUNG DUNG QUAN LY CUA HANG")
    print("1.Quan ly danh muc")
    print("2.Quan ly don hang")
    print("3.Thong ke bao cao")
    print("0.Thoat")
    choice = int(input("Moi nhap lua chon: "))
    if(choice==1):
        while True:
            os.system('cls')
            print("\n\t\tCHE DO QUAN LY DANH MUC")
            print("1.Xem danh sach cac hang")
            print("2.Them hang moi")
            print("3.Xoa mot hang")
            print("4.Xem toan bo san pham")
            print("5.Xem danh sach san pham ung voi hang")
            print("6.Them san pham")
            print("7.Sua thong tin san pham")
            print("8.Xoa san pham")
            print("0.Thoat")
            choice = int(input("Moi nhap lua chon: "))
            if (choice == 1):
                os.system('cls')
                a.print_brand()
                os.system('pause')
            elif (choice == 2):
                os.system('cls')
                brand=input("Ten hang moi: ")
                a.add_brand(brand)
                os.system('pause')
            elif (choice == 3):
                os.system('cls')
                a.delete_brand()
                os.system('pause')
            elif (choice == 4):
                os.system('cls')
                a.print_product()
                os.system('pause')
            elif (choice==5):
                os.system('cls')
                a.show_product_brand()
                os.system('pause')
            elif (choice==6):
                os.system('cls')
                a.add_product()
                a.save_product()
                os.system('pause')
            elif(choice==7):
                os.system('cls')
                a.update_product()
                os.system('pause')
            elif(choice==8):
                try:
                    os.system('cls')
                    a.remove_product()
                    os.system('pause')
                except:
                    print("Ban da nhap sai vui long thu lai!!!")
                    os.system('pause')
            elif(choice==0):
                break


    elif(choice==2):
        while True:
            os.system('cls')
            print("\n\t\tCHE DO QUAN LY DON HANG")
            print("1.Nhap don hang moi")
            print("2.Xem chi tiet tat ca don hang ")
            print("3.Xem chi tiet don hang trong thang")
            print("4.Cap nhat chi tiet don hang")
            print("5.Xoa don hang")
            print("0.Thoat")
            choice = int(input("Moi nhap lua chon: "))
            if (choice == 1):
                os.system('cls')
                a.create_bill()
                os.system('pause')
            elif (choice == 2):
                os.system('cls')
                a.print_bill()
                os.system('pause')
            elif(choice==3):
                os.system('cls')
                a.show_sell()
                os.system('pause')
            elif (choice == 4):
                os.system('cls')
                a.update_bill()
                os.system('pause')
            elif (choice == 5):
                try:
                    os.system('cls')
                    a.delete_bill()
                    os.system('pause')
                except:
                    print("Ban da nhap sai, vui long thu lai!!!")
                    os.system('pause')
            elif(choice==0):
                break;
    elif(choice==3):
        while True:
            os.system('cls')
            print("\n\t\tTHONG KE BAO CAO")
            print("1.Xem danh sach cac mat hang sap het(con duoi 10 san pham)")
            print("2.Xem danh sach cac mat hang ban chay(ban tren 20 san pham/ thang)")
            print("3.Doanh thu va loi nhuan cua thang")
            print("0.Thoat")
            choice = int(input("Moi nhap lua chon: "))
            if (choice == 1):
                os.system('cls')
                a.show_product_over()
                os.system('pause')
            elif (choice == 2):
                os.system('cls')
                a.show_best_seller()
                os.system('pause')
            elif (choice == 3):
                os.system('cls')
                a.profit()
                os.system('pause')
            elif (choice == 0):
                break
    elif(choice==0):
        os.system('cls')
        break;

