# Eugenius Mario Situmorang - Ilmu Komputer 2021
# Inisiasi list untuk meletakkan kode index huruf
lst_1 = []
lst_2 = []

# Inisiasi hasil kali dengan satu agar tidak menjadi 0 x sesuatu 
hasil_kali_1 = 1
hasil_kali_2 = 1

# Memberi inputan ke dalam program
panjang_codename = int(input())
codename_1 = str(input()).upper()
codename_2 = str(input()).upper()

# 0 sebagai inisiasi index ke-0 jika difind string
huruf = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Memasukkan kode index dari huruf ke dalam list
for i in range(panjang_codename):
    lst_1.append(huruf.find(codename_1[i]))
    lst_2.append(huruf.find(codename_2[i]))

# Mengalikan isi dari setiap list sehingga didapat total perkalian list
for i in range(panjang_codename):
    hasil_kali_1 *= lst_1[i]
    hasil_kali_2 *= lst_2[i]

# Mencari sisa bagi 47
hasil_kali_1 %= 47
hasil_kali_2 %= 47

# Jika sisa bagi bernilai sama maka print "PERGI" dan sebaliknya jika tidak print "TETAP"
if hasil_kali_1 == hasil_kali_2:
    print("PERGI")
else:
    print("TETAP")
    
