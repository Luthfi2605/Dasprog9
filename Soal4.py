from statistics import median

isi_angka = input('Masukan beberapa angka untuk diidi kedalam list dan pisahkan dengan spasi(minimal 5 angka): ')
angka = list(map(int, isi_angka.split(' ')))
susun_angka = sorted(angka)
print()
print('Dengan data yang anda masukan, kita bisa membuat list seperti ini:')
print(angka)
print('Berikut adalah list yang tersusun dari terkecil hingga terbesar:')
print(susun_angka)
print('Tebesar: %s'%(max(susun_angka)))
print('terkecil: %s'%(min(susun_angka)))
print('Median: %s'%(median(susun_angka)))