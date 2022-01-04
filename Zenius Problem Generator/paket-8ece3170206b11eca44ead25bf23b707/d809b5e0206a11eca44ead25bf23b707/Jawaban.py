"""
Program ini menampilkan jawaban dari jumlah a(n) di mana :
a(n) terdefinisi sebagai f(prima_berikut(n)) dengan f(n) adalah fungsi deret fibonacci
dengan basis f(0) = 0 dan f(1) = 1. Sebelum menuju f(n) perhatikan bahwa prima_berikut(n)
merupakan fungsi untuk mengembalikan nilai bilangan prima terkecil setelah n. Pada soal ini
Di minta jumlah a(n) rentang 1123<=n<=2123 dengan jawaban yang sudah dimodulo 1234567929624
"""

def cek_prima(n):
    """
    Fungsi ini digunakan untuk mengecek bilangan prima atau bukan. Bilangan prima didapati
    dengan definisi angka prima hanya habis dibagi angka 1 dan angka itu sendiri.
    """
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def prima_berikut(n):
    """
    Fungsi ini akan mengembalikan bilangan prima terkecil setelah n, pada setiap perulangan 
    pemanggilan angka setelah n maka setiap angka akan dicek keprimaannya sehingga ketika
    didapati angka prima dari fungsi cek_prima() akan dikembalikan ke dalam fungsi fib().
    """
    count = n
    while True:
        count += 1
        # Block ini berfungsi sebagai pengecekan bilangan prima atau bukan
        if cek_prima(count) == True:
            return count

def fib(n):
    """
    Fungsi ini digunakan untuk mencari bilangan fibonacci ke-n dengan cara melakukan fungsi perulangan
    dummie yang sudah ada dengan diawali basis 0 dan 1. Nilai baru didapati dengan menambahkan setiap 
    dua bilangan fibonacci sebelum bilangan n itu sendiri. Nilai akan ditambahkan ke dalam dictionary
    agar tersimpan dan dapat dengan mudah diambil kembali tanpa memakan banyak waktu ketika ingin mencari
    bilangan fibonacci selanjutnya.
    """
    # Melakukan pengumpulan angka fibonacci
    # Angka fibonacci pertama adalah 0, dan yang kedua adalah 1
    fib_dict = {1 : 0, 2 : 1}

    # Jika terdapat n maka langsung kembalikan nilai fibonacci
    if n in fib_dict.keys():
        return fib_dict[n]
    else:
        # Tetapi jika belum dapat melakukan perhitungan terlebih dahulu
        maks = max(fib_dict.keys())
        for i in range(maks + 1, n + 1):
            fib_dict[i] = fib_dict[i-1] + fib_dict[i-2]

    # Nilai yang dikembalikan adalah nilai fibonacci ke-n
    return fib_dict[n]

def cetak_jawaban(nama_file, jawaban):
    """
    Fungsi yang digunakan untuk mencetak hasil jawaban ke dalam file Jawaban.txt dengan
    menyertakan detail di dalam file jawaban
    """
    my_file = open(nama_file, mode='w')
    print(jawaban, file=my_file)
    my_file.close()

def main():
    """
    Fungsi main() berjalan sebagai fungsi utama program di mana pada fungsi ini akan terdapat
    perulangan dengan range yang di minta untuk dijumlahkan hasil fungsi a(n) nya atau fib(n).
    Lalu setelah dijumlahkan akan dimodulo dan dicetak dalam Jawaban.txt
    """
    total = 0
    rentang_1 = 1123
    rentang_2 = 2123
    angka_mod = 1234567929624
    DETAIL = ""
    for i in range(rentang_1, rentang_2 + 1):
        total += fib(prima_berikut(i))
        DETAIL += "\nn : {} | prima_berikut(n) : {} | a(n) : {}".format(i, prima_berikut(i), fib(prima_berikut(i)))
    
    hasil = total % angka_mod
    jawaban = "Jawaban : {}{}".format(hasil, DETAIL)
    cetak_jawaban("./paket-8ece3170206b11eca44ead25bf23b707/d809b5e0206a11eca44ead25bf23b707/Jawaban.txt",jawaban)
    print("Selesai")
   
# Memulai program
main()