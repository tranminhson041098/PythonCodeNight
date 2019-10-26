print("Chương trình quản lý sinh viên:")
print()
print("Bạn chọn một trong các chức năng sau:")

print("1. Nhập thông tin sinh viên ")
print("2. In danh sách sinh viên đã sắp xếp ")
print("3. Sắp xếp sinh viên theo điểm trung bình ")
print("4. Xếp loại sinh viên ")
print("5. Thoát")

listmenu = [1,2,3,4,5]
def nhapsosinhvien():
    N = int(input("Nhập số sinh viên trong lớp: "))
    return N
def nhaplieusinhvien():
    N = nhapsosinhvien()
    listname =[""]*N
    running = True
    index = 0 
    while running:
        b=input("Nhập tên sinh viên thứ {}: ".format(index+1))
        if (b in ["+","-","*","%","&"]) and b.isdigit():
            print("Trong tên có kí tự sai , mời nhập lại")
            continue
        else :
            index+=1
            listname[index]=b
            running = (index==N)
    
    return listname
# def indanhsach():
#     listdanhsach = listname
#     print(listdanhsach)
    
running =True
while running:
    a=input("Nhập vào chức năng bạn muốn thực hiện: ")
    
    if not (a.isdigit() and int(a) in listmenu):
        print("Chức năng bạn muốn không tồn tại")
        continue
    
    elif int(a)==1:
        print("Chức năng nhập liệu sinh viên")
        nhaplieusinhvien()
        # indanhsach()
    elif int(a)==2:
        print("Chức năng in danh sách sinh viên đã sắp xếp")
    elif int(a)==3:
        print("Chức năng sắp xếp sinh viên theo điểm trung bình")
    elif int(a)==4:
        print("Chức năng xếp loại sinh viên")
    else:
        print("Thoát khỏi ứng dụng")
        c=input("Bạn có thật sự muốn thoát không(Y/N)? ")
        if c.lower() in ["y","yes","true"]:
            break
        else:
            continue

    


        


