"""
Name             : Aplication absent from Tkinter version 1
Created By       : Rahmandani Herlambang (Danias)
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/DaniasHerlambang13/-I-Aplication-Absent-from-Tkinter.git
Thanks to        : Python Tkinter - Mexico Tech - Newbie
"""

from Tkinter import*
import Tkinter as tk
from tkMessageBox  import*
import ttk
import time
import math
import os
import csv
import shutil

class Data (Frame):

    def __init__(self,parent):
        Frame.__init__(self,parent)
        
        self.parent = parent
        self.parent.resizable(False,False)
##        self.parent.overrideredirect(True)
        self.teksJam = StringVar()
        self.badan()


    def badan(self):
        self.update() #memenggil def update dan menjalankanya
        self.teksJam = StringVar()
        
        self.datJam_menu = time.strftime("Daftar Peserta")

        lebar = 1020
        tinggi = 660

        setTengahX = (self.parent.winfo_screenwidth() - lebar)//2
        setTengahY = (self.parent.winfo_screenheight() - tinggi)//2

        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi , setTengahX, setTengahY - 35))


        #-----------------------------------------------------------------
        self.mainFrame = Frame(self.parent, bg= "darkred", relief= RIDGE, bd=10)
        self.mainFrame.pack(fill=BOTH, expand=YES)

        self.parent.title(self.datJam_menu)
        self.menubar = Menu(self.parent)
        self.parent.config(menu = self.menubar)
        fileMenu = Menu(self.menubar, tearoff=0)
        self.fosti = PhotoImage(file='./logofosti/FFOSTI.gif')
        self.menubar.add_cascade(label = 'ABOUT',compound='top',menu = fileMenu)
        fileMenu.add_command( label = 'LINUX TEAM',compound='top',image=self.fosti)

        self.inti=Frame(self.mainFrame , bg = "darkred")
        self.inti.pack(expand=YES, side = LEFT)

        self.intii=Frame(self.mainFrame , bg = "darkred")
        self.intii.pack(expand=YES, side = RIGHT)


        # ************************* penggunaan listbox n scroll

        self.LB=Frame(self.intii , bg = "darkred")
        self.LB.pack(expand=YES, side = RIGHT)

        self.LBB=LabelFrame(self.LB , bg = "darkred",fg='grey',text='Daftar Nama'
                             ,font=('Papyrus', 13))
        self.LBB.pack(expand=YES, side = RIGHT)

        self.LBBB=LabelFrame(self.LBB , bg = "darkred",fg='grey',text='Total Kehadiran'
                             ,font=('Papyrus', 13))
        self.LBBB.pack(expand=YES, side = BOTTOM)

        # ************************* JUMLAH 

        self.Jumlah= Menubutton(self.LBBB ,text="JUMLAH", bg = "darkred", fg="grey",font=('Papyrus', 15))
        self.Jumlah.pack( side=LEFT)

        self.Jumlahh= Entry(self.LBBB , bg = "black",fg="grey", font=('Stencil', 20)
                              ,bd=5, relief= RIDGE)
        self.Jumlahh.pack(side=LEFT)

        # ************************* penggunaan listbox n scroll
        
        self.listboxData=Listbox(self.LBB, bg='black',fg='grey', font=('Stencil', 15),
                                 width=22 , height=20,relief=RIDGE , bd=8)
        self.listboxData.pack(fill=BOTH, side=LEFT,expand=YES)
        s=ttk.Style()
        s.theme_use('classic')
        s.configure('TScrollbar', background='darkred')
        scrollbar = ttk.Scrollbar(self.LBB, orient=VERTICAL,
                                command=self.listboxData.yview,cursor='hand2')
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listboxData.config(yscrollcommand=scrollbar.set)

        #--------------------------------------------------------------

        self.F_isi= Frame (self.inti , bg = "darkred")
        self.F_isi.pack(expand= YES)

        # ************************* button logo

        self.F_atas= Frame(self.F_isi , bg="darkred")
        self.F_atas.pack(expand=YES,side=TOP)
        
        self.logo1 = PhotoImage(file='./logofosti/FOSTI.gif')
        self.logo = Label(self.F_atas,bg="darkred",bd=8, relief= GROOVE)#,image=self.logo1)
        self.logo.pack(expand=YES)

        #-----------------------------------------------------------------

        self.F_isi_kiri= Frame(self.F_isi , bg="darkred",bd=8, relief= GROOVE)
        self.F_isi_kiri.pack(expand=YES,side=LEFT)

        self.L_nama= Menubutton(self.F_isi_kiri ,text="Nama"+ 8*" "+":", bg = "darkred", fg="grey", font=('Old English Text MT', 23))
        self.L_nama.pack(side=TOP, pady=10, padx=3)

        self.L_jurusan= Menubutton(self.F_isi_kiri ,text="Jabatan"+ 5*" "+":", bg = "darkred", fg="grey",font=('Old English Text MT', 23))
        self.L_jurusan.pack(side=TOP, pady=10, padx=3)

        self.L_nomorHp= Menubutton(self.F_isi_kiri ,text="Nomor"+ 6*" "+":", bg = "darkred", fg="grey",font=('Old English Text MT', 23))
        self.L_nomorHp.pack( side=TOP, pady=10, padx=3)

        #------------------------------------------------------------------------
        
        self.F_isi_kanan= Frame(self.F_isi , bg="black",bd=5, relief= GROOVE)
        self.F_isi_kanan.pack(expand=YES,side=RIGHT)

        self.E_nama= Entry(self.F_isi_kanan , bg = "grey", fg="black", font=('Papyrus', 20)
                           ,bd=5, relief= RIDGE,width=33)
        self.E_nama.pack(expand=YES , side=TOP, pady=7, padx=3)

        self.E_jurusan= Entry(self.F_isi_kanan , bg = "grey", fg="black", font=('Papyrus', 20)
                              ,bd=5, relief= RIDGE,width=33)
        self.E_jurusan.pack(expand=YES , side=TOP, pady=7, padx=3)

        self.E_nomorHp= Entry(self.F_isi_kanan , bg = "grey",fg="black", font=('Papyrus', 20)
                              ,bd=5, relief= RIDGE,width=33)
        self.E_nomorHp.pack(expand=YES , side=RIGHT, pady=7, padx=3)
        
        #-------------------------------------------------------------------

        self.F_isi_bawah= Frame(self.inti , bg="black")
        self.F_isi_bawah.pack(expand=YES,side=BOTTOM,fill=BOTH)

        self.F_isi_bawah_kanan= Frame(self.F_isi_bawah , bg="black")
        self.F_isi_bawah_kanan.pack(side=RIGHT)
        
        self.F_isi_bawah_kiri= Frame(self.F_isi_bawah , bg="red")
        self.F_isi_bawah_kiri.pack(side=LEFT)
        
        self.OKE = Button (self.F_isi_bawah_kanan , text="OKE" , bg="darkred" ,fg="black", font=('Stencil', 20)
                           ,command=self.oke,bd=8, relief= RIDGE)
        self.OKE.pack(expand=YES, side=LEFT, pady=10)

        self.OKE = Button (self.F_isi_bawah_kanan , text="RAPAT SELESAI" , bg="black" ,fg="darkred", font=('Stencil', 20)
                           ,command=self.keluar,bd=8, relief= RIDGE,cursor='hand2')
        self.OKE.pack(side=RIGHT ,pady=10, padx=5)
        
        # ************************* label untuk jam()
        self.j = Label(self.F_isi_bawah_kiri,bg='black',textvariable=self.teksJam
                                 ,compound='center',fg='white',font=('Papyrus', 25))
        self.j.pack(side=LEFT)        
    
        #------------------------BUAT FILE
        files=open("FOSTI1.csv","w")
        files.write("NAMA;JABATAN;NOMOR HP\n")
        files.close()

        files=open("FOSTI2.csv","w")
        files.write("NAMA,JABATAN,NOMOR HP\n")
        files.close()

        #------------------------BUAT ANIMASI
        try:
            asd=PhotoImage(file='./logofosti/FOSTI.gif')
            self.canvas = Canvas(self.logo ,width = 700, height = 300,bg="black")    
            self.canvas.pack(side=TOP,expand=YES)
            x0 = -140
            y0 = 140
            x1 = 440
            y1 = 300
            i = 0
            deltax = 2
            deltay = 3
            which = self.canvas.create_image(200,200,image=asd, tag='redBall')
            self.Tampil_awal()            
            while True:
                self.canvas.move('redBall', deltax, deltay)
                self.canvas.after(40)
                self.canvas.update()
                if x1 >= 400:
                    deltax = -2
                if x0 < 0:
                    deltax = 2
                if y1 > 300:
                    deltay = -3
                if y0 < 0:
                    deltay = 3
                x0 += deltax
                x1 += deltax
                y0 += deltay
                y1 += deltay
        except:
            pass
        
    # ************************* jam update menurut waktu lokal pc()   
    def update(self):
        # strftime() berfungsi untuk merubah data waktu secara lokal
        # menjadi bentuk string yang kita inginkan.
        datJam = time.strftime("%H : %M : %S %p " ,
                               time.localtime())

        # mengubah teks jam sesuai dengan waktu saat ini
        self.teksJam.set(datJam)
        
        # perubahan teks jam dalam selang waktu 1 detik (1000 ms)
        self.timer = self.parent.after(1000, self.update)
        
    def oke(self,event=None):
        Tnama    = self.E_nama.get()
        Tjurusan = self.E_jurusan.get()
        TnomorHp = self.E_nomorHp.get()
        
        x=open('FOSTI1.csv')
        x.readline()
        baca=csv.reader(x)
        self.isi=[]

        if Tnama == ''\
           or Tjurusan == ''\
           or TnomorHp == '':
            showerror('FOSTI - UMS','SILAHKAN DILENGKAPI TIDAK BOLEH KOSONG')

        else:
            data1 = open('FOSTI1.csv','a')

            data1.write (Tnama)
            data1.write (";")
            data1.write (Tjurusan)
            data1.write (";")
            data1.write (TnomorHp)
            data1.write (";")
            data1.write ("\n")
            data1.close()

            data2 = open('FOSTI2.csv','a')

            data2.write (Tnama)
            data2.write (",")
            data2.write (Tjurusan)
            data2.write (",")
            data2.write (TnomorHp)
            data2.write (",")
            data2.write ("\n")
            data2.close()
            showinfo('FOSTI - UMS','TERIMAKASIH')       
            self.Kosong()

            #-------------------------------------------------------

            nol = ''
            for item in baca:
                if item[0] == nol:
                    pass
                    
                else:
                    
                    self.isi.append(item)
                    item1 = item[0].split(';')
                     
                    self.listboxData.insert(END, item1[0])
                    self.listboxData.selection_set(0)
                    
            i= len(self.isi)        
            self.Jumlahh.insert(END, i)
            
    def Tampil_awal(self):     
        x=open('FOSTI1.csv')
        x.readline()
        baca=csv.reader(x)
        self.isi=[]

        nol = ''
        for item in baca:
            if item[0] == nol:
                pass
                
            else:
                
                self.isi.append(item)
                item1 = item[0].split(';')
                 
                self.listboxData.insert(END, item1[0])
                self.listboxData.selection_set(0)
                
        i= len(self.isi)        
        self.Jumlahh.insert(END, i)
            
    def Kosong(self):
        self.listboxData.delete(0,END)
        
        self.E_nama.delete(0, END)
        self.E_jurusan.delete(0, END)
        self.E_nomorHp.delete(0, END)
        self.Jumlahh.delete(0, END)

    def keluar(self):
        if askyesno("FOSTI","APAKAH RAPAT SUDAH SELESAI ?"):
            #-------------COPY
            x=str( time.strftime('%A. %d %B %Y - Pukul %H.%M WIB'))

            os.makedirs( r'ABSEN FOSTI - %s'%x)

            shutil.move('FOSTI1.csv', 'ABSEN FOSTI - %s'%x)
            shutil.move('FOSTI2.csv', 'ABSEN FOSTI - %s'%x)

            root.destroy()
        
if __name__ == '__main__':
    root = Tk()
    app = Data(root)
    root.mainloop()
        
