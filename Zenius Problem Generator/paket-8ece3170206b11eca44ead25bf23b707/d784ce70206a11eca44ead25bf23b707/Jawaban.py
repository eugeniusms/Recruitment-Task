"""
Program bilangan berpangkat yang dipartisi 3-3 kemudian dijumlahkan secara keseluruhan dari
total hasil partisi yang ada
"""

def partisi_3(bilangan):
    """
    Fungsi untuk membagi bilangan hasil pemangkatan menjadi bagian 3-3 dalam bentuk angka
    kemudian akan dikembalikan keseluruhannya dalam bentuk list(array) menuju fungsi main
    """
    part = ""
    lst_hasil = []
    bilangan = str(bilangan)
    
    # Setiap indeks bilangan habis dibagi 3 maka tambah dan reset ulang pengambilan angka
    for i in range(1, len(bilangan)+1):
        part += bilangan[i - 1]
        if i%3 == 0:
            lst_hasil.append(part)
            part = ""
    
    # Mengubah bentuk string dalam list menjadi integer
    lst_hasil = list(map(int, lst_hasil))
    return lst_hasil


def jumlah(partisi):
    """
    Fungsi untuk menjumlahkan hasil partisi 3 yang sudah didapati sebelumnya dengan cara
    menjumlahkan setiap angka yang terdapat di dalam array kemudian dikembalikan kembali
    menuju fungsi utama.
    """
    total = 0
    for angka in partisi:
        total += angka
    return total

def cetak_jawaban(nama_file, jawaban):
    """
    Fungsi yang digunakan untuk mencetak hasil jawaban ke dalam file Jawaban.txt dengan
    menyertakan detail di dalam file jawaban
    """
    my_file = open(nama_file, mode='w')
    print(jawaban, file=my_file)
    my_file.close()


def main():
    """Fungsi untuk penjalanan program utama di mana di dalam fungsi ini akan diambil nilai
    dari pangkat dan konstanta yang akan di bagi 3-3 di fungsi partisi_3() dan kemudian dijumlahkan 
    di dalam fungsi jumlah(), setelah itu hasilnya akan dikembalikan dan dicetak ke Jawaban.txt 
    melalui fungsi cetak_jawaban().
    """
    # Inisiasi bilangan
    bilangan = 2**1592
    partisi = partisi_3(bilangan)
    total = jumlah(partisi)
    jawaban = "Jumlah partisi-3 2^1592 : {}\nPartisi : {}".format(total, partisi)
    cetak_jawaban("./paket-8ece3170206b11eca44ead25bf23b707/d784ce70206a11eca44ead25bf23b707/Jawaban.txt",jawaban)
    print("Selesai")

# Memulai program
main()