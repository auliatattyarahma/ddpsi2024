print('---- membuat keterangan ke lulusan ----')
def nilai_kelulusan(nilai):
    if nilai >= 80:
        return 'lulus'
    else :
        return 'gagal'
    
#untuk mencetak value
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))
