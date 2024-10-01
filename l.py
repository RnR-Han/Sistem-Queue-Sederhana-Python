import os
class Queue:
    def __init__(self):
        n = int(input("Masukan Size Queue yang diinginkan :"))
        print("Berhasil terbuat Queue Yang Berkapasitas",n)
        self.size = n
        self.current_size = 0
        self.data = [None] * 0
        self.front = None
        self.back = None

    def isEmpty(self):
        os.system(CLS)
        if self.current_size == 0:
            return True
        else:
            return False

    def isFull(self):
        os.system(CLS)
        if self.current_size == self.size:
            return True
        else:
            return False

    def enqueue(self,newdata):
        os.system(CLS)
        if self.isFull():
            print("Maaf Antrian Sudah Penuh",newdata,"tidak dapat menambah Antrian")
        else:
            if self.back is not None:
                self.back = (self.back + 1),self.size
            else:
                self.front = 0
                self.back = 0

            self.data = newdata
            self.current_size = self.current_size + 1
            print(newdata," Data Telah DiMasukkan Ke antrian")

    def dequeue(self):
        os.system(CLS)
        if self.isEmpty():
            print("Maaf Antrian Kosong, Tidak Bisa Di Keluarkan")
            return None
        else:
            datakeluar = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front + 1), self.size
            self.current_size = self.current_size - 1
            print(datakeluar," Telah Di Keluarkan Dari Antrian")
            return datakeluar

    def printinfo(self):
        os.system(CLS)
        print("\n",100*"-")
        print(20*" ","VIEW ABOUT QUEUE ")
        print(" Capacity Queue : ",self.size)
        print(" How Many Queue : ",self.current_size)
        #Tampilan Jika Kosong
        if self.isEmpty():
            print("Data Posisi Terdepan : -")
            print("Data Pada Posisi Paling Belakang : -")
        else:
            print("Data Pada Posisi Terdepan : ", self.data[self.front])
            print("Data Pada Posisi Terakir  : ", self.data[self.back])
        print("Isi List data ",self.data)
        print(100*"-")

    def visualisasiQueue(self):
        os.system(CLS)
        print("\n Visualisasi Queue \n")
        for i in range(self.size):
            print("     [%2d]     "%(self.size - 1), end = "")
        print()

        for i in range(self.size):
            print(20*"-",end="")

        print()

        jumlahposisikosong = self.size = self.current_size
        for i in range (self.size):
            if i < jumlahposisikosong:
                print("    %10s    "%(""),end="")
            else:
                print("    %10s    "%(self.data[self.front-i-1]),end="")

        print(">>   [DEPAN]",end="")
        print()
        for i in range (self.size):
            print(20*"-",end="")

        print("")

    def menu(self):

        os.system("CLS")
        print("Mesin Antrian Bank Garin")
        print(50*"-")
        print("1. Masukan daftar Antrian (Push) ")
        print("2. Cek Data Antrian (Empty) ")
        print("3. Hapus Data Antrian (Pop)")
        print("4. Keluar Dari Program")
        print(50*"-")
        menu = int(input("Masukan Menu Yang DiPilih : "))
        if menu == 1:
            inputan = int(input("Masukan Jumlah Nasabah :"))
            for i in range(inputan):
                newdata = input(" Tujuan Nasabah [Teller / Costumer Service] : "%(i-1))
                self.enqueue(newdata)
            self.visualisasiQueue()
            input("Tekan Enter Untuk Kembali Ke Menu")
            self.menu()

        elif menu == 2:
            self.printinfo()
            self.visualisasiQueue()
            input("Tekan Enter Untuk Kembali Ke Menu")
            self.menu()

        elif menu == 3:
            self.dequeue()
            self.visualisasiQueue()
            input("Tekan Enter Untuk Kembali Ke Menu")
            self.menu()

        elif menu == 4:
            print("Anda Akan Keluar Program ")
            input("Tekan Enter Untuk Keluar Program....")
            exit()

        else:
            print("Keyword Anda Salah, Mohon Coba Lagi")

#pembatas
Q=Queue()
Q.menu()
