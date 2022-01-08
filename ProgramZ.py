from tkinter import *


root =Tk()
root.title('Program Myob Lite')

root.geometry("800x600")

pesan = 'Selamat datang di Myob v0.5 \n apa yang ingin anda lakukan?'
pesanv= Message(root, text = pesan, width=600)
pesanv.pack()


frame = LabelFrame(root, text="This is frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)




'''def pilihan1():
    windowa = Toplevel(root)
    windowa.title("Memasukkan Barang")
    windowa.geometry("600x480")
    
    label1 = Label(windowa, text="Masukkan jumlah barang yang ingin dimasukkan")
    masukx = Entry(windowa, borderwidth=5)

    buttoni = Button(windowa, text="Klik untuk simpan", command=pilihan1x)

    
    
    masukx.pack()
    label1.pack()
    buttoni.pack()
    return(masukx)'''

def pilihan1x():
        windowb = Toplevel(root)
        windowb.title("Memasukkan Barang")
        windowb.geometry("600x480")

        label1 = Label(windowb, text ="Masukkan Nama Barang")
        masuk = Entry(windowb, borderwidth=5)

        
        label2 = Label(windowb, text ="Masukkan Jumlah Barang")
        masuk2 = Entry(windowb, borderwidth=5)

        button1 = Button(windowb, text="Klik untuk simpan", command=hasil)

        masuk.pack()
        label1.pack()
        masuk2.pack()
        label2.pack()
        button1.pack()

        
def hasil(pilihan1x):

        masuk = pilihan1x()
        masuk2 = pilihan1x()
        print("Anda telah memasukkan = %s \nSebanyak = %s", masuk.get(), masuk2.get())        

def simpan1():

    masuk= pilihan1x()
    masuk2 = pilihan1x()
    
    with open('C:/Users/Yudha/Documents/Coding 1/PythonTesting/database.txt' , 'a') as f:
                
                f.write("\n" + masuk + "\t"+ masuk2)

                f.close()

    label1 = Label(simpan1, text="Anda telah memasukkan")


button1 = Button(root, text="Membeli Barang", command=pilihan1x)
button1.pack()

button2 = Button(root, text="Mengecek Barang")
button2.pack()

button3 = Button(root, text="Membuat Hutang")
button3.pack()

button4 = Button(root, text="Membayar Hutang")
button4.pack()

button5 = Button(root, text="Mengatur ulang Barang")
button5.pack()


root.mainloop()
