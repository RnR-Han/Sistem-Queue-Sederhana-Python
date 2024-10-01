import os
import queue

class myQueue:
    def __init__(self):
        self.items = queue.Queue()
    #Untuk Melihat Stock Barang
    def isEmpty(self):
        return self.items.empty()
    #Untuk Menambah Barang
    def qAdd(self, item):
        self.items.put(item)
    #Untuk Mengeluarkan Barang
    def qOut(self):
        if not self.items.empty():
            return self.items.get()
        else:
            return "Data Antrian Kosong"
    #Membuat Kapsitas Queue
    def size(self):
        return self.items.qsize()
    #Membuat Tampilan Menu
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("cls")
            print("-")
            print("Mesin Antrian Bank Garin")
            print("-")
            print("1. Menambah Antrian (PUSH)")
            print("2. Menghapus Antrian (POP)")
            print("3. Cek Antrian (Empty)")
            print("4. Banyak Antrian Antrian (About)")
            print("5. Keluar Program (EXIT)")
            print("-")
            pilihan = str(input(("Masukan Pilihan Anda : ")))
            if(pilihan == 1):
                os.system("cls")
                obj = str(input("Masukan Nomor Urut Nasabah :"))
                self.qAdd(obj)
                print("Nasabah dengan Nomor Antrian "+obj+" Telah Di Masuk Antrian")
            elif(pilihan == 2):
                os.system("cls")
                temp = self.qOut()
                if temp != "Data Antrian Kosong":
                    print("Nasabah dengan Nomor Antrian "+temp+" Telah Selesai")
                else:
                    print("Antrian Kosong")
                    print("")
            elif(pilihan == 3):
                os.system("cls")
                print(self.isEmpty())
            elif(pilihan == 4):
                os.system("cls")
                print("Kapasitas Queue Adalah"+str(self.size()))
            elif(pilihan == 5):
                print("Terimakasih Telah Menerima Layanan Kami")
                print("Tekan Enter Untuk keluar Program")
                print("Semoga Harimu Menyenangkan")
            else:
                pilih="n"
if __name__== "__main__":
    q = myQueue()
    q.mainmenu

