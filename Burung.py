from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_bulu, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_bulu = warna_bulu
        self.paruh = paruh

    def terbang(self):
        print(f"{self.nama}, terbang di {self.hidup}, dan memakan {self.makanan} ")

    def berkicau(self):
        print(f"{self.nama}, berkicau dengan indah dipagi hari ")

    def cetak_burung(self):
        super().cetak
        print("Nama \t\t:", self.nama,
              "\nMakanan \t:", self.makanan,
              "\nHidup \t\t:", self.hidup,
              "\nBerkembang Biak :", self.berkembang_biak,
              "\nWarna Bulu \t: ", self.warna_bulu,
              "\nParuh \t\t: ", self.paruh,
              "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        
gagak = Burung("Gagak", "Serangga", "Udara", "Bertelur", "Hitam", "Bengkok")
gagak.terbang()
gagak.berkicau()
gagak.cetak_burung()

merpati = Burung("Merpati", "Biji-bijian", "Udara", "Bertelur", "Putih", "Pendek Runcing")
merpati.terbang()
merpati.berkicau()
merpati.cetak_burung()

jalak = Burung("Jalak", "Serangga", "Udara", "Bertelur", "Hitam", "Lurus Runcing")
jalak.terbang()
jalak.berkicau()
jalak.cetak_burung()

murai = Burung("Murai", "Cacing", "Udara", "Bertelur", "Biru", "Lurus Tajam")
murai.terbang()
murai.berkicau()
murai.cetak_burung()