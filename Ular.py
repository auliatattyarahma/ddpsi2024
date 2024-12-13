from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.racun = racun

    def melata(self):
        print(f"Ular {self.nama} itu melata untuk mencari mangsa nya seperti {self.makanan}")

    def lincah(self):
        print(f"ular {self.nama} itu bergerak dengan lincah, dan memiliki warna {self.warna} yang indah")

    def cetak_ular(self):
        super().cetak
        print("nama \t\t: ",self.nama,
              "\nmakanan \t:",self.makanan,
              "\nhidup \t\t: ",self.hidup,
              "\nberkembang biak :",self.berkembang_biak,
              "\nwarna \t\t: ",self.warna,
              "\nracun \t\t: ",self.racun,
              "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
cobra = Ular("Cobra", "Daging", "Darat", "Bertelur", "Hitam", "Berbisa")
cobra.melata()
cobra.lincah()
cobra.cetak_ular()

viper = Ular("viper", "Tikus", "Darat", "Ovovivipar", "Coklat", "Berbisa")
viper.melata()
viper.lincah()
viper.cetak_ular()

boa = Ular("Boa", "Burung", "Darat", "Ovovivipar", "Hijau", "Tidak_Berbisa")
boa.melata()
boa.lincah()
boa.cetak_ular()

sanca = Ular("Sanca", "Tikus", "Darat", "Bertelur", "Hijau", "Tidak_Berbisa")
sanca.melata()
sanca.lincah()
sanca.cetak_ular()