wadah = []
for i in range (10):
    isi_wadah = int(input('Masukan angka ke-%s: '%(i+1)))
    wadah.append(isi_wadah)
print()
print("Isi dari list angka yaang anda masukan adalah:")
print(wadah)
print("Maka total dari semua angka di atas adalah %s"%(sum(wadah)))