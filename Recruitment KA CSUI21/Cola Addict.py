# Menginisiasi variabel dan input
uang, jumlah_toko, harga = input().split()

cola_gratis = []
tiap_beli = []
cola_didapat = []

for i in range(int(jumlah_toko)):
    cola_gratis.append("0")
    tiap_beli.append("0")

# Untuk menuliskan isi dari setiap berapa cola gratis berapa sesuai jumlah toko di awal
for i in range(int(jumlah_toko)):
    cola_gratis[i], tiap_beli[i] = input().split()

# Mencari cola yang normal tanpa gratisan
cola_tanpa_gratis = int(uang) // int(harga)

# Melakukan perulangan pencarian jumlah cola setiap toko sampai toko terakhir
for i in range(int(jumlah_toko)):
    # Mencari hasil bagi div untuk tambahan cola dengan membagi nilai b
    tambahan = cola_tanpa_gratis // int(tiap_beli[i])
    # Mengalikan hasil div dari nilai b di atas dengan nilai a karena tiap b dibeli, tiap a pula didapat
    tambahan *= int(cola_gratis[i])
    # Menjumlahkan total cola beli biasa + bonus toko lalu dimasukkan ke dalam list
    tambahan += cola_tanpa_gratis
    cola_didapat.append(tambahan)
    
print(max(cola_didapat))
