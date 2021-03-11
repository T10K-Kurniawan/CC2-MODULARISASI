from GMTR.balok import hitung_luas_balok, info as info_balok
from GMTR.persegi import hitung_keliling_kotak, info as info_kotak
from GMTR.segitiga import hitung_luas_segitiga, info as info_segitiga

print(info_segitiga())
print(f"\nhitung_luas_segitiga {hitung_luas_segitiga(70,26)}")
print(info_kotak())
print(f'\nhitung_keliling_kotak {hitung_keliling_kotak(5, 5, 5, 5)}')
print(info_balok())
print(f'\nhitung_luas_balok {hitung_luas_balok(8, 5, 12)}')