pilihan2="Y"
while pilihan2=="Y":
    print("Halo! apa yang ingin anda lakukan?")
    print("1. Membeli barang")
    print("2. Mengecek barang")
    print("3. Membuat utang")
    print("7. Membayar Hutang")
    print("4. Laporan")
    print("5. Mengatur ulang barang")
    print("6. Menghapus data")

    pilihan = str(input("Masukkan yang ingin dilakukan = "))

    if pilihan == "1":
        count = int(input('Berapa banyak record nilai mahasiswa yang ingin Anda tambahkan? '))
        
        with open('C:/Users/Yudha/Documents/Coding 1/PythonTesting/database.txt' , 'a') as f:
            for i in range(1,count+1):
                print("Masukkan data barang dan jumlah ke-" ,i)
                barang=str(input("Masukkan nama barang = "))
                jmlbarang=int(input("Masukkan jumlah barang = "))
                f.write("\n" + barang + "\t"+ str(jmlbarang))
                

    elif pilihan =="2":
        f = open('C:/Users/Yudha/Documents/Coding 1/PythonTesting/database.txt', 'r')
        print("Stok yang anda miliki       Jumlahnya")
        print(f.read())
        f.close()

    elif pilihan =="3":
        f = open('C:/Users/Yudha/Documents/Coding 1/PythonTesting/utang.txt', 'a')
        utang=int(input("Masukkan jumlah utang yang di inginkan  (Limit 5JT)= "))
        if utang > 5000000:
            print("Anda melebihi limit")

        else:

            f.write(str(utang))
            f.close()

    elif pilihan =="4":
        with open('C:/Users/Yudha/Documents/Coding 1/PythonTesting/database.txt') as file1, open('C:/Users/Yudha/Documents/Coding 1/PythonTesting/utang.txt') as file2:
            baca1 = file1.read()
            baca2 = file2.read()
            print("Stok yang dimiliki     Jumlah stok")
            print(baca1)
            print("Utang yang dimiliki")
            print(baca2)
            file1.close()
            file2.close()

    elif pilihan =="5":
        modif = open('C:/Users/Yudha/Documents/Coding 1/PythonTesting/database.txt' ,'r+')
        list_data = modif.readlines()
        bacadata = modif.read()

        print(bacadata)
        print("Pilih data yang mau diganti")
        ganti=int(input("Masukkan barisnya = "))
        barang=str(input("Masukkan nama barang = "))
        jmlbarang=str(input("Masukkan jumlah barang = "))
        list_data[ganti] = barang +"\t" +jmlbarang

        modif = open('C:/Users/Yudha/Documents/Coding 1/PythonTesting/database.txt' , 'w')
        update = "".join(list_data)

        modif.write(update)
        modif.close()

    elif pilihan =="6":
        print("Pilih data yang mau dihapus")
        ganti=int(input("Masukkan barisnya = "))
        with open("C:/Users/Yudha/Documents/Coding 1/PythonTesting/database.txt", "r") as f:
            list_data = f.readlines()
            
        with open("C:/Users/Yudha/Documents/Coding 1/PythonTesting/database.txt", "w") as f:
            list_data[ganti] = ""
            for line in list_data:
                if line.strip("") != "database_diapus":
                    f.write(line)
            print("Baris ",ganti," telah dihapus")
    elif pilihan =="7":
        utang2 = open('C:/Users/Yudha/Documents/Coding 1/PythonTesting/utang.txt')
        bayaru = utang2.read()

        print("Anda memiliki hutang sebanyak = ")
        print(bayaru)
        utang2.close()
        
        utang2 = open('C:/Users/Yudha/Documents/Coding 1/PythonTesting/utang.txt', 'w')

        bayarut = int(bayaru)


        utang3=int(input("Masukkan jumlah yang ingin dibayarkan = "))

        apdet = bayarut - utang3

        if apdet <=0:
            print("Anda telah melunasi hutang")
            apdet = ""


        
        utang2.write(str(apdet))

        utang2.close()
        
        utang2 = open('C:/Users/Yudha/Documents/Coding 1/PythonTesting/utang.txt')

        print("Utang anda sisa = ")
        print(utang2.read())
        utang2.close()



    else:
        print("salah pilihan")

    pilihan2 = str(input("Mau mengulang? Y/N = "))
    if pilihan2 == "N":
        print("Sedang Keluar....")