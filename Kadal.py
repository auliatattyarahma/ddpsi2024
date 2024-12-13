from Animal import *

class Kadal(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, ekor, sisik):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.ekor = ekor
        self.sisik = sisik

    def berjemur(self):
        print(f"{self.nama}, memiliki kebiasaan berjemur di bawah sinar matahari")

    def kamuflase(self):
        print(f"Kadal seperti {self.nama}, suka berkamuflase untuk menangkap magsanya seperti {self.makanan}")

    def cetak_kadal(self):
        super().cetak
        print("nama \t\t: ",self.nama,
              "\nmakanan \t:",self.makanan,
              "\nhidup \t\t: ",self.hidup,
              "\nberkembang biak :",self.berkembang_biak,
              "\nekor \t\t: ",self.ekor,
              "\nsisik \t\t: ",self.sisik,
              "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

bunglon = Kadal("Bunglon", "Serangga", "Darat", "Bertelur", "Prehensil", "Berkerut")
bunglon.berjemur()
bunglon.kamuflase()
bunglon.cetak_kadal()

gecko = Kadal("Gecko", "Serangga", "Darat", "Bertelur", "Prehensil", "Mikroskopis")
gecko.berjemur()
gecko.kamuflase()
gecko.cetak_kadal()

iguana = Kadal("Iguana", "Sayuran Hijau", "Darat", "Bertelur", "Panjang", "Berduri")
iguana.berjemur()
iguana.kamuflase()
iguana.cetak_kadal