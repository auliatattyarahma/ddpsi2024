pilihan = int(input(""" Pilih nomor pilihan :
                      1. Menghitung Luas Persegi 
                      2. Menghitung Luas Lingkaran 
                      3. Menghitung Luas Segitiga """))
match pilihan:
    case 1:
        print("Menghitung Luas Persegi")
        s = int(input("Masukan Nilai Sisi: "))
        luasPersegi = s * s
        print(f"Luas persegi dengan sisi, {s}, adalah {luasPersegi}")
    case 2:
        print("Menghitung Luas Lingkaran")
        pi = 3.14
        r = int(input("Masukan Nilai Jari-Jari"))
        luasLingkaran = pi * r ** 2
        print(f"Luas lingkaran dengan Jari-Jari {r} adalah {luasLingkaran}")
    case 3:
        print("Menghitung Luas Segitiga")
        alas = int(input("Masukkan nlai alas: "))
        tinggi = int(input("Masukan nilai tinggi: "))
        luasSegitiga = 1/2 * alas * tinggi
        print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luasSegitiga}")
    case _:
        print("Input Tidak Valid")