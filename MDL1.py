""""
Program Menghitung Segitiga
Luas_segitiga = alas*tinggi / 2
"""
print('luas segitiga simple')
alas = 42
tinggi = 19
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'menghitung fungsi {hitung_luas_segitiga(10,6)}')
print(f'menghitung fungsi {hitung_luas_segitiga(30,15)}')

