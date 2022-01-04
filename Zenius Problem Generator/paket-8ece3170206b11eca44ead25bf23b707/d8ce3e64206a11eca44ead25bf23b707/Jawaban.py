"""
Program seperti kriptografi atau basis converter antar sistem bilangan. Terdapat dua 
skenario yang saya pahami dalam soal ini:
1. Ketika AAAAAA berlangsung sampai AAAAAJ kemudian berpindah ke AAAABA (Kriptografi)
atau
2. Ketika AAAAAA berlangsung sampai AAAAAZ kemudian berpindah ke AAAABA (Basis-26 Sistem Bilangan)
Berhubung menurut saya kedua kemungkinan ini lebih memungkinkan jika yang dimaksud adalah
tentang basis-26 karena banyaknya kemungkinan P(10059) dibutuhkan maka saya akan menyelesaikan 
permasalahan ini sesuai poin-2
"""

def konversi_26(bilangan):
    """
    Fungsi ini mengonversi dari sistem bilangan desimal menjadi sistem bilangan-26 di mana
    pada setiap angka bitnya akan diubah menjadi bentuk huruf yang memiliki indeks sebanyak
    26 pula.
    """
    # Karena AAAAAAA berperan sebagai awalan = 0
    bilangan = bilangan - 1
    hasil = []

    # Melakukan pengonversian sistem desimal menjadi sistem bilangan-26 dengan digit-6
    while bilangan != 0:
        hasil.append(bilangan % 26)
        bilangan = bilangan // 26
    while len(hasil) != 6:
        hasil.append(0)
    hasil.reverse()

    # Melakukan pengonversian menjadi bentuk huruf untuk dikembalikan ke dalam P()
    konversi = ""
    huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for digit in hasil:
        konversi += huruf[digit]

    return konversi

def cek_palindrom(konversi):
    """
    Fungsi ini mengembalikan nilai 1 jika 6 huruf merupakan palindrom, sebaliknya fungsi
    akan mengembalikan nilai 0 jika 6 huruf tersebut bukan merupakan fungsi palindrom.
    Pengecekan dilakukan dengan melakukan penyamaan indeks huruf ke n dengan indeks huruf
    ke 6-n
    """
    cek = 0
    for i in range(3):
        if konversi[i] == konversi[5-i]:
            cek += 1
    if cek == 3:
        return 1
    else:
        return 0

def deret_palindrom(angka):
    """
    Fungsi yang digunakan untuk menghitung jumlah anggota yang palindrom dari A yaitu P()
    Di fungsi ini akan dijalankan perhitungan satu per satu sehingga didapati semua macam
    bentuk palindrom mulai dari AAAAAA sampai ZZZZZZ kemudian saat menemukan anggota yang
    palindrom dengan cek_palindrom == 1 maka tambahkan indeks palindrom agar didapati 
    indeks palindrom ke n dari anggota A. Fungsi akan mengembalikan indeks ke-n dari P(n).
    """
    DETAIL = ""
    hitung = 1
    palindrom = 0
    while palindrom < angka:
        # Setiap perhitungan akan dikonversi dan dicek apakah palindrom melalui fungsi cek_palindrom()
        konversi = konversi_26(hitung)

        if cek_palindrom(konversi) == 1:
            palindrom += 1
            DETAIL += "\n{} : {}".format(palindrom, konversi)
            # print("\n{} : {}".format(palindrom, konversi))

        if palindrom == angka:
            return konversi, DETAIL
        hitung +=1 

def cetak_jawaban(nama_file, jawaban):
    """
    Fungsi untuk mencetak hasil keluaran yang sudah didapati di dalam program ke suatu file
    bernama nama_file.
    """
    my_file = open(nama_file, mode='w')
    print(jawaban, file=my_file)
    my_file.close()

def main():
    """
    Program ini akan dijalankan dengan fungsi utama main() yang akan melakukan prosedur
    sebagai berikut:
    1. Melakukan pengambilan nilai angka untuk dihitung dalam P() = deret_palindrom()
    2. Sesampainya di perhitungan maka dijalankan pengecekan satu-satu dalam fungsi deret_palindrom
    3. Hasil pengembalian dari pengecekan dikembalikan ke dalam fungsi main dalam bentuk hasil dan DETAIL
    """
    angka = 10059
    hasil, DETAIL = deret_palindrom(angka)
    jawaban = "P({}) adalah : {}{}".format(angka,hasil, DETAIL) 
    cetak_jawaban("./paket-8ece3170206b11eca44ead25bf23b707/d8ce3e64206a11eca44ead25bf23b707/Jawaban.txt",jawaban)
    print("Selesai")

# Memulai program
main()