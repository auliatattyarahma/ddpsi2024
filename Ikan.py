from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, pola, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.pola = pola
        self.warna = warna

    def perenang(self):
        print(f"ikan {self.nama}, merupakan perenang yang handal di dalam {self.hidup}")

    def indah(self):
        print(f"{self.nama}, memiliki pola {self.pola}, dan warna {self.warna} yang sangat indah")

    def cetak_ikan(self):
        super().cetak
        print("nama \t\t: ", self.nama,
              "\nmakanan \t: ", self.makanan,
              "\nhidup \t\t: ", self.hidup,
              "\nberkembang biak : ", self.berkembang_biak,
              "\npola \t\t: ", self.pola,
              "\nwarna \t\t: ", self.warna,
              "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        
koi = Ikan("Koi", "Cacing Sutra", "Air", "Bertelur", "Kohaku", "Merah")
koi.perenang()
koi.indah()
koi.cetak_ikan()

arwana = Ikan("Arwana", "Serangga", "Air", "Bertelur", "Sisik Berkilau", "Merah")
arwana.perenang()
arwana.indah()
arwana.cetak_ikan()

piranha = Ikan("Piranha", "Daging", "Air", "Bertelur", "Bintik-Bintik Gelap", "Perak")
piranha.perenang()
piranha.indah()
piranha.cetak_ikan()

cupang = Ikan("Cupang", "Pelet", "Air", "Bertelur", "Solid", "Biru")
cupang.perenang()
cupang.indah()
cupang.cetak_ikan()